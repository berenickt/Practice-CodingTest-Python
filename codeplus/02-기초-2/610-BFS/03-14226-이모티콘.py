# 💡 이모티콘 📚 https://www.acmicpc.net/problem/14226
from collections import deque

n = int(input())  # 입력으로 정수 n을 받음
dist = [[-1] * (n + 1) for _ in range(n + 1)]  # 거리 정보를 저장할 2차원 배열 dist 초기화
q = deque()
q.append((1, 0))  # 큐에 (현재 화면에 있는 이모티콘 수, 클립보드에 있는 이모티콘 수)를 저장하며 시작
dist[1][0] = 0  # 시작 지점의 거리를 0으로 초기화

while q:
    s, c = q.popleft()  # 현재 화면과 클립보드의 이모티콘 수를 가져옴
    if dist[s][s] == -1:  # 화면의 이모티콘을 모두 복사하여 클립보드에 저장
        dist[s][s] = dist[s][c] + 1  # 이전 상태에서 1회 추가하는 것이므로 거리 1 증가
        q.append((s, s))  # 다음 상태를 큐에 추가
    if s + c <= n and dist[s + c][c] == -1:  # 클립보드에 있는 이모티콘을 화면에 붙여넣기
        dist[s + c][c] = dist[s][c] + 1  # 이전 상태에서 1회 추가하는 것이므로 거리 1 증가
        q.append((s + c, c))  # 다음 상태를 큐에 추가
    if s - 1 >= 0 and dist[s - 1][c] == -1:  # 화면에 있는 이모티콘 중 하나 삭제
        dist[s - 1][c] = dist[s][c] + 1  # 이전 상태에서 1회 삭제하는 것이므로 거리 1 증가
        q.append((s - 1, c))  # 다음 상태를 큐에 추가

ans = -1

for i in range(n + 1):  # 최종 화면에 n개의 이모티콘을 출력하는데 걸리는 최소 거리를 찾음
    if dist[n][i] != -1:  # 목표 지점까지 도달 가능한 경우
        if ans == -1 or ans > dist[n][i]:  # 최소 거리를 갱신
            ans = dist[n][i]

print(ans)  # 최소 거리를 출력
