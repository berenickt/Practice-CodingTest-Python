"""삽입 정렬(insertion_sort)
선택 정렬은 문제 풀이에 사용하기에는 느린편인다.

삽입 정렬(insertion_sort)은 특정한 데이터를 적절한 위치에서 삽입하는 정렬이다.
더불어 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에,
그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
즉, 데이터가 거의 정렬되어 있을 떄 효율적이다.

삽입 정렬은 두 번째 데이터부터 시작한다.
왜냐하면 첫 번째 데이터는 그 자체로 정렬되어있다고 판단하기 때문이다.
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
# 👉🏽 [0, 1, 2, 3, 4, 6, 7, 8, 9]

"""
여기서 range의 세번째 매개 변수를 넣었는데, 
range의 매개 변수는 3개(start, end, step)다. 

세 번째 매개 변수인 step에 -1이 들어가면, 
start 인덱스부터 시작해 end+1 인덱스까지 1씩 감소한다.
앞의 코드에서는 j 변수가 i부터 1까지 1씩 감소한다.
"""

"""💡 시간복잡도
선택정렬은 N-1번 만큼 가장 작은 수를 찾아 맨 앞으로 보내야 한다.
또한, 매번 가장 작은 수를 찾기 위해서 비교 연산이 필요하다.

구현 방식에 따라 사소한 오차는 있을 수 있지만,
앞쪽의 순서대로 구현했을 경우 연산 횟수는 N + (N-1) + (N-2) + ... + 2로 볼 수 있다.

따라서, 근사치 N x (N + 1) / 2번의 연산을 수행한다고 했을 때,
가장 큰 수를 꺼내면 시간복잡도는 O(N^2)이 된다.

선택정렬은 정렬해야 할 데이터의 개수가 10,000개 이상이면, 
정렬 속도가 급격히 느려지므로 10,000개 이하일때 가급적 사용하도록 하자.
"""
