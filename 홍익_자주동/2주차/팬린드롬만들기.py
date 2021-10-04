# if-else 너무더럽게짰음
# 분명코드최적화 가능
# 리스트 A-Z까지 27개 요소에 문자개수 넣음
# 홀수인 글자가 하나만 나와야하고 그 홀수인 숫자가 1인지 1이상인지확인
# odd 변수 를 통해 홀수있는지 확인
# 입출력은 ord()함수 이용
import sys

input = sys.stdin.readline().rstrip()
arr = []
check = True
odd = False
oddNum = 0

#배열에 각 문자 개수 입력
for i in range(26):
    arr.append(input.count(chr(i+65)))

#일단 글자 짝홀검사

for i in range(len(arr)):
    if arr[i] % 2 == 1 and odd == False:
        odd = True
        oddNum = i
    elif arr[i] % 2 == 1 and odd == True:
        check = False

#출력
if check == True:
    for i in range(len(arr)):
        if odd == True and i == oddNum:
            if arr[i] > 1:
                p = arr[i] // 2
                for j in range(p):
                    print(chr(oddNum+65), end='')
            else:
                continue

        elif arr[i] != 0:
            for j in range(arr[i] //2):
                print(chr(i+65), end='')

    if odd == True:
        print(chr(oddNum+65), end='')

    for i in reversed(range(len(arr))):
        if odd == True and oddNum == i:
            if odd == True and i == oddNum:
                if arr[i] > 1:
                    p = arr[i] // 2
                    for j in range(p):
                        print(chr(oddNum + 65), end='')
                else:
                    continue
        elif arr[i] != 0:
            for j in range(arr[i] // 2):
                print(chr(i+65), end='')

else:
    print("I'm Sorry Hansoo")
# if check == True:
#     for i in range(len(arr)):
#         if odd == True and i == oddNum:
#             continue
#         if arr[i] != 0:
#             for j in range(arr[i]//2):
#                 print(chr(i+65), end='')
#
#     if odd == True:
#         for i in range(arr[oddNum]):
#             print(chr(oddNum+65), end='')
#
#     for i in reversed(range(len(arr))):
#         if odd == True and oddNum == i:
#             continue
#         if arr[i] != 0:
#             for j in range(arr[i] // 2):
#                 print(chr(i+65), end='')
#
# else:
#     print("error")



