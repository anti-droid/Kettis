import sys
import re


data = sys.stdin.read()
if not data.endswith("\n"):
    sys.exit(43)
lines = data.split('\n')
if lines[-1] != "":
    sys.exit(43)
lines.pop()

print(lines)
l = lines[0]
if not re.fullmatch(r"^(0|([1-9][0-9]*))$", l):
    exit(43)
else:
    l = int(l)
if not 0 <= l <= 100_000_000_000_000:
    exit(43)

n = lines[1]
if not re.fullmatch(r"^(0|([1-9][0-9]*))$", n):
    exit(43)
else:
    n = int(n)
if not 0 <= n <= 100_000:
    exit(43)

if len(lines) != 2 + n:
    sys.exit(43)

for i in range(2, 2 + n):
    line = lines[i]
    if not re.fullmatch(r"^(0|([1-9][0-9]*))$", line):
        exit(43)
    d = int(line)
    if not 0 <= d <= 1_000_000_000:
        exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)
exit(42)