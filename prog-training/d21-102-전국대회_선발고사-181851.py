# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181851
"""
0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다.
등수가 높은 3명을 선발해야 하지만,
개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 
참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

각 학생들의 선발 고사 등수를 담은 정수 배열 rank와
전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어짐
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때, 
10000 x a + 100 x b + c를 return

입력#1
rank       : [3, 7, 2, 5, 4, 6, 1]
attendance : [False, True, True, True, True, False, False]

출력#1
20403

📌 cf. index() : 해당 요소의 인덱스 반환
"""


def solution(rank, attendance):
    student = [rank[idx] for idx, el in enumerate(attendance) if el == True]
    stu_num = [rank.index(i) for i in sorted(student)]  # e.g.1) [2, 4, 5, 7]
    a, b, c = stu_num[0], stu_num[1], stu_num[2]
    return 10000 * a + 100 * b + c


print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))
