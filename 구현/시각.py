import sys

n = int(input())
count = 0
for x in range(n+1):
    for y in range(60):
        for z in range(60):
            nx = x // 10
            ny = y // 10
            nz = z // 10
            if x % 10 == 3 or y % 10 == 3 or z % 10 == 3 or nx == 3 or ny == 3 or nz == 3:
                count += 1

print(count)

"""Sol2

for x in range(n+1):
    for y in range(60):
        for z in range(60):
            if '3' in str(x) + str(y) + str(z):
                count += 1
print(count)

***