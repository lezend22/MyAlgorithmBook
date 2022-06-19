import sys

t = int(sys.stdin.readline())
for _ in range(t):

    answer = 'YES'
    n = int(sys.stdin.readline())
    phone = []
    dic = {-1}
    for i in range(n):
        num = str(sys.stdin.readline().rstrip())
        phone.append(num)
        dic.add(num)

    # print(dic)
    # print(phone)
    for i in range(n):
        tmp = ''
        dic.remove(phone[i])
        for j in phone[i]:
            tmp += j
            # print(tmp)
            if tmp in dic:
                answer = "NO"
                break
        dic.add(phone[i])

    print(answer)



