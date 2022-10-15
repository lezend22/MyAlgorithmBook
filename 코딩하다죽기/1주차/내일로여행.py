import sys


def check(port, cost):
    if port in ["ITX-Saemaeul", "ITX-Cheongchun", "Mugunghwa"]:
        return 0
    elif port in ["S-Train", "V-Train"]:
        return cost / 2
    else:
        return cost

n, ticket = map(int, sys.stdin.readline().split())
city = set(map(str, sys.stdin.readline().split()))

dic = {}
num, INF = 0, 1e9

for i in city:
    dic[i] = num
    num += 1

arr = [[INF] * num for _ in range(num)]
discount = [[INF] * num for _ in range(num)]

for i in range(num):
    arr[i][i] = 0
    discount[i][i] = 0


m = int(sys.stdin.readline())
togo = list(map(str, sys.stdin.readline().split()))

k = int(sys.stdin.readline())
for _ in range(k):
    a, b, c, d = map(str, sys.stdin.readline().split())
    d = int(d)
    dis_cost = check(a, d)
    # print(b, c, d, dis_cost)
    arr[dic[b]][dic[c]] = min(arr[dic[b]][dic[c]], d)
    arr[dic[c]][dic[b]] = min(arr[dic[c]][dic[b]], d)
    discount[dic[b]][dic[c]] = min(discount[dic[b]][dic[c]], dis_cost)
    discount[dic[c]][dic[b]] = min(discount[dic[c]][dic[b]], dis_cost)


for r in range(num):
    for i in range(num):
        for j in range(num):
            arr[i][j] = min(arr[i][j], arr[i][r] + arr[r][j])
            discount[i][j] = min(discount[i][j], discount[i][r] + discount[r][j])

cost1, cost2 = 0, 0
x_go = [dic[x] for x in togo]


for i in range(len(x_go)-1):
    s, e = x_go[i], x_go[i+1]
    # print(arr[s][e], discount[s][e])
    cost1 += arr[s][e]
    cost2 += discount[s][e]

cost2 = cost2 + ticket
cost1 = cost1
# print(cost1, cost2)
if cost2 < cost1:
    print("Yes")
else:
    print("No")

