"""📍 quick_sort(퀵 정렬)
퀵 정렬은 지금까지 배운 정렬 알고리즘 중 가장 많이 사용되는 알고리즘이다.
퀵 정렬과 병합정렬은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이기도 하다.

퀵 정렬은 다음과 같이 동작한다.

1. 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식

퀵 정렬에서는 대표적으로 피벗(pivot)이 사용된다.
큰 숫자와 작은 숫자를 교환할 때, 
교환하기 위한 기준을 바로 피벗(pivot)이라고 표현한다.

피벗을 설정하는 자리는 많지만, 가장 왼쪽을 기준으로 잡자.
자세한 동작원리는 나동빈의 강의에서 살펴보자.
@see https://www.youtube.com/watch?v=EuJSDghD4z8

코드는 교재에 나온 2가지 모두 사용해봤는데,
뭔가 느낌이 딱 와닿지 않아서 나에게 이해가 잘되는 코드를 하나 찾았다.

array는 사용할때마다 랜덤한 값을 주고싶어 random 라이브러리를 호출했다.
"""

"""
1번째 방법(널리 사용되는 코드)
"""
import random

array = random.sample(range(100), 10)
print(array)


def quick_sort(array, start, end):
    if len(array) <= 1:
        return array

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left = left + 1
        while right > start and array[right] >= array[pivot]:
            right = right - 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)

print(array)
# 👉🏽
# random: [92, 5, 28, 75, 24, 32, 73, 53, 22, 46]
# quick_sort: [5, 22, 24, 28, 32, 46, 53, 73, 75, 92]

"""
2번째 방법(개인적으로 이해가 잘 되는 코드)
"""
import random

array = random.sample(range(100), 10)
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left, right = list(), list()

    for idx in range(1, len(array)):
        if array[idx] < pivot:
            left.append(array[idx])
        else:
            right.append(array[idx])

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(array))
# 👉🏽
# [71, 76, 32, 87, 68, 58, 96, 51, 97, 30]
# [30, 32, 51, 58, 68, 71, 76, 87, 96, 97]

"""
3번째 방법(list Comprehension 사용한 코드)
"""
import random

array = random.sample(range(100), 10)
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(array))
# 👉🏽
# [59, 86, 13, 24, 85, 93, 92, 17, 90, 28]
# [13, 17, 24, 28, 59, 85, 86, 90, 92, 93]

"""
퀵 정렬의 평균 시간복잡도는 O(NlogN)이다.
왜 O(NlogN)인지 궁금하다면 여기를 참고하자.
@see https://codingdog.tistory.com/entry/%ED%80%B5-%EC%A0%95%EB%A0%AC-%ED%8F%89%EA%B7%A0-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EC%99%9C-Onlogn%EC%9D%BC%EA%B9%8C

다만, 여기서 중요한 점은 퀵 정렬의 시간복잡도가 최악인 경우는 O(N^2)이다.
이는 어제 배운 삽입 정렬, 선택 정렬의 시간복잡도와 동일하다.
데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다. 
하지만, 리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작한다.

앞서 다룬 삽입 정렬은 이미 데이터가 정렬되어있을 경우에는 매우 빠르게 동작한다고 배웠는데,
퀵 정렬은 그와 반대된다는 점을 기억하자.
"""
