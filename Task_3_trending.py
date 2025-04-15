#Task 3: Trending Content Identification

#!/usr/bin/env python3
import sys
from collections import defaultdict

content_likes_shares = defaultdict(int)

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) < 4:
        continue

    _, _, action_type, content_id = fields[:4]

    if action_type in ['like', 'share']:
        print(f"{content_id}\t1")
