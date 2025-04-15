#Task 2: Action Aggregation and Sorting

#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) < 4:
        continue
    user_id, _, action_type = fields[:3]
    print(f"{user_id}\t{action_type}\t1")
