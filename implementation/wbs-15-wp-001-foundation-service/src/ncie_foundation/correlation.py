"""Correlation ID handling required by NCIE service boundaries."""

CORRELATION_HEADER = b"x-correlation-id"


def correlation_id_from_headers(headers: list[tuple[bytes, bytes]]) -> str | None:
    for name, value in headers:
        if name.lower() == CORRELATION_HEADER:
            decoded = value.decode("utf-8", errors="strict").strip()
            return decoded or None
    return None
