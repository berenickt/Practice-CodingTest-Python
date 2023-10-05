# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181930
"""
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 
세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
(생략)

세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return
"""


def solution1(a, b, c):
    check = len(set([a, b, c]))
    if check == 1:
        return 3 * a * 3 * (a**2) * 3 * (a**3)
    elif check == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


def solution2(a, b, c):
    answer = a + b + c
    if a == b or b == c or a == c:
        answer *= a**2 + b**2 + c**2
    if a == b == c:
        answer *= a**3 + b**3 + c**3
    return answer
