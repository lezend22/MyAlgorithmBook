import sys
import time
row = ['a','b','c','d','e','f','g','h']
pos = str(sys.stdin.readline().rstrip())
x = ord(pos[0])
y = int(pos[1])
dx, dy = x, y
count = 0
d1 = [-1, 1]
d2 = [-2, 2]

for i in d1:
    dx = x + i
    if chr(dx) in row:
        for j in d2:
            dy = y + j
            if dy >= 1 and dy <= 8:
                count += 1
for i in d2:
    dx = x + i
    if chr(dx) in row:
        for j in d1:
            dy = y + j
            if dy >= 1 and dy <= 9:
                count += 1

print(count)





