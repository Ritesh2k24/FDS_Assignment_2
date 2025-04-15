# Task 1: Data Cleansing and Parsing
#!/usr/bin/env python3
import sys
import json
from datetime import datetime

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) != 5:
        continue

    timestamp, user_id, action_type, content_id, metadata = fields

    try:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        json_obj = json.loads(metadata)
    except:
        continue

    print(f"{user_id}\t{timestamp}\t{action_type}\t{content_id}\t{metadata}")
