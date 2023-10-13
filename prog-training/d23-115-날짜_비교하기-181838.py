# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181838
"""
정수 배열 date1과 date2가 주어집니다.
두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다.
각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.

만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return

입력#1
date1 : [2021, 12, 28]
date2 : [2021, 12, 29]

출력#1
1
"""


def solution(date1, date2):
    for d1, d2 in zip(date1, date2):
        if d1 < d2:
            return 1
        elif d1 > d2:
            return 0
    return 0


print(solution([2021, 12, 28], [2021, 12, 29]))


#########################cf. int(True)는 1, 리스트간 부등호 사용가능
def solution2(date1, date2):
    return int(date1 < date2)
