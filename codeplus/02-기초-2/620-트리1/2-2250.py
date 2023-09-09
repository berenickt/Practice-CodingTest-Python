# 💡 트리의 높이와 너비 📚 https://www.acmicpc.net/problem/2250
def inorder(node, level):
    global dist
    if n_list[node][0] != -1:
        inorder(n_list[node][0], level + 1)
    distance[level].append(dist)
    dist += 1
    if n_list[node][1] != -1:
        inorder(n_list[node][1], level + 1)


n = int(input())
n_list = [[0, 0] for _ in range(n + 1)]
distance = [[] for _ in range(n + 1)]
r_list = [0 for _ in range(n + 1)]
dist = 1

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
        root = i

inorder(root, 1)

max_dist = 0
l = 1

for i in range(1, n + 1):
    if distance[i]:
        d = max(distance[i]) - min(distance[i]) + 1
        if max_dist < d:
            l = i
            max_dist = d

print(l, max_dist)
