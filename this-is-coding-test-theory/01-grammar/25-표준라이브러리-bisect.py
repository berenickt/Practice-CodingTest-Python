""" bisect() 
정렬된 배열에서 특정한 원소를 찾을 때 주로 사용하고 배열 위치를 반환한다.

bisect_left
bisect_right 

1. 해당 값이 리스트에 있을 때
bisect_left  : 해당 index 반환
bisect_right : 해당 index+1 반환

2. 해당 값이 리스트에 없을 때
bisect_left  : 리스트 오름차순에 들어갈 index 반환
bisect_right : 리스트 오름차순에 들어갈 index 반환
"""
from bisect import bisect_left, bisect_right

# 특정한 원소의 배열 위치
a = [1, 2, 4, 4, 8]
print(bisect_left(a, 2))  # 👉🏽 1 ===> 왼쪽부터 첫 2의 위치 인덱스
print(bisect_right(a, 4))  # 👉🏽 4 ===> 오른쪽부터 첫 4의 위치 인덱스+1


# 값이 특정 범위에 속하는 원소의 개수
def count_by_range(a, lValue, rValue):
    right_idx = bisect_right(a, rValue)
    left_idx = bisect_left(a, lValue)
    return right_idx - left_idx


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))  # 👉🏽 2 ===> 8(r) - 6(l)
print(count_by_range(a, 3, 3))  # 👉🏽 4 ===> 6(r) - 2(l)

# 0 ~ 9 범위의 데이터 개수
print(count_by_range(a, 1, 9))  # 👉🏽 10 ===> 10(r) - 0(l)
