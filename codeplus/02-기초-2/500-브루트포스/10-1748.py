# 💡 수 이어 쓰기 1 📚 https://www.acmicpc.net/problem/1748
n = int(input())  # 사용자로부터 정수 n을 입력받음

# 결과값을 저장할 변수를 초기화
ans = 0

# 시작 숫자를 1로 설정
start = 1

# 각 자리수의 길이를 1로 설정
length = 1

# 시작 숫자가 n보다 작거나 같은 동안 반복
while start <= n:
    # 시작 숫자의 10배에서 1을 뺀 값을 end로 설정
    end = start * 10 - 1

    # end가 n보다 크면 end를 n으로 설정
    if end > n:
        end = n

    # 시작부터 끝까지의 숫자의 개수와 각 자리수의 길이를 곱한 값을 ans에 더함
    ans += (end - start + 1) * length

    # 시작 숫자를 10배로 곱함
    start *= 10

    # 각 자리수의 길이를 1씩 증가
    length += 1

# 결과값을 출력
print(ans)
