try:
    l = int(input())
except:
    exit(43)

try:
    n = int(input())
except:
    exit(43)

for i in range(n):
    try:
        int(input())
    except:
        exit(43)

exit(42)