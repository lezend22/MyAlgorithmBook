import sys

s = list(sys.stdin.readline().rstrip())
result = [""] * len(s)

def func(arr, start):

    if not arr:
        return

    min1 = min(arr)
    idx = arr.index(min1)
    result[start+idx] = min1
    print("".join(result))
    func(arr[idx+1:], start+idx+1)
    func(arr[:idx], start)

func(s, 0)