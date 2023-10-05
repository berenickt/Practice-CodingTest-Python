# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181927
"""
정수 리스트 num_list가 주어질 때, 
마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 
마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return

입력#1
[2, 1, 6]

출력#1 
[2, 1, 6, 5]

마지막 원소인 6이 그전 원소인 1보다 크기 때문에 6 - 1인 5를 추가해 return
"""


def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else:
        num_list.append(n1 * 2)
    return num_list
