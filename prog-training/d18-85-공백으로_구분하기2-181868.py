# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181868
"""
단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return

입력#1
" i    love  you"

출력#1
["i", "love", "you"]

📌 cf. strip() : 문자열 및  공백 제거
"""


def solution(my_string):
    print(my_string.strip())
    return my_string.strip().split()


print(solution(" i    love  you"))
