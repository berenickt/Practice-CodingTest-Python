# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""
n개의 음이 아닌 정수들이 있습니다. 
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만드는 코드

입력 #1
[1, 1, 1, 1, 1], 3

출력 #1
5

입력 설명 #1
[1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
"""


def dfs(numbers, target, depth, leaf):
    global cnt  # 전역변수 선언
    cnt = 0

    # 깊이가 끝까지 닿았으면
    if depth == len(numbers) & leaf == target:
        cnt += 1
        return

    # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
    elif depth == len(numbers):
        return

    # 재귀함수로 구현 (새로운 value 값 세팅)
    dfs(numbers, target, depth + 1, leaf + numbers[depth])
    dfs(numbers, target, depth + 1, leaf - numbers[depth])


def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)
    return cnt
