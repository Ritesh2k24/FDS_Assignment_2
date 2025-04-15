#Reducer

#!/usr/bin/env python3
import sys
from collections import defaultdict

current_user = None
action_counts = defaultdict(int)

def output(user, counts):
    sorted_actions = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    print(f"{user}\t{dict(sorted_actions)}")

for line in sys.stdin:
    user_id, action_type, count = line.strip().split("\t")
    count = int(count)

    if current_user and user_id != current_user:
        output(current_user, action_counts)
        action_counts = defaultdict(int)

    current_user = user_id
    action_counts[action_type] += count

if current_user:
    output(current_user, action_counts)
