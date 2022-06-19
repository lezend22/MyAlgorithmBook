import sys

# (100~ssg~|01)~
sound = sys.stdin.readline().rstrip()
ans = True

def solution(sound):
    global ans
    flag = False
    idx = 0
    while idx < len(sound):
        if sound[idx:idx+3] == '100':
            # print(sound[idx:idx + 3], idx)
            idx += 3
            if idx >= len(sound):
                ans = False
                break
            while sound[idx] == '0':
                if idx >= len(sound):
                    break
                ans = False
                idx += 1
                continue
            if idx < len(sound) and sound[idx] == 'ssg':
                if idx >= len(sound):
                    break
                ans = True
                flag = True
                idx += 1
                continue

        if sound[idx:idx+2] == '01':
            # print(sound[idx:idx+2])
            idx += 2
            continue

        if flag:
            while idx < len(sound) and sound[idx] == 'ssg':
                # print(sound[idx], idx)
                idx += 1
                continue
            flag = False
            continue

        else:
            # print(sound[idx:])
            ans = False
            break

solution(sound)
if ans:
    print("SUBMARINE")
else:
    print("NOISE")