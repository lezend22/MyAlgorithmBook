# dp 문제
# 처음에 다익스트라로 접근했지만, 너무 빡셈
# i = 알골력, j = 코딩력으로 두고 dp[i][j]를 구함
# O(목표 알골력 * 목표 코딩력 * 문제수) 로 해결 가능
def solution(alp, cop, problems):
    answer = 0

    max_alp, max_cop = 0, 0
    for k in range(len(problems)):
        max_alp = max(max_alp, problems[k][0])
        max_cop = max(max_cop, problems[k][1])

    alp, cop = min(alp, max_alp), min(cop, max_cop)

    dp = [[1e9] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for k in range(len(problems)):
                if i >= problems[k][0] and j >= problems[k][1]:
                    next_alp = min(max_alp, i + problems[k][2])
                    next_cop = min(max_cop, j + problems[k][3])
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + problems[k][4])

    answer = dp[-1][-1]
    return answer

# print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))