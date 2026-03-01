import random

ll = int(input()) # The drinking limit for the country
n = int(input()) #The amount of cases
m = int(input()) #0 for random cases, 1 for manual input
if m == 0:
    r = int(input()) #If set to random cases, asks for a range for the cases


d = {}
if m == 1:
    for i in range (n):
        d[i] = int(input()) #Manual inputs for cases

print(ll)
print(n)
for i in range (n):
    if m == 0:
        print(random.randint(0, r))
    else:
        print(d[i])
