# 💡 Guess(맞춰봐) 📚 https://www.acmicpc.net/problem/1248
def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            # 연속하는 부분합이 0이 아닌 경우 False 반환
            if s != 0:
                return False
        elif sign[i][index] < 0:
            # 연속하는 부분합이 음수가 아닌 경우 False 반환
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            # 연속하는 부분합이 양수가 아닌 경우 False 반환
            if s <= 0:
                return False

    # 모든 조건을 만족하면 True 반환
    return True


def go(index):
    # 모든 숫자를 결정한 후 부등호 관계를 만족하는지 확인하여 True 또는 False 반환
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        # 현재 위치에 0을 할당하고 부등호 관계를 확인하여 True 또는 False 반환
        return check(index) and go(index + 1)

    for i in range(1, 11):
        # 현재 위치에 부등호 관계에 따라 양수 또는 음수를 할당
        ans[index] = i * sign[index][index]

        # 부등호 관계를 만족하고 다음 자리로 진행한 결과가 True이면 True 반환
        if check(index) and go(index + 1):
            return True

    # 모든 숫자를 시도한 후에도 부등호 관계를 만족하는 경우가 없으면 False 반환
    return False


n = int(input())  # 입력: 부등호의 개수
s = input()  # 입력: 부등호 문자열
sign = [[0] * n for _ in range(n)]  # 부등호 관계를 저장할 이차원 리스트
ans = [0] * n  # 결과를 저장할 리스트
cnt = 0  # 부등호 문자열을 처리하기 위한 인덱스

for i in range(n):
    for j in range(i, n):
        if s[cnt] == "0":
            sign[i][j] = 0
        elif s[cnt] == "+":
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        # 부등호 문자열 인덱스 증가
        cnt += 1

go(0)  # 숫자 결정 과정 시작
print(" ".join(map(str, ans)))  # 결정된 숫자 리스트 출력
