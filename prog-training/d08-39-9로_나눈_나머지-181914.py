# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181914
"""
음이 아닌 정수를 9로 나눈 나머지는 
그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 
이 정수를 9로 나눈 나머지를 return

입력#1
"123"

출력#1
6
"""


def solution(number):
    num_add = sum([int(s) for s in number])
    return num_add % 9


print(solution("123"))
