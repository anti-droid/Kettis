import sys
import re

try:
    l = input()
    if not re.match(r"(0|([1-9][0-9]*))", l):
        exit(43)
    else:
        l = int(l)
    if not 0 <= l <= 100_000_000_000_000:
        exit(43)
except:
    exit(43)

try:
    n = input()
    if not re.match(r"(0|([1-9][0-9]*))", n):
        exit(43)
    else:
        n = int(n)
    if not 0 <= n <= 100_000:
        exit(43)
except:
    exit(43)

for i in range(n):
    line = input()
    if not re.match(r"(0|([1-9][0-9]*))", line):
        exit(43)
    try:
        d = int(line)
        if not 0 <= d <= 1_000_000_000:
            exit(43)
    except:
        exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)
exit(42)