# 💡 부등호 📚 https://www.acmicpc.net/problem/2529
def ok(num):
    for i in range(n):
        # 만약 현재 인덱스의 부등호가 "<"이고, 현재 숫자가 다음 숫자보다 크다면 False 반환
        if a[i] == "<":
            if num[i] > num[i + 1]:
                return False
        # 만약 현재 인덱스의 부등호가 ">"이고, 현재 숫자가 다음 숫자보다 작다면 False 반환
        elif a[i] == ">":
            if num[i] < num[i + 1]:
                return False

    # 모든 부등호 관계가 유효하면 True 반환
    return True


def go(index, num):
    if index == n + 1:
        # 모든 자리 숫자가 결정되었고, 부등호 관계가 유효한 경우에 결과 리스트에 숫자 추가
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        # 이미 사용된 숫자인 경우 스킵
        if check[i]:
            continue

        # 숫자 i를 사용함을 표시
        check[i] = True

        # 다음 자리 숫자를 결정하기 위해 재귀 호출
        go(index + 1, num + str(i))

        # 다른 자리에서 숫자 i를 사용하기 위해 표시 제거
        check[i] = False


# 입력: 부등호의 개수
n = int(input())

# 입력: 부등호 문자열을 공백으로 나눠서 리스트로 저장
a = input().split()

# 결과를 저장할 리스트
ans = []

# 사용된 숫자를 체크하기 위한 리스트
check = [False] * 10


go(0, "")  # 숫자 결정 과정 시작
ans.sort()  # 결과 리스트를 정렬
print(ans[-1])  # 가장 큰 수 출력
print(ans[0])  # 가장 작은 수 출력
