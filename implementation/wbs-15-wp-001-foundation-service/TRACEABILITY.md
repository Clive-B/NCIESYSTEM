# WBS-15-WP-001 Traceability

| Implementation artifact | Source authority | Verification mapping | Current status |
|---|---|---|---|
| `src/ncie_foundation/app.py` health/readiness | NCIE-004 Ch.5; NCIE-002 Ch.27; NCIE-015 Ch.10/20 | Local contract tests; NCIE-016 code-level and operational verification later | TEST SPECIFIED |
| Correlation handling and problem details | NCIE-004 Ch.2, Ch.5, Ch.8; NCIE-002 Ch.25 | Local contract tests; integration verification later | TEST SPECIFIED |
| `config.py` secret references | NCIE-004 Ch.24; NCIE-015 Ch.4 | Local unit tests; security verification later | TEST SPECIFIED |
| `structured_logging.py` | NCIE-004 Ch.26; NCIE-015 Ch.20 | Local unit tests; observability/security verification later | TEST SPECIFIED |
| `telemetry.py` hook protocol | NCIE-004 Ch.26; NCIE-015 Ch.20 | Interface/unit verification now; exporter integration later | TEST SPECIFIED |
| `authorization.py` deny-all default | NCIE-004 Ch.5; NCIE-009 boundary remains upstream | Local unit test; WBS-16 security verification later | TEST SPECIFIED |
| `access_control.py` mapping decision point | NCIE-009 Ch.6 Table 9; W16-D11-A | Empty-registry, four-layer integration, current/exact and stale/revoked/ambiguous negative tests | LOCALLY VERIFIED |
| `access_control.py` delegation contracts | NCIE-009 Ch.7 Table 11; W16-D12-A | Four-class taxonomy, non-expansion, attribution, expiry/revocation and deputisation tests | LOCALLY VERIFIED |
| `access_control.py` privileged-access contracts | NCIE-009 Ch.8 Table 13; W16-D13-A | Three-class/interface, unassigned-authority, self-approval, expiry/revocation and content-separation tests | LOCALLY VERIFIED |
| `access_control.py` emergency contracts | NCIE-009 Ch.9 Table 15; W16-D14-A | Three-class trigger/action, zero-eligibility, auto-expiry, revocation, notification and independent-review tests | LOCALLY VERIFIED |

## Explicit limitations

- Python 3.14.7 and PyPI are approved by `NCIE-WBS15-OWNER-DECISION-2026-09-17-002`; development dependencies are version- and hash-locked for Windows x86-64.
- FastAPI is not installed or imported; the service uses the standard ASGI protocol.
- No authentication provider, authorization policy, database, queue, cache, external connector, telemetry exporter or production host is configured.
- The WP-004 institutional mapping registry and operational privilege/emergency authority boundaries are empty. `UNASSIGNED = NO GRANT / DENY`.
- Readiness indicates only whether this local template can receive requests. It never represents business correctness, institutional Evidence, Human approval or production acceptance.
- Python tests cannot be executed until an approved interpreter/toolchain exists on the workstation.
