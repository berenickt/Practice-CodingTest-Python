# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181895
"""
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며,
각 구간은 닫힌 구간입니다. 
닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.

이때 배열 arr의 첫 번째 구간에 해당하는 배열과 
두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return

입력#1
arr        : [1, 2, 3, 4, 5]
intervals  : [[1, 3], [0, 4]]

출력#1
[2, 3, 4, 1, 2, 3, 4, 5]

📌 cf. extend
list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.
"""


def solution(arr, intervals):
    l = []
    for idx in intervals:
        l.extend(arr[idx[0] : idx[1] + 1])
    return l


print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))


################################
def solution2(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1 : e1 + 1] + arr[s2 : e2 + 1]
