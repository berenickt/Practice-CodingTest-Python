"""
코딩 테스트에서의 이진 탐색문제는 범위가 큰 상황에서 탐색을 가정하는 문제가 많다.
따라서, 탐색 범위가 20,000,000을 넘어가면 이진 탐색으로 문제에 접근해보길 권한다.

처리해야 할 데이터의 개수나 값이 10,000,000 이상으로 넘어가면,
이진탐색과 같이 시간 복잡도가 O(logN)의 속도를 내야 하는 알고리즘을 떠올려야 
문제를 풀 수 있는 경우가 많다는 점도 기억하자!
"""

"""bisect_range(이진탐색 라이브러리)
bisect_left(a,x)  : 정렬된 순서를 유지하면서 배열 a에 x를 삽입 할 가장 왼쪽 인덱스를 반환
bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입 할 가장 오른쪽 인덱스를 반환
"""
# 값이 특정 범위에 속하는 데이터의 개수 구하기
from bisect import bisect_left, bisect_right


def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_range(array, 4, 4))
print(count_range(array, -1, 3))
# 👉🏽 2 6
