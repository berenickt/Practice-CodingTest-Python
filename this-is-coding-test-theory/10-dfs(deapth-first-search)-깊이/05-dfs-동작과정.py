"""
DFS의 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
    방문처리(visited)란 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는것을 의미한다. 
    방문처리를 함으로써 각 노드를 한 번씩만 처리 할 수 있다.

깊이 우선 탐색 알고리즘인 DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단하다.
탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다.

실제로 스택을 쓰지 않고,
재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있다.
"""


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 방문한 노드 출력
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 만약 연결된 노드가 아직 방문하지 않은 노드라면, 그 노드에 대해 dfs 함수를 재귀적으로 호출
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
"""
여기서 각 숫자는 노드를 나타내며, 
노드들 사이의 선은 노드들이 서로 연결되어 있음을 나타냅니다. 

e.g. 노드 1은 노드 2, 3, 8과 연결되어 있습니다. 
이는 graph[1] = [2, 3, 8]으로 표현되어 있습니다

e.g., 노드 2은 노드 1, 7과 연결되어 있습니다.  graph[2] = [1, 7]
e.g., 노드 3은 노드 1, 4, 5과 연결되어 있습니다.  graph[3] = [1, 4, 5]
...
"""


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
# 👉🏽 1 2 7 6 8 3 4 5

"""
아래는 코드가 실행되는 동안 visited가 어떻게 변하는지에 대한 설명입니다.

1. 초기 상태:
- graph: [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
- visited: [F, F, F, F, F, F, F, F, F]

2. dfs(graph, 1, visited) 호출 후:
- visited: [F, T, F, F, F, F, F, F, F]
- 출력: 1

3. dfs(graph, 2, visited) 호출 후:
- visited: [F, T, T, F, F, F, F, F, F]
- 출력: 1 2

4. dfs(graph, 7, visited) 호출 후:
- visited: [F, T, T, F, F, F, F, T, F]
- 출력: 1 2 7

5. dfs(graph, 6, visited) 호출 후:
- visited: [F, T, T, F, F, F, T, T, F]
- 출력: 1 2 7 6

6. dfs(graph, 8, visited) 호출 후:
- visited: [F, T, T, F, F, F, T, T, T]
- 출력: 1 2 7 6 8

7. dfs(graph, 3, visited) 호출 후:
- visited: [F, T, T, T, F, F, T, T, T]
- 출력: 1 2 7 6 8 3

8. dfs(graph, 4, visited) 호출 후:
- visited: [F, T, T, T, T, F, T, T, T]
- 출력: 1 2 7 6 8 3 4

9. dfs(graph, 5, visited) 호출 후:
- visited: [F, T, T, T, T, T, T, T, T]
- 출력: 1 2 7 6 8 3 4 5

이렇게 모든 노드를 방문하게 되면 visited 리스트는 모두 T가 되고, 출력은 1 2 7 6 8 3 4 5가 됩니다.
"""
