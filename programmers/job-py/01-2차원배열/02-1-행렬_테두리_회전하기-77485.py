# 💡 행렬 테두리 회전하기(Lv2) 📚 https://school.programmers.co.kr/learn/courses/30/lessons/77485
"""
행렬의 크기와 회전해야 하는 두 좌표가 주어지면,
1. 1씩 증가하는 행렬을 생성합니다.
2. 회전해야 할 위치들의 값을 받아옵니다.
3. 행렬을 시계 방향으로 회전시킵니다.
4. 3번 과정에서 최소값을 찾습니다.
"""
"""
시작좌표(x1, y1)와 끝좌표(x2, y2)가 주어지면 사각형이 생기는데, 여기서 중앙을 제외한 테두리 부분을 시계 방향으로 회전
마치 컨베이어 벨트처럼 오른쪽으로 돌면 된다.
다만, 회전하는 과정에서 변수는 일단 값이 1번 변경되면, 이전 값을 기억하지 않는다.
이렇게 값이 사라지면 나머지 작업에서도 똑같이 값이 사라진다.
그래서 사라지는 값을 기억했다가 마지막에 다시 할당하는 과정이 필수적이다.
💡 이떄, 생각을 바꿔 시계 반대방향으로 회전하면?
왼쪽 아래(1) → 오른쪽 아래(2) → 오른쪽 위(3) → 왼쪽 위(4) 순서로 바꾸면, 
맨 처음 숫자 8만 사라져서 해당 값만 기억했다 마지막 들어갈 위치 8에 할당하면 됩니다.
"""
# 📌 (3) 행렬을 시계 방향으로 회전시킵니다. (반시계로 회전시키고, 최소값(맨왼쪽상단) 마지막에 추가)
def rotate(x1, y1, x2, y2, matrix):
    # 시작 지점 (x1, y1)의 값을 first 변수에 저장
    first = matrix[x1][y1] # e.g.1) 8, 15, 25

    # 회전된 영역 내에서 최소값을 저장할 변수를 초기화
    min_value = first

    # 왼쪽 방향으로 회전하면서 값을 이동
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k + 1][y1]
        # 회전된 영역 내에서의 최솟값을 업데이트
        min_value = min(min_value, matrix[k + 1][y1])
        
    # 아래 방향으로 회전하면서 값을 이동
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k + 1]
        min_value = min(min_value, matrix[x2][k + 1])

    # 오른쪽 방향으로 회전하면서 값을 이동
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k - 1][y2]
        min_value = min(min_value, matrix[k - 1][y2])

    # 위 방향으로 회전하면서 값을 이동
    for k in range(y2, y1 + 1, -1):
        matrix[x1][k] = matrix[x1][k - 1]
        min_value = min(min_value, matrix[x1][k - 1])

    matrix[x1][y1 + 1] = first # 처음 위치로 회전된 값을 설정
    return min_value # 회전된 영역 내에서의 최솟값을 반환

def solution(rows, columns, listOfRotation):
    # 📌 (1) 1씩 증가하는 행렬을 생성합니다.
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    # print(matrix) 👇
    # [[1, 2, 3, 4, 5, 6],      [7, 8, 9, 10, 11, 12],    [13, 14, 15, 16, 17, 18], 
    # [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]

    # 📌 (2) 회전해야 할 위치들의 값을 받아옵니다.
    result = []
    for x1, y1, x2, y2 in listOfRotation:
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))

    # 모든 회전이 완료된 최솟값 리스트를 반환
    # return result

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))  # [8, 10, 25]
# 2행2열~5행4열까지 영역의 테두리를 시계방향으로 회전
# 3행3열~6행6열까지 영역의 테두리를 시계방향으로 회전
# 5행1열~6행3열까지 영역의 테두리를 시계방향으로 회전
# 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자를 순서대로 배열에 담아 return

# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))  # [1, 1, 5, 3]


