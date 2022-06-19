import copy
from itertools import permutations
number = []
fine = []
answer = 0
yeonsan = set()
for i in range(11):
    fine.append(str(i))

def calculate(num1, p, num2):
    if p == "+":
        return num1 + num2
    elif p == '*':
        return num1 * num2
    elif p == '-':
        return num1 - num2

def getMaxNum(pos, number):
    global answer
    for p in pos:
        # print(p)
        i = 0
        while len(number) != 1:
            if i > len(number)-1:
                break
            if number[i] == p:
                val = calculate(number[i-1], number[i], number[i+1])
                number[i] = val
                # print("ssg", number)
                number.pop(i-1)
                # print("2", number)
                number.pop(i)
                # print("3", number)
                i -= 1
            i += 1

        if len(number) == 1:
            answer = max(answer, abs(number[0]))

def solution(expression):
    stack = ""
    for i in expression:
        if i not in fine:
            number.append(int(stack))
            stack = ""
            number.append(i)
            yeonsan.add(i)
        else:
            stack += i
    number.append(int(stack))

    pos = list(permutations(yeonsan))
    for p in pos:
        getMaxNum(p, copy.deepcopy(number))

    return answer

print(solution("50*6-3*2"))
