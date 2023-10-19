# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return

입력 #1
[1, 2, 3, 2, 3]

출력 #1
[4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 
    따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
"""

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


print(solution([1, 2, 3, 2, 3]))


#####################################
def solution2(prices):
    length = len(prices)

    # answer을 max값으로 초기화, [4, 3, 2, 1, 0]
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]

    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
