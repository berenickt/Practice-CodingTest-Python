# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181947
"""두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드
a + b = c
"""
a, b = map(int, input().strip().split(" "))
print(f"{a} + {b} = {a + b}")
