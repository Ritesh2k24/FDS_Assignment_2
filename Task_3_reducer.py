# combine counts

#!/usr/bin/env python3
import sys

current_content = None
total = 0

for line in sys.stdin:
    content_id, count = line.strip().split("\t")
    count = int(count)

    if current_content and content_id != current_content:
        if total >= 100:  # threshold
            print(f"{current_content}\tTRENDING\t{total}")
        total = 0

    current_content = content_id
    total += count

if current_content and total >= 100:
    print(f"{current_content}\tTRENDING\t{total}")
