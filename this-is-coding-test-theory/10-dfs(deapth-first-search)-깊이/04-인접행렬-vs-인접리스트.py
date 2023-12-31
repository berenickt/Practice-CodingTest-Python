""" 인접행렬 vs 인접 리스트 
두 방식의 차이는 어떤점이 있을까?
메모리측면, 속도측면 에서 살펴보자.

메모리측면
- 인접 행렬(Adjacency Matrix) : 
    모든 관계를 저장하므로 노드 개수가 많을 수록 불필요한 메모리가 소요된다.
- 인접 리스트(Adjacency List)  : 
    연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.


속도측면
- 인접 행렬(Adjacency Matrix): 
    모든 경우의 수가 제시되어 있으므로 인접리스트보다 빠르다.
- 인접 리스트(Adjacency List): 
    인접행렬방식에 비해 정보를 얻는 속도가 느리다.
    인접리스트방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문이다.
"""
