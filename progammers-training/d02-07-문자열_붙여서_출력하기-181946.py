# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181946
"""
두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다. 
입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성
"""

# 방법1
print(input().strip().replace(" ", ""))

# 방법2
str1, str2 = input().strip().split(" ")
print(f"{str1}{str2}")
