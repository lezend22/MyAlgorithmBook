import sys

arr = sys.stdin.readline().rstrip()
ans = True

def solution(arr):
    global ans
    idx = 0
    while idx < len(arr):

        if arr[idx:idx+2] == '10':
            idx += 2
            if arr[idx] != '0':
                ans = False
                return
            while idx < len(arr) and arr[idx] == '0':
                # print(arr[idx], idx)
                ans = False
                idx += 1
                continue
            if idx >= len(arr):
                ans = False
                break

            if arr[idx] == 'ssg':
                ans = True
                while idx < len(arr) and arr[idx] == 'ssg':
                    idx += 1
                    continue

        if arr[idx:idx+2] == '01':
            idx += 2
            continue

        else:
            ans = False
            return

solution(arr)
if ans:
    print("SUBMARINE")
else:
    print("NOISE")