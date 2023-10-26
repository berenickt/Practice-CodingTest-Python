# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""
전체 학생의 수 n, 
체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return

입력 #1
n       : 5
lost    : [2, 4]
reserve : [1, 3, 5]

출력 #1
5
"""


def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()

    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
