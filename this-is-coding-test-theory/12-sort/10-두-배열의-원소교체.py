"""
동빈이는 두 개의 배열 A와 B를 가지고 있다.
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.

동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데,
바꿔치기 연산이란 배열 A에 있는 원소 하나와 
배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.

동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 
여러분은 동빈이를 도와야한다.

N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 
최대 K 번의 바꿔치기 연산을 수행하여 
만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

e.g. N = 5, K = 3이고, 배열 A와 B가 다음과 같다고 하자.
배열 A = [1, 2, 5, 4, 3]
배열 B = [5, 5, 6, 6, 5]

이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다.
연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기
연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기
연산 3) 배열 A의 원소 '3'과 배열 B의 원소 '5'를 바꾸기

세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다.
배열 A = [6, 6, 5, 4, 5]
배열 B = [3, 5, 1, 2, 5]
이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다.

cf.
첫 번째 줄에 N, K 가 공백으로 구분되어 입력된다. (1 <= N <= 100,000, 0 <= K <= N)
두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 
모든 원소는 10,000,000보다 작은 자연수이다.
세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 
모든 원소는 10,000,000보다 작은 자연수입니다.

input #1  N = 원소의 개수, K = 바꿀 수 있는 횟수
5 3
1 2 5 4 3
5 5 6 6 5

output #1 배열 A의 모든 원소의 합의 최대값
26

Tip
배열 A를 오름차순 정렬하고, 배열 B를 내림차순 정렬한 뒤
배열 A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때 교체를 수행하며,
이 과정을 K번 반복하면 됩니다.

배열A를 오름차, 배열B를 내림차로 정렬하고,
가장 첫 원소부터 비교하면서 A의 원소가 B원소보다 작으면 교체를 수행
"""
n, k = map(int, input().split())  # N과 K를 입력 받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split()))  # 배열 B의 모든 원소를 입력받기

a.sort()  # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))  # 배열 A의 모든 원소의 합을 출력
