"""
못생긴 수란 오직 2, 3, 5 만을 소인수로 가지는 수를 의미한다.
다시 말해 오직 2, 3, 5를 약수로 가지는 합성수를 의미한다.
12의 약수인 1, 2, 3, 4, 6, 12 중에서 2와 3이 소인수이다.
1은 못생긴 수라고 가정한다.

따라서 못생긴 수들은 {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... } 순으로 이어지게 된다.
이때, n번째 못생긴 수를 찾는 프로그램을 작성해라.
e.g. 11번째 못생긴 수는 15

input #1
10

output #1
12

Tip
2의 배수 변수, 3의 배수 변수, 5의 배수 변수에 대하여 
각각 '가장 작은 못생긴 수'부터 오름차순으로 하나씩 확인하면서,
각 배수를 곱한 값도 '못생긴 수'가 될 수 있도록 처리한다.

e.g. 먼저 못생긴 수로 1이 있다고 해보자.
이때 각각 2의 배수, 3의 배수, 5의 배수를 구하면 다음과 같다.
2의 배수 : 1 x 2 = 2
3의 배수 : 1 x 3 = 3
5의 배수 : 1 x 5 = 5

이로써 우리는 새롭게 2, 3, 5 또한 못생긴 수에 해당한다는 것을 알 수 있다.
따라서, 전체 못생긴 수는 {1, 2, 3, 5}가 된다.

첫 번째로 못생긴 수인 1에 이어서 그 다음으로 못생긴 수는 2가 된다.
이때 각각 2의 배수, 3의 배수, 5의 배수를 구하면 다음과 같다.
2의 배수 : 2 x 2 = 4
3의 배수 : 2 x 3 = 6
5의 배수 : 2 x 5 = 10
이로써 우리는 4, 6, 10이 못생긴 수에 해당한다는 것을 알 수 있다.
따라서, 전체 못생긴 수는 {1, 2, 3, 4, 6, 10}이 된다.

이렇게 못생긴 수들을 작은 수부터 차례대로 확인하면서,
각 못생긴 수에 대해서 2의 배수 3의 배수, 5의 배수를 고려하며 풀면 된다.
"""
n = int(input())

ugly = [0] * n  # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1  # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0

# 처음에 곱셈 값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])
