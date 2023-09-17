# 💡 괄호 📚 https://www.acmicpc.net/problem/9012
def getIsParentheses(s):
    count = 0  # 괄호 쌍을 유지하기 위한 카운트 변수 초기화

    for ch in s:
        # 여는 괄호일 경우 카운트 증가 (괄호 쌍 시작)
        if ch == "(":
            count += 1
        # 닫는 괄호일 경우 카운트 감소 (괄호 쌍 끝)
        else:
            count -= 1
        # 중간에 닫는 괄호가 더 많을 경우
        if count < 0:
            return "NO"
    # 모든 괄호가 쌍을 이루었을 경우
    if count == 0:
        return "YES"
    # 괄호 쌍이 다 맞지 않는 경우
    else:
        return "NO"


TEST_CASE = int(input())

for _ in range(TEST_CASE):
    print(getIsParentheses(input()))
