# 💡 단지번호붙이기 📚 https://www.acmicpc.net/problem/2667
from collections import deque, Counter
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


n = int(input())  # 입력: 행과 열의 크기 n
a = [list(map(int, list(input()))) for _ in range(n)]  # 입력: 2차원 배열 a
group = [[0] * n for _ in range(n)]  # 그룹 정보를 저장하는 2차원 배열 초기화
cnt = 0  # 그룹의 개수를 저장하는 변수 초기화

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1  # 그룹 개수 증가
            bfs(i, j, cnt)  # BFS로 그룹 결정

ans = reduce(lambda x, y: x + y, group)  # 모든 그룹 정보를 하나의 리스트로 합치기
ans = [x for x in ans if x > 0]  # 0인 원소는 제외하고 리스트로 만들기
ans = sorted(list(Counter(ans).values()))  # 그룹 크기를 세서 정렬하기

print(cnt)  # 그룹의 개수 출력
print("\n".join(map(str, ans)))  # 그룹 크기 출력
