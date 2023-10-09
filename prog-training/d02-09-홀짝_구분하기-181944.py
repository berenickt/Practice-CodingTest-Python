# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181944
"""
자연수 n이 입력으로 주어졌을 때, 
n이 짝수이면 "n is even"을, 
홀수이면 "n is odd"를 출력하는 코드

입력 #1
100

출력 #1
100 is even
"""

a = int(input())

if a % 2 == 1:
    print(f"{a} is odd")
else:
    print(f"{a} is even")
