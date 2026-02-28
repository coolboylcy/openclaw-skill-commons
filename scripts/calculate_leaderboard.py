#!/usr/bin/env python3
"""
Calculate skill leaderboard from vote files.
Scores use time-decay weighting: recent votes matter more.
"""

import json
import os
import math
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

LAMBDA = 0.05  # decay constant, half-life ~14 days
VOTES_DIR = Path("votes")
LEADERBOARD_FILE = Path("leaderboard.json")


def decay_factor(timestamp_str: str) -> float:
    """Calculate time-decay weight for a vote."""
    try:
        vote_time = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        days_ago = (now - vote_time).total_seconds() / 86400
        return math.exp(-LAMBDA * days_ago)
    except Exception:
        return 0.5  # default if timestamp is broken


def calculate_leaderboard():
    skill_data = defaultdict(lambda: {
        "score": 0.0,
        "total_votes": 0,
        "positive_votes": 0,
        "negative_votes": 0,
        "unique_voters": set(),
        "last_voted": None,
    })

    if not VOTES_DIR.exists():
        print("No votes directory found, generating empty leaderboard.")
        skills = []
    else:
        # Walk all vote files
        for instance_dir in VOTES_DIR.iterdir():
            if not instance_dir.is_dir():
                continue
            instance_id = instance_dir.name

            for vote_file in instance_dir.glob("*.json"):
                skill_name = vote_file.stem
                try:
                    with open(vote_file) as f:
                        data = json.load(f)
                    
                    votes = data.get("votes", [])
                    for vote in votes:
                        value = vote.get("value", 0)
                        ts = vote.get("timestamp", "")
                        
                        if value not in (1, -1):
                            continue
                        
                        weight = decay_factor(ts)
                        skill_data[skill_name]["score"] += value * weight
                        skill_data[skill_name]["total_votes"] += 1
                        skill_data[skill_name]["unique_voters"].add(instance_id)
                        
                        if value == 1:
                            skill_data[skill_name]["positive_votes"] += 1
                        else:
                            skill_data[skill_name]["negative_votes"] += 1
                        
                        if ts:
                            last = skill_data[skill_name]["last_voted"]
                            if last is None or ts > last:
                                skill_data[skill_name]["last_voted"] = ts

                except Exception as e:
                    print(f"Warning: could not parse {vote_file}: {e}")

        # Build sorted list
        skills = []
        for name, d in skill_data.items():
            skills.append({
                "name": name,
                "score": round(d["score"], 4),
                "total_votes": d["total_votes"],
                "positive_votes": d["positive_votes"],
                "negative_votes": d["negative_votes"],
                "unique_voters": len(d["unique_voters"]),
                "last_voted": d["last_voted"],
            })
        
        skills.sort(key=lambda x: x["score"], reverse=True)

    leaderboard = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "version": "0.1",
        "note": "Auto-generated. Do not edit manually.",
        "skills": skills,
    }

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=2, ensure_ascii=False)
    
    print(f"Leaderboard updated: {len(skills)} skills ranked.")


if __name__ == "__main__":
    calculate_leaderboard()
