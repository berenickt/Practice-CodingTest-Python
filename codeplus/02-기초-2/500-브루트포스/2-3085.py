# 💡 사탕 게임 📚 https://www.acmicpc.net/problem/3085
# 주어진 2차원 배열의 각 행과 열에서 연속된 같은 값의 개수를 반환하는 함수
def check(a):
    n = len(a)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if a[i][j] == a[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if a[j][i] == a[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


# 입력받은 배열의 크기
n = int(input())

# 입력받은 배열
a = [list(input()) for _ in range(n)]

# 최댓값을 저장할 변수
ans = 0

# 배열의 각 원소를 왼쪽과 위쪽으로 이동시켜보며 최댓값을 찾는 반복문
for i in range(n):
    for j in range(n):
        # 왼쪽으로 이동할 수 있는 경우
        if j + 1 < n:
            # 왼쪽으로 이동
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            # check 함수를 호출하여 결과를 저장
            temp = check(a)
            # 최댓값보다 큰 경우 최댓값을 갱신
            if ans < temp:
                ans = temp
            # 원래 위치로 이동
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        # 위쪽으로 이동할 수 있는 경우
        if i + 1 < n:
            # 위쪽으로 이동
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            # check 함수를 호출하여 결과를 저장
            temp = check(a)
            # 최댓값보다 큰 경우 최댓값을 갱신
            if ans < temp:
                ans = temp
            # 원래 위치로 이동
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]

# 최댓값을 출력
print(ans)
