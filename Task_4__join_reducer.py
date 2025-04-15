#!/usr/bin/env python3
import sys

current_user = None
profile = None
activities = []

for line in sys.stdin:
    user_id, tag, data = line.strip().split("\t", 2)

    if current_user and user_id != current_user:
        if profile:
            for activity in activities:
                print(f"{current_user}\t{profile}\t{activity}")
        current_user = user_id
        profile, activities = None, []

    current_user = user_id
    if tag == "PROFILE":
        profile = data
    elif tag == "ACTIVITY":
        activities.append(data)

if profile:
    for activity in activities:
        print(f"{current_user}\t{profile}\t{activity}")
