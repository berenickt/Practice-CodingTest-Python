# 💡 단지번호붙이기 📚 https://www.acmicpc.net/problem/2667
from collections import deque, Counter
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 깊이 우선 탐색 (DFS) 함수 정의
def dfs(x, y, cnt):
    group[x][y] = cnt  # 현재 위치를 그룹 번호로 표시
    for k in range(4):  # 상하좌우 방향에 대해서
        nx, ny = x + dx[k], y + dy[k]  # 새로운 좌표 계산
        if 0 <= nx < n and 0 <= ny < n:  # 범위 내에 있는지 확인
            if a[nx][ny] == 1 and group[nx][ny] == 0:  # 육지이고 아직 그룹이 지정되지 않았다면
                dfs(nx, ny, cnt)  # 해당 위치를 같은 그룹으로 설정


n = int(input())  # 입력: 행과 열의 크기 n
a = [list(map(int, list(input()))) for _ in range(n)]  # 입력: 2차원 배열 a
group = [[0] * n for _ in range(n)]  # 그룹 정보를 저장하는 2차원 배열 초기화
cnt = 0  # 그룹의 개수를 저장하는 변수 초기화

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:  # 육지이고 아직 그룹이 지정되지 않았다면
            cnt += 1  # 그룹 개수 증가
            dfs(i, j, cnt)  # DFS로 같은 그룹 결정

ans = reduce(lambda x, y: x + y, group)  # 모든 그룹 정보를 하나의 리스트로 합치기
ans = [x for x in ans if x > 0]  # 0인 원소는 제외하고 리스트로 만들기
ans = sorted(list(Counter(ans).values()))  # 그룹 크기를 세서 정렬하기

print(cnt)  # 그룹의 개수 출력
print("\n".join(map(str, ans)))  # 그룹 크기 출력
