import sys


n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())

result = float("-inf")
def calc(a, b, c):

    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    else:
        return a * b

def chain(index, ret):
    global result

    if index >= len(opers):
        result = max(result, ret)
        return

    chain(index+1, calc(ret, nums[index+1], opers[index]))
    # print(result)
    if index+1 < len(opers):
        chain(index+2, calc(ret, calc(nums[index+1], nums[index+2], opers[index+1]), opers[index]))
        # print(result)


def arrSplit():
    for i in arr:
        if i.isdigit():
            nums.append(int(i))
        else:
            opers.append(i)

nums = []
opers = []

arrSplit()
chain(0, nums[0])
print(result)