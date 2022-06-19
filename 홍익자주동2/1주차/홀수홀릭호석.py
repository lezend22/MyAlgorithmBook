import sys

a = sys.stdin.readline().rstrip()
result = []

def func(arr, ret):

    # print(arr)
    tmp = 0
    for i in arr:
        if int(i) % 2 != 0:
            tmp += 1
    ret += tmp
    if len(arr) >= 3:
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                # print("########")
                s1 = int(arr[:i+1])
                s2 = int(arr[i+1:j+1])
                s3 = int(arr[j+1:])
                func(str(s1+s2+s3), ret)

    elif 2 <= len(arr) < 3:
        s = int(arr[0]) + int(arr[1])
        func(str(s), ret)
    else:
        global result
        result.append(ret)


func(a, 0)
# print(result)
print(min(result), max(result))