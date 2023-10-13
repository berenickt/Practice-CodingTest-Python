# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181839
"""
1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 
두 주사위를 굴렸을 때 나온 숫자를 
각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

- a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
- a와 b 중 하나만 홀수라면 2 x (a + b) 점을 얻습니다.
- a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.

두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return

입력#1
a : 3
b : 5

출력#1
34
"""


def solution(a, b):
    # 두 수 모두 짝수일 경우
    if a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    # 두 수 모두 홀수일 경우
    elif a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    # 짝수 하나 홀수 하나일 경우
    return 2 * (a + b)


print(solution(3, 5))
