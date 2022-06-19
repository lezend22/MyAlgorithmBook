import sys

s = list(sys.stdin.readline().rstrip())
result = [""] * len(s)

def func(start, arr):
    global result

    if len(arr) == 0:
        # print(arr)
        return

    min_ = min(arr)
    index = arr.index(min_)
    result[start + index] = min_
    print("".join(result))

    func(start + index + 1, arr[index+1:])
    func(start, arr[:index])

func(0, s)