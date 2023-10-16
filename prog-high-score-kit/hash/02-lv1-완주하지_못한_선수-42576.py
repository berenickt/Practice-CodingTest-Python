# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return

입력 #1
participant : ["leo", "kiki", "eden"]
completion  : ["eden", "kiki"]

출력 #1
"leo"
"""


def solution(participant, completion):
    # 참가자와 완주자 명단 정렬
    part = sorted(participant)
    comp = sorted(completion)
    # 우선, 정렬 기준 앞에서 값이 다 같을수 있기 때문에 마지막 값으로 할당
    answer = part[-1]

    # 같은 위치, 같은 값이면 패스하고 같은 위치 다른 값이면 그 요소를 정답 변수에 할당
    for i in range(len(comp)):
        if part[i] == comp[i]:
            pass
        elif part[i] != comp[i]:
            answer = part[i]
            break

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))


#################################
"""
완주 못한 사람은 한 명이라는 전제가 있으니까 
그 한 명만 찾아내면 됨
"""


def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
