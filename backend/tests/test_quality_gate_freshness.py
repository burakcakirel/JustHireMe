"""Freshness gate fails closed on undated scraped postings (Tier-1 fix).

Previously a posting with no parseable date got a free pass ("freshness
unknown"), so stale jobs flowed into the (auto-apply) pipeline. Now an undated
lead is treated as not-fresh unless it came from a recency-constrained source.
"""
from datetime import datetime, timezone

from discovery.quality_gate import _freshness, _parse_date, evaluate_lead_quality

_GOOD_DESC = (
    "Entry-level fully remote React and TypeScript role building API workflows "
    "and dashboards. Clear apply path, mentorship, and a portfolio review. We "
    "value shipping over credentials and welcome new-grad applicants."
)


# --- _freshness unit behavior ---------------------------------------------------

def test_undated_lead_fails_closed():
    fresh, reason = _freshness({"title": "x"})
    assert fresh is False
    assert "no posting date" in reason


def test_undated_with_fresh_source_top_level_passes():
    fresh, _ = _freshness({"_fresh_source": "google_past_week"})
    assert fresh is True


def test_undated_with_fresh_source_in_meta_passes():
    fresh, _ = _freshness({"source_meta": {"fresh_source": "google_past_week"}})
    assert fresh is True


def test_recent_dated_lead_is_fresh():
    fresh, _ = _freshness({"posted_date": "today"})
    assert fresh is True


def test_stale_dated_lead_keeps_stale_wording():
    fresh, reason = _freshness({"posted_date": "2020-01-01"})
    assert fresh is False
    assert "stale posting" in reason  # existing callers/tests rely on this phrasing


# --- end-to-end through the gate ------------------------------------------------

def test_undated_lead_is_penalized_and_rejected():
    q = evaluate_lead_quality({
        "title": "Junior React Developer", "company": "Acme",
        "url": "https://jobs.example.com/x", "platform": "search",
        "description": _GOOD_DESC, "signal_score": 80,
        # no posted_date, no fresh_source -> fail closed
    })
    assert "no posting date" in q["reason"]
    assert q["accepted"] is False


def test_undated_but_fresh_source_is_accepted():
    q = evaluate_lead_quality({
        "title": "Junior React Developer", "company": "Acme",
        "url": "https://jobs.example.com/x", "platform": "search",
        "description": _GOOD_DESC, "signal_score": 88,
        "source_meta": {"fresh_source": "google_past_week"},
    })
    assert q["accepted"] is True


# --- _parse_date ISO-8601 with colon timezone offset ----------------------------

def test_parse_date_iso_8601_with_colon_tz():
    """ISO-8601 with colon timezone offset must parse without warning."""
    dt = _parse_date("2026-06-05T14:21:12+00:00")
    assert dt is not None
    assert dt.year == 2026
    assert dt.month == 6
    assert dt.day == 5
    assert dt.hour == 14
    assert dt.minute == 21
    assert dt.second == 12
    assert dt.tzinfo is not None


def test_parse_date_iso_8601_z_suffix():
    """ISO-8601 with Z suffix still parses."""
    dt = _parse_date("2026-06-05T14:21:12Z")
    assert dt is not None
    assert dt.year == 2026
    assert dt.month == 6


def test_parse_date_naive_is_utc():
    """Naive ISO-8601 gets UTC timezone attached."""
    dt = _parse_date("2026-06-05T14:21:12")
    assert dt is not None
    assert dt.tzinfo is not None
    assert dt.tzinfo.utcoffset(None).total_seconds() == 0


def test_parse_date_invalid_returns_none():
    """Unparseable strings return None without warning."""
    result = _parse_date("not-a-date")
    assert result is None
