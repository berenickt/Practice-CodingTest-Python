# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181903
"""
두 정수 q, r과 문자열 code가 주어질 때, 
code의 각 인덱스를 q로 나누었을 때 
나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어붙인 문자열을 return

입력#1
q         : 3
r         : 1
code      : "qjnwezgrpirldywt"

출력#1
"jerry"
"""


def solution(q, r, code):
    # 문자열과 문자열별 인덱스/q의 나머지를 튜플로 저장
    l = [(c, i % q) for i, c in enumerate(code)]
    answer = ""

    # 튜플 속 인덱스/q의 나머지값이 r인 문자열만 가져옴
    for s in l:
        if s[1] == r:
            answer += s[0]
    return answer


print(solution(3, 1, "qjnwezgrpirldywt"))


###############################
def solution2(q, r, code):
    return code[r::q]
