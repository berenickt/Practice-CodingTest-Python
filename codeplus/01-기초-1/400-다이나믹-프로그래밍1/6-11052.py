# 💡 카드 구매하기 📚 https://www.acmicpc.net/problem/11052
# 정수 n을 입력받음
n = int(input())

# 리스트 a에 0을 추가하고, 사용자로부터 입력받은 숫자들을 리스트로 변환하여 저장
a = [0] + list(map(int, input().split()))

# 각 위치에서 얻을 수 있는 최대 값을 저장할 배열 d를 초기화
d = [0] * (n + 1)

# 바텀업(DP) 방식으로 최대 값을 계산
for i in range(1, n + 1):
    # i번째 위치에서 얻을 수 있는 최대 값은
    # i - j 번째 위치에서 얻을 수 있는 최대 값에 a[j]를 더한 값 중 최댓값입니다.
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + a[j])

# n번째 위치에서 얻을 수 있는 최대 값을 출력
print(d[n])
