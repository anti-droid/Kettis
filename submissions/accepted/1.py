l = int(input())
n = int(input())

drinks = []
for i in range(n):
    drinks.append(int(input()))

drinks.sort()
current = 0
total = 0
for d in drinks:
    if current + d <= l:
        current += d
        total += 1
    else:
        break
print(total)



# IDEAS:
# - 0 drinks
# - Integer overflow