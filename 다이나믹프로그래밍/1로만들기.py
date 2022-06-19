import sys

x = int(sys.stdin.readline())

# count = 0
#
# while(x != ssg):
#
#     if x == 2:
#         x = x // 2
#         count += ssg
#
#     if x % 5 == 0:
#         x = x // 5
#         count += ssg
#     elif x % 3 == 0:
#         x = x // 3
#         count += ssg
#     else:
#         x -= ssg
#         count += ssg
#
# print(count)

#존너 희한하게 풀었네,,
#모범답안 (다이나믹프로그래밍) 어렵다,,직관적으로안보인다,,

d = [0] * 30001 # 0~30000까지

for i in range(2, x+1):
    d[i] = d[i-1] + 1   #일단 1빼기 부터 해보고 나중에 비교
    if i % 2 == 0:      #elif쓰면안되는게 2, 3, 5 공통 약수를 갖고있을 수도있음
        d[i] = min(d[i], d[i//2]+1) #1뺀것과 나눈것 중 어떤것이 더 최소인지 찾음
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5]+1)

print(d[x])