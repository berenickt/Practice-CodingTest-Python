# 💡 괄호 📚 https://www.acmicpc.net/problem/9012
def valid(s):
    cnt = 0  # 괄호 쌍을 유지하기 위한 카운트 변수 초기화

    for ch in s:
        if ch == '(':  # 여는 괄호일 경우 카운트 증가 (괄호 쌍 시작)
            cnt += 1
        else:          # 닫는 괄호일 경우 카운트 감소 (괄호 쌍 끝)
            cnt -= 1
        if cnt < 0:    # 중간에 닫는 괄호가 더 많을 경우
            return 'NO'
    if cnt == 0:     # 모든 괄호가 쌍을 이루었을 경우
        return 'YES'
    else:            # 괄호 쌍이 다 맞지 않는 경우
        return 'NO'


t = int(input())   # 테스트 케이스 개수 입력
for _ in range(t):  # 각 테스트 케이스에 대해 반복
    print(valid(input()))  # 결과 출력
