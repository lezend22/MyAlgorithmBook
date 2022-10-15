import sys
from math import ceil

a, b, c = map(int, sys.stdin.readline().split())
result = ceil((c - b) / (a - b))
print(result)