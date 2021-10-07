# 스택을이용하여 하나씩 넣어봄
# 마지막에 넣은 글자를 계속검사하여
# explosive의 마지막과 같을경우 word검색
# index slicing을 이용하여 간결한 코드구성 가능
import sys
arr = sys.stdin.readline().rstrip()
explosive = sys.stdin.readline().rstrip()

lastchar = explosive[-1]
stack = []
length = len(explosive)

for i in arr:
    stack.append(i)
    # print(stack[-length:])
    if i == lastchar and ''.join(stack[-length:]) == explosive:
        del stack[-length:]

result = ''.join(stack)
if result != '':
    print(result)
else:
    print("FRULA")

# O(N * N) 너무오래걸리는코드 시간초과.
# input = sys.stdin.readline().rstrip()
# c4 = sys.stdin.readline().rstrip()
#
# arr = list(input)
# find = input.find(c4)
#
# while find != -1:
#
#     for i in range(len(c4)):
#         arr.pop(find)
#
#     input = ''.join(arr)
#     find = input.find(c4)
#
# if len(input) > 0:
#     print(input)
# else:
#     print("FRULA")



