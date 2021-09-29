import sys

arr = list(sys.stdin.readline().rstrip())
stack = []
result = 0
for i in range(len(arr)):
    if arr[i] == ')':

        if arr[i-1] == '(':
            stack.pop()
            result = result + len(stack)

        else:
            stack.pop()
            result = result + 1


    # '('가 오는경우
    else:
        stack.append(arr[i])

print(result)

# visited = [0] * len(arr)
# count = 0
# cut = 0
# total = 0
#
# for i in range(len(arr)):
#     count = 0
#     if arr[i] == '(' and visited[i] == 0 and arr[i+1] != ')':
#         for j in range(i+1, len(arr)):
#             if arr[j] == '(' and arr[j+1] != ')':
#                 count += 1
#             elif arr[j] == ')' and arr[j-1] != '(':
#                 if count == 0:
#                     visited[i] = j
#                     break
#                 else:
#                     count -= 1
#
# for i in range(len(visited)):
#     cut = 0
#     if visited[i] != 0:
#         for j in range(i+1, visited[i]):
#             if arr[j] == '(' and arr[j+1] == ')':
#                 cut += 1
#         total += (cut + 1)
#
# print(total)