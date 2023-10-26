# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""
문자열 형식으로 숫자 number와
제거할 수의 개수 k가 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때,
만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return

입력 #1
number : "1924"
k      : 2

출력 #1
"94"
"""


def solution(number, k):
    # 스택 선언
    stack = []

    # number의 길이만큼 for loop
    for num in number:
        # 1. 제거할 수 k가 남았고
        # 2. 스택에 값이 있고
        # 3. 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k를 1씩 감소
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        # 스택에 num 추가
        stack.append(num)

    # k가 남아있는 경우 - 테스트 케이스 number: "93939", k: 2, 출력: 999, 실제정답: 99
    if k != 0:
        stack = stack[:-k]

    # 배열을 문자열로 바꿔주고 반환
    return "".join(stack)


print(solution("1924", 2))
