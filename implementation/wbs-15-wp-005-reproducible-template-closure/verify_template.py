"""Verify the WBS-15 source-tree template using only the Python standard library."""

import asyncio
import json
import sys
import tomllib
from pathlib import Path
from typing import Any, cast


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("rb") as stream:
        return cast(dict[str, Any], json.load(stream))


def load_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as stream:
        return tomllib.load(stream)


def verify_lock(lock_path: Path) -> tuple[int, int]:
    text = lock_path.read_text(encoding="utf-8")
    package_count = sum(
        1 for line in text.splitlines() if "==" in line and not line.lstrip().startswith("#")
    )
    hash_count = text.count("--hash=sha256:")
    require(package_count > 0, "Development lock must contain exact packages")
    require(package_count == hash_count, "Every locked package must have one SHA-256 hash")
    return package_count, hash_count


async def verify_runtime(source_root: Path) -> dict[str, Any]:
    sys.path.insert(0, str(source_root))
    from ncie_foundation.composition import compose_foundation_service
    from ncie_foundation.harness import InProcessHarness

    service = compose_foundation_service(
        {
            "NCIE_SERVICE_NAME": "ncie-wp005-verification",
            "NCIE_SERVICE_VERSION": "0.0.0-verification",
            "NCIE_ENVIRONMENT": "local-clean-verification",
            "NCIE_CONFIG_SCHEMA_VERSION": "1",
        }
    )
    harness = InProcessHarness(service)
    before = await harness.request("/health/ready")
    await harness.start()
    live = await harness.request("/health/live")
    ready = await harness.request("/health/ready")
    await harness.stop()
    after = await harness.request("/health/ready")

    require(before.status_code == 503, "Readiness must fail closed before startup")
    require(live.status_code == 200, "Liveness must respond after startup")
    require(ready.status_code == 200, "Readiness must respond after explicit startup")
    require(after.status_code == 503, "Readiness must fail closed after shutdown")
    require(
        not bool(ready.payload["authoritativeBusinessState"]), "Health cannot be business state"
    )
    require(ready.payload["productionAcceptance"] == "PENDING", "Acceptance must remain pending")
    return {
        "beforeStart": before.status_code,
        "live": live.status_code,
        "ready": ready.status_code,
        "afterStop": after.status_code,
    }


def main() -> int:
    closure_root = Path(__file__).resolve().parent
    implementation_root = closure_root.parent
    foundation_root = implementation_root / "wbs-15-wp-001-foundation-service"
    manifest = load_json(closure_root / "SERVICE_TEMPLATE_MANIFEST.json")
    project = load_toml(foundation_root / "pyproject.toml")

    require(sys.version_info[:3] == (3, 14, 7), "Verification requires approved Python 3.14.7")
    require(manifest["runtime"]["applicationBoundary"] == "ASGI", "ASGI boundary required")
    require(not manifest["runtime"]["frameworkSelected"], "Framework must remain deferred")
    require(manifest["runtime"]["runtimeDependencies"] == [], "Runtime dependencies prohibited")
    require(project["project"]["dependencies"] == [], "Project runtime dependencies prohibited")
    require(not project["tool"]["ncie"]["production-authorized"], "Production cannot be authorized")
    require(project["tool"]["ncie"]["acceptance-status"] == "PENDING", "Acceptance must be pending")

    expected_work_packages = [f"WBS-15-WP-{number:03d}" for number in range(1, 6)]
    require(
        project["tool"]["ncie"]["work-packages"] == expected_work_packages,
        "Project work-package manifest is incomplete",
    )
    package_count, hash_count = verify_lock(foundation_root / "requirements-dev.lock")
    runtime = asyncio.run(verify_runtime(foundation_root / "src"))
    result = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "lockedPackages": package_count,
        "lockedHashes": hash_count,
        "runtime": runtime,
        "productionAuthorized": False,
        "controlledAcceptance": "PENDING",
    }
    print(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
