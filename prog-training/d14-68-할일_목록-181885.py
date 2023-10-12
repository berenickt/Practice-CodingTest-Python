# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181885
"""
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 
각각의 일을 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return

입력#1
todo_list : ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished  : [True, False, True, False]

출력#1
["practiceguitar", "studygraph"]
"""


def solution(todo_list, finished):
    return [td for td, f in zip(todo_list, finished) if not f]


print(
    solution(
        ["problemsolving", "practiceguitar", "swim", "studygraph"],
        [True, False, True, False],
    )
)
