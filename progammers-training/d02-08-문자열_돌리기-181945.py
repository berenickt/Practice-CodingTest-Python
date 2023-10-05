# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181945
"""
문자열 str이 주어집니다. 
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드

입력 #1
abcde

출력 #1
a
b
c
d
e
"""

# 방법 1
print("\n".join(input()))

# 방법 2
for s in input():
    print(s)
