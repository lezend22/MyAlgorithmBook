

def solution(commands):
    n = 50
    arr = [[dict() for _ in range(50)] for _ in range(50)]
    dic = {}
    answer = []

    for command in commands:
        print(command)

        if command[:6] == "UPDATE":
            com = list(map(str, command.split()))
            if len(com) == 3:
                a, b, c = com

                for i in range(n):
                    for j in range(n):
                        if (i, j) in dic.keys():
                            i, j = dic[(i, j)]
                        if arr[i][j] == b:
                            print(arr[i][j])
                            arr[i][j] = c

            else:
                a, b, c, d = command.split()
                b, c = int(b), int(c)
                if (b, c) in dic.keys():
                    b, c = dic[(b, c)]

                arr[b][c] = d

        elif command[:8] == "UNMERGE":
            com = list(map(str, command.split()))
            a, b, c = command.split()
            b, c = int(b), int(c)
            del dic[(b, c)]

        elif command[0] == "PRINT":
            a, b, c = command.split()
            b, c = int(b), int(c)
            if not arr[b][c]:
                answer.append("EMPTY")
            else:
                answer.append(*arr[b][c])



        elif command[0] == "MERGE":
            a, b, c, d, e = command.split()
            b, c, d, e = int(b), int(c), int(d), int(e)
            dic[(d, e)] = (b, c)




    print(answer)

    return answer

solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])