# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181884
"""
정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간
이때까지 더했던 원소들의 합을 return

입력#1
numbers : [34, 5, 71, 29, 100, 34]
n       : 123

출력#1
139
"""


def solution(numbers, n):
    result = 0
    for num in numbers:
        result += num
        if result > n:
            return result


print(solution([34, 5, 71, 29, 100, 34], 123))
