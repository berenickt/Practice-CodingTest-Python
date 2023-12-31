"""
시뮬레이션 및 완전 탐색문제에서 
2차원 공간에서의 방향 벡터가 자주 활용됨
"""

"""반시계 방향으로 움직임
- 동 (East)  : x축으로 0, y축으로 1 이동 
- 북 (North) : x축으로 -1, y축으로 0 이동 
- 서 (West)  : x축으로 0, y축으로 -1 이동 
- 남 (South) : x축으로 1, y축으로 0 이동 

이 순서는 일반적으로 시계 반대 방향으로 이동하는 것을 나타냅니다.
이는 많은 문제에서 사용되는 표준적인 방향 순서입니다.

여기서 x축과 y축은 일반적인 수학적 좌표계와는 다르게, 
프로그래밍에서의 배열 인덱스를 기준으로 합니다.

일반적으로 프로그래밍에서 2차원 배열은 왼쪽 상단을 (0,0)으로 시작하며, 
x축은 아래로, y축은 오른쪽으로 증가합니다. 
따라서, x축으로 -1 이동은 배열의 위쪽으로 이동하는 것을 의미하므로 
'북(North)'으로 표현한 것
"""
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = x + dy[i]
    print(nx, ny)

"""출력결과 (위치(2,2) 기준 반시계 방향으로 동북서남으로 이동한 결과)
2 3
1 2
2 1
3 2
"""
