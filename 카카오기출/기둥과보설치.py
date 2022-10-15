# 시뮬레이션, n 작다면 언제나 완탐 고려
# 모든 보와 기둥을 전부 아이템화. result 배열에 넣어 관리함.
# 매 frame마다 모든 item을 확인하는 방향으로 구현

def check(result):

    for item in result:
        x, y, a = item
        if a == 0:
            if y != 0 and not ((x, y-1, 0) in result or (x-1, y, 1) in result or (x, y, 1) in result):
                return False
        else:
            if not ((x, y-1, 0) in result or (x+1, y-1, 0) in result or ((x-1, y, 1) in result and (x+1, y, 1) in result)):
                return False

    return True



def solution(n, build_frame):
    result = set()
    for frame in build_frame:
        x, y, a, b = frame
        item = (x, y, a)

        # 설치먼저
        if b == 1:
            result.add(item)
            if not check(result):
                result.remove(item)
        else:
            if item in result:
                result.remove(item)
                if not check(result):
                    result.add(item)

    result = list(result)
    result.sort()
    answer = []
    for i in result:
        answer.append(list(i))

    return answer

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))