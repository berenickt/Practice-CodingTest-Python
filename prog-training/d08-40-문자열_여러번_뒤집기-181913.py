# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181913
"""
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return

입력#1
"rermgorpsam"
[[2, 3], [0, 7], [5, 9], [6, 10]]

출력#1
"programmers"

입력 설명#1
        "rermgorpsam"
[2, 3]	"remrgorpsam"
[0, 7]	"progrmersam"
[5, 9]	"prograsremm"
[6, 10]	"programmers"
"""


def solution(my_string, queries):
    answer = list(my_string)
    for q in queries:
        # q[0]부터 q[1] + 1까지의 인덱스만큼 슬라이싱
        answer[q[0] : q[1] + 1] = answer[q[0] : q[1] + 1][::-1]
    return "".join(answer)


print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))
