"""📍 순차탐색(sequential_search)
순차탐색은 리스트 안에 있는 특정한 데이터를 찾기 위해, 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.

보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 주로 사용하는데,
리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 찾을 수 있다는 장점이있다.

그러나, 코딩테스트에서는 시간을 무한정으로 주지 않는 경우가 많기 때문에, 
문제를 잘 보고 사용여부를 판단하면 되겠다.

순차 탐색은 이름처럼 순차로 데이터를 탐색한다는 의미이다.
리스트안에 데이터를 하나씩 방문하면서 내가 찾는 문자열과 동일한지 찾는 원리인데,
후에 count() 메소드를 이용할때에도 내부에서는 순차탐색이 사용된다.
"""


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))

"""
순차 탐색은 데이터 정렬여부와 상관없이 가장 앞에있는 원소부터 하나씩 확인해야 하는점이 특징이다.
따라서, 데이터의 개수가 N개 일때, 
최대 N번의 비교연산이 수행되므로 최악의 경우의 시간복잡도는 O(N)이 되겠다.
"""
