"""
Skill: Get Current Timestamp
Description: Returns the current date and time as a Unix timestamp and formatted string.
"""

from datetime import datetime, timezone


def get_current_timestamp() -> dict:
    """
    Get the current timestamp.

    Returns:
        dict: A dictionary containing:
            - unix_timestamp (float): Current time as a Unix timestamp (seconds since epoch).
            - iso8601 (str): Current time formatted as an ISO 8601 string (UTC).
            - formatted (str): Human-readable local date and time string.
    """
    now_utc = datetime.now(timezone.utc)
    now_local = now_utc.astimezone()
    return {
        "unix_timestamp": now_utc.timestamp(),
        "iso8601": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "formatted": now_local.strftime("%Y-%m-%d %H:%M:%S"),
    }


if __name__ == "__main__":
    result = get_current_timestamp()
    print(f"Unix Timestamp : {result['unix_timestamp']}")
    print(f"ISO 8601 (UTC) : {result['iso8601']}")
    print(f"Formatted      : {result['formatted']}")
