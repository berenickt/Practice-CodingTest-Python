"""📍 이진탐색(binary_search)
이진탐색은 배열 내부의 데이터가 정렬되어야만 사용할 수 있는 알고리즘이다.

이진 탐색은 퀵 정렬(quick_sort)과 비슷하게 
탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.

이진 탐색은 위치를 나타내는 변수 3개(시작점, 끝점, 중간점)를 사용해서 함수를 만든다.
그래서, 찾으려는 데이터와 중간점(Middle)위치에 있는 데이터를 반복적으로 비교해서 
원하는 데이터를 찾는게이진 탐색 과정이다.

자세한 설명내용은 유튜브 강의를 참고.
@see https://www.youtube.com/watch?v=94RC-DsGMLo&t=763s

이진탐색은 데이터를 한번 확인할때마다, 
원소의 개수가 절반씩 감소한다는 점에서 시간 복잡도가 O(logN)이다.

이진탐색을 구현하는 방법에는 2가지(재귀함수, 반복문)가 있다
"""


# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

"""input #1
10 7
1 3 5 7 9 11 13 15 17 19
결과 : 4
"""

"""input #1
10 7
1 3 5 6 9 11 13 15 17 19
결과 : 원소가 존재하지 않습니다.
"""
