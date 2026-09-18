"""Structured logging that does not serialize arbitrary request or secret data."""

import json
import logging
from datetime import UTC, datetime
from typing import Any


class NcieJsonFormatter(logging.Formatter):
    """Emit the minimum operational fields allowed by the foundation scope."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "signalCategory": getattr(record, "signal_category", "PLATFORM_HEALTH"),
            "classification": getattr(record, "classification", "NOT_SET"),
            "protectedValuesIncluded": False,
        }
        correlation_id = getattr(record, "correlation_id", None)
        trace_id = getattr(record, "trace_id", None)
        if correlation_id:
            payload["correlationId"] = correlation_id
        if trace_id:
            payload["traceId"] = trace_id
        return json.dumps(payload, separators=(",", ":"), sort_keys=True)
