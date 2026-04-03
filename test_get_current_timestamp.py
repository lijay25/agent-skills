"""Tests for the get_current_timestamp skill."""

import time
from datetime import datetime, timezone

from get_current_timestamp import get_current_timestamp


def test_returns_dict_with_required_keys():
    result = get_current_timestamp()
    assert "unix_timestamp" in result
    assert "iso8601" in result
    assert "formatted" in result


def test_unix_timestamp_is_recent():
    before = time.time()
    result = get_current_timestamp()
    after = time.time()
    assert before <= result["unix_timestamp"] <= after


def test_iso8601_format():
    result = get_current_timestamp()
    # Should match YYYY-MM-DDTHH:MM:SSZ
    dt = datetime.strptime(result["iso8601"], "%Y-%m-%dT%H:%M:%SZ")
    assert dt.year >= 2024


def test_formatted_format():
    result = get_current_timestamp()
    # Should match YYYY-MM-DD HH:MM:SS
    dt = datetime.strptime(result["formatted"], "%Y-%m-%d %H:%M:%S")
    assert dt.year >= 2024


def test_iso8601_is_utc():
    before_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result = get_current_timestamp()
    after_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # The returned ISO 8601 value should be within the before/after window
    assert before_utc <= result["iso8601"] <= after_utc
