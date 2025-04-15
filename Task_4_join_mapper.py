#Task 4: Join with user_profiles.txt

#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) == 2:
        print(f"{fields[0]}\tPROFILE\t{fields[1]}")
    else:
        print(f"{fields[0]}\tACTIVITY\t{','.join(fields[1:])}")
