# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""
구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

사람들의 몸무게를 담은 배열 people과
구명보트의 무게 제한 limit가 매개변수로 주어질 때,
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return

입력 #1
people : [70, 50, 80, 50]
limit  : 100

출력 #1
3

cf.
lef	rig	people[lef]	people[rig]	people[lef] + people[rig]	boatCnt
  0	  3	        50	        80	                     130        0
  1	  3	        50	        70	                     120        1
  2	  3	        50	        50	                     100        2
"""


def solution(people, limit):
    boatCnt = 0
    people.sort()
    L_inx = 0
    R_inx = len(people) - 1
    MAX_boatCnt = len(people)

    while L_inx < R_inx:
        if people[L_inx] + people[R_inx] <= limit:
            L_inx += 1
            boatCnt += 1
        R_inx -= 1
    return MAX_boatCnt - boatCnt


print(solution([70, 50, 80, 50], 100))
