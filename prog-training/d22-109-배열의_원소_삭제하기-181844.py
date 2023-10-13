# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181844
"""
정수 배열 arr과 delete_list가 있습니다.
arr의 원소 중 delete_list의 원소를 모두 삭제하고, 
남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return

입력#1
arr         : [293, 1000, 395, 678, 94]
delete_list : [94, 777, 104, 1000, 1, 12]

출력#1
[293, 395, 678]
"""


def solution(arr, delete_list):
    return [a for a in arr if a not in delete_list]


print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))


################################
def solution2(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr
