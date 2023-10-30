# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
권투 경기는 1대1 방식으로 진행이 되고,
만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때, 
정확하게 순위를 매길 수 있는 선수의 수를 return

입력 #1
N       : 5
results : [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

출력 #1
2

입출력 예 설명 #1
2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위

cf. Floyd-Warshell 알고리즘
한 점에서 다른 점까지의 거리를 (한 다리 거쳐서) 찾을 수 있는 알고리즘
"""


def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][i] == None:
                    continue

                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]

    answer = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i + 1 :]:
            continue
        answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
