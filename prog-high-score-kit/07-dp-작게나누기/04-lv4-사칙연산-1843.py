# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/1843
"""
사칙연산에서 더하기(+)는 결합법칙이 성립하지만, 
빼기(-)는 결합법칙이 성립하지 않습니다.

e.g. 식 1 - 5 - 3은 연산 순서에 따라 다음과 같이 다른 결과를 가집니다.
((1 - 5) - 3) = -7
(1 - (5 - 3)) = -1

위 예시와 같이 뺄셈은 연산 순서에 따라 그 결과가 바뀔 수 있습니다.

e.g. 식 1 - 3 + 5 - 8은 연산 순서에 따라 다음과 같이 5가지 결과가 나옵니다.
(((1 - 3) + 5) - 8) = -5
((1 - (3 + 5)) - 8) = -15
(1 - ((3 + 5) - 8)) = 1
(1 - (3 + (5 - 8))) = 1
((1 - 3) + (5 - 8)) = -5
위와 같이 서로 다른 연산 순서의 계산 결과는 [-15, -5, -5, 1, 1]이 되며,
이중 최댓값은 1입니다.

문자열 형태의 숫자와, 더하기 기호("+"), 뺄셈 기호("-")가 들어있는 배열 arr가 
매개변수로 주어질 때,
서로 다른 연산순서의 계산 결과 중 최댓값을 return

입력 #1
["1", "-", "3", "+", "5", "-", "8"]

출력 #1
1
"""


def solution(arr):
    minmax = [0, 0]
    sum_value = 0

    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == "+":
            continue
        elif arr[idx] == "-":
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value + tempmin)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx + 1])
            minmax[1] = max(
                -(sum_value + tempmin), -minus_v + (sum_value - minus_v) + tempmax
            )
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
    minmax[1] += sum_value
    return minmax[1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
