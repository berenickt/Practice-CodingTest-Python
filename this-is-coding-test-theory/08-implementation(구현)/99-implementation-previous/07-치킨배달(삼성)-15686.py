# 📚 https://www.acmicpc.net/problem/15686
"""
크기가 N x N인 도시가 있습니다.
도시는 1 x 1 크기의 칸으로 나누어져 있습니다.
도시의 각 칸은 빈칸, 치킨집, 집 중 하나입니다.

도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미합니다.
r과 c는 1부터 시작합니다.
이 도시에 사는 사람들은 치킨을 매우 좋아합니다. 따라서 사람들은 "치킨 거리"라는 말을 주로 사용합니다.

치킨 거리는 집과 가장 가까운 치킨집 사이의 거리입니다.
즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있습니다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합입니다.
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2| 로 구합니다.

예를 들어, 아래와 같은 지도를 갖는 도시를 살펴봅시다.
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2

0은 빈 칸, 1은 집, 2는 치킨집입니다.

(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 
|2-5| + |1-5| = 7입니다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2입니다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 
|5-5| + |4-5| = 1입니다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1입니다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈입니다.
프랜차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 합니다.
오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 사실을 알아냈습니다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 합니다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하세요

input #1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

output #1
5
"""
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))  # 일반 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))


# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
