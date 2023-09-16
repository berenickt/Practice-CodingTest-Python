# 💡 트리의 높이와 너비 📚 https://www.acmicpc.net/problem/2250
def inorder(node, level):
    global dist
    if n_list[node][0] != -1:
        inorder(n_list[node][0], level + 1)
    distance[level].append(dist)
    dist += 1
    if n_list[node][1] != -1:
        inorder(n_list[node][1], level + 1)


n = int(input())  # 노드 개수 입력
n_list = [[0, 0] for _ in range(n + 1)]  # 노드 정보를 저장할 리스트 초기화
distance = [[] for _ in range(n + 1)]  # 각 레벨별 노드 거리 정보를 저장할 리스트 초기화
r_list = [0 for _ in range(n + 1)]  # 노드의 오른쪽 자식 개수를 저장할 리스트 초기화
dist = 1  # 노드 거리 초기화

# 노드 정보 입력 및 처리
for _ in range(n):
    parent, l, r = map(int, input().split())
    n_list[parent][0] = l
    n_list[parent][1] = r
    if l != -1:
        r_list[l] += 1
    if r != -1:
        r_list[r] += 1

for i in range(1, n + 1):
    if r_list[i] == 0:
        root = i  # 루트 노드 찾기

inorder(root, 1)  # 중위 순회 수행

max_dist = 0  # 최대 거리 초기화
l = 1  # 최대 거리가 나타나는 레벨 초기화

for i in range(1, n + 1):
    if distance[i]:
        d = max(distance[i]) - min(distance[i]) + 1  # 현재 레벨의 노드 거리 범위 계산
        if max_dist < d:
            l = i  # 최대 거리가 나타나는 레벨 갱신
            max_dist = d  # 최대 거리 갱신

print(l, max_dist)  # 결과 출력
