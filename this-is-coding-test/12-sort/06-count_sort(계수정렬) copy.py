"""📍 count_sort(계수 정렬)
계수 정렬은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.

모든 데이터가 양의 정수인 상황을 가정했을때, 
데이터의 개수가 N, 
데이터 중 최댓값이 K일때, 
계수 정렬은 최악의 경우에도 수행 시간 O(N+K)를 보장한다.

계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 만 사용할 수 있다.
일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.

계수정렬의 사용 조건은 다음과 같다.

1. 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때
2. 모든 데이터가 양의 정수일 때
3. 동일한 데이터가 섞여있을 때

계수 정렬은 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크면 사용할 수 없는데, 그 이유는 다음과 같다.
계수 정렬을 이용할 때는 모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언해야하기 때문이다.

예를 들어, 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000이라면, 
총 1,000,001개의 데이터가 들어갈 수 있는 리스트를 초기화해야한다.
여기서 1개를 더해주는 이유는 0부터 1,000,000까지는 총 1,000,001개의 수가 존재하기 때문이다.

때문에, 계수정렬은 공간복잡도는 높지만 조건이 맞으면 빠르게 동작한다는 장점을 갖고 있다.
"""
array = [1, 3, 1, 2, 5, 6, 1]

count = [0] * (len(array) + 1)

for i in range(len(array)):
    count[array[i]] = count[array[i]] + 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

# 👉🏽 1 1 1 2 3 5 6

"""count_sort의 시간복잡도
모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 
데이터 중 최대값의 크기를 K라고 할 때,
계수 정렬의 시간 복잡도는 O(N+K)이다.

따라서, 데이터의 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작한다.
사실상 현존하는 정렬 알고리즘 중 기수 정렬(radix_sort)과 더불어 가장 빠르다고 할 수 있다.
"""
