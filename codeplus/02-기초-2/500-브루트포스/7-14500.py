# 💡 테트로미노 📚 https://www.acmicpc.net/problem/14500
"""
입력받은 두 개의 정수 n과 m을 각각 비밀번호의 길이와 비밀번호의 문자 개수로 간주하고
비밀번호를 구성하는 문자 중 깨진 문자의 개수를 최소화하는 비밀번호를 구하는 프로그램
"""
# 입력받은 두 개의 정수를 각각 변수에 저장
n, m = map(int, input().split())

# 비밀번호를 저장할 리스트를 생성
a = [list(map(int, input().split())) for _ in range(n)]

# 비밀번호를 구성하는 문자 중 깨진 문자의 개수를 최소화하는 비밀번호를 구함
ans = 0
for i in range(n):
    for j in range(m):
        if j + 3 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]
            if ans < temp:
                ans = temp

        if i + 3 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j]
            if ans < temp:
                ans = temp

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2]
            if ans < temp:
                ans = temp

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 2][j]
            if ans < temp:
                ans = temp

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 2]
            if ans < temp:
                ans = temp

        if i + 2 < n and j - 1 >= 0:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j - 1]
            if ans < temp:
                ans = temp

        if i - 1 >= 0 and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i - 1][j + 2]
            if ans < temp:
                ans = temp

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j]
            if ans < temp:
                ans = temp

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp

        if i + 1 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
            if ans < temp:
                ans = temp

        if i - 1 >= 0 and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i - 1][j + 1] + a[i - 1][j + 2]
            if ans < temp:
                ans = temp

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2]
            if ans < temp:
                ans = temp

        if i + 2 < n and j - 1 >= 0:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j - 1] + a[i + 2][j - 1]
            if ans < temp:
                ans = temp

        if j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2]
            if i - 1 >= 0:
                temp2 = temp + a[i - 1][j + 1]
                if ans < temp2:
                    ans = temp2

            if i + 1 < n:
                temp2 = temp + a[i + 1][j + 1]
                if ans < temp2:
                    ans = temp2

        if i + 2 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j]
            if j + 1 < m:
                temp2 = temp + a[i + 1][j + 1]
                if ans < temp2:
                    ans = temp2

            if j - 1 >= 0:
                temp2 = temp + a[i + 1][j - 1]
                if ans < temp2:
                    ans = temp2

print(ans)
