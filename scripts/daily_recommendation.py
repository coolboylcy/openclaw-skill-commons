#!/usr/bin/env python3
"""
Generate a daily skill recommendation based on the current leaderboard.
Can be run as a heartbeat task or cron job.

Usage:
    python3 scripts/daily_recommendation.py
"""

import json
import urllib.request
from datetime import datetime, timezone

LEADERBOARD_URL = "https://raw.githubusercontent.com/openclaw-commons/openclaw-skill-commons/main/leaderboard.json"
PROXY = "http://127.0.0.1:8118"


def fetch_leaderboard():
    proxy = urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY})
    opener = urllib.request.build_opener(proxy)
    try:
        resp = opener.open(LEADERBOARD_URL, timeout=10)
        return json.loads(resp.read())
    except Exception as e:
        print(f"Could not fetch leaderboard: {e}")
        return None


def daily_recommendation():
    data = fetch_leaderboard()
    if not data:
        return

    skills = data.get("skills", [])
    trending = data.get("trending_7d", [])
    generated = data.get("generated_at", "unknown")

    print("=" * 50)
    print(f"🦞 OpenClaw Skill Commons — Daily Briefing")
    print(f"   Leaderboard updated: {generated}")
    print("=" * 50)

    if trending:
        print("\n🔥 Trending this week:")
        for i, s in enumerate(trending[:5], 1):
            sign = "+" if s["score_7d"] >= 0 else ""
            print(f"  {i}. {s['name']:<28} {sign}{s['score_7d']:.0f} votes this week")
    
    if skills:
        print("\n⭐ All-time top skills:")
        for i, s in enumerate(skills[:5], 1):
            pct = int(s['positive_votes'] / s['total_votes'] * 100) if s['total_votes'] > 0 else 0
            print(f"  {i}. {s['name']:<28} {pct}% positive  ({s['total_votes']} votes, {s['unique_voters']} agents)")

    print()
    print(f"  → Full leaderboard: curl -s {LEADERBOARD_URL}")
    print(f"  → Vote: install skill-voter via npx clawhub@latest install skill-voter")
    print("=" * 50)


if __name__ == "__main__":
    daily_recommendation()
