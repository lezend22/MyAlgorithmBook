import sys
s = sys.stdin.readline().rstrip()

arr = []
for i in range(len(s)):
    arr.append((s[i], i))

arr2 = sorted(arr, key=lambda x:x[0])

order = []
for i in arr2:
    if not order:
        order.append(i)
    else:
        if i[1] == len(s)-1:
            order.append(i)
            break
        if i[1] < order[0][1]:
            continue
        else:
            order.append(i)

stack = []
for i in order:
    stack.append(i[0])
    # print(''.join(stack))

temps = arr.index(order[0])
for i in range(len(order)-1, 0, -1):

    if i == 1:
        temps = arr.index(order[i-1])
        # print("temps", temps)
    # print(i)
    e = order[i][1]
    f = order[i-1][1]
    temp = []
    for j in range(f+1, e):
        temp.append(arr[j])
    temp.sort(key=lambda x:x[0])
    # print(temp)
    for k in temp:
        order.append(k)

# print(order)
temp = []
for i in range(0, temps):
    temp.append(arr[i])

temp.sort(key=lambda x:x[0])
for j in temp:
    order.append(j)
# print(order)

result = []
for i in range(len(order)):
    result.append(order[i])
    result.sort(key=lambda x:x[1])
    for j in result:
        print(j[0], end='')
    if i != len(order)-1:
        print()

# dic = {}
# for i in range(len(s)):
#     dic[s[i]] = i
#
# arr = sorted(s)
# stack = []
# arr2 = []

# def get_key(val):
#     for key, value in dic.items():
#         if value == val:
#             return key





# for i in arr:
#
#     if not stack:
#         stack.append(dic[i])
#         arr2.append(i)
#         print(i)
#     else:
#         if dic[i] < stack[0]:
#             continue
#         else:
#             stack.append(dic[i])
#             arr2.append(i)
#             for j in stack:
#                 print(get_key(j), end='')
#             print()
#
# arr3 = [x for x in arr if x not in arr2]
#
# for i in arr3:
#
#     stack.append(dic[i])
#     stack.sort()
#     for j in stack:
#         print(get_key(j), end='')
#     print()
