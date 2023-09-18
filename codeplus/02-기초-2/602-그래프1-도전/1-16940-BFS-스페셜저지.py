# 💡 BFS 스페셜 저지 📚 https://www.acmicpc.net/problem/16940
from collections import deque

n = int(input())  # 노드 개수 입력
a = [[] for _ in range(n)]  # 빈 인접 리스트 초기화

for _ in range(n - 1):
    u, v = map(int, input().split())  # 간선 정보 입력
    u -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    v -= 1  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경
    a[u].append(v)  # 양방향 간선 추가
    a[v].append(u)  # 양방향 간선 추가

order = list(map(int, input().split()))  # 방문 순서 입력
order = [x - 1 for x in order]  # 1부터 시작하는 인덱스를 0부터 시작하는 인덱스로 변경

check = [False] * n  # 노드 방문 여부를 저장하는 배열 초기화
parent = [-1] * n  # 각 노드의 부모 노드를 저장하는 배열 초기화
q = deque()  # 큐 초기화

q.append(0)  # 루트 노드를 큐에 추가
check[0] = True  # 루트 노드 방문 처리
m = 1  # 방문 순서 리스트의 인덱스를 나타내는 변수 초기화

for i in range(n):
    if not q:  # 큐가 비어있는 경우
        print(0)  # 순서에 맞게 방문하지 못한 경우 출력하고 종료
        exit()

    x = q.popleft()  # 큐에서 노드를 꺼냄
    if x != order[i]:  # 현재 노드와 순서가 일치하지 않는 경우
        print(0)  # 순서에 맞게 방문하지 못한 경우 출력하고 종료
        exit()

    cnt = 0  # 현재 노드의 자식 노드 개수를 저장하는 변수 초기화
    for y in a[x]:
        if check[y] == False:  # 아직 방문하지 않은 자식 노드인 경우
            parent[y] = x  # 부모 노드 정보 업데이트
            cnt += 1  # 자식 노드 개수 증가

    for j in range(cnt):
        if m + j >= n or parent[order[m + j]] != x:  # 순서에 맞게 방문하지 못한 경우
            print(0)  # 순서에 맞게 방문하지 못한 경우 출력하고 종료
            exit()
        q.append(order[m + j])  # 다음 방문할 노드를 큐에 추가
        check[order[m + j]] = True  # 노드 방문 처리
    m += cnt  # 방문 순서 리스트의 인덱스 업데이트

print(1)  # 순서에 맞게 방문한 경우 1 출력
