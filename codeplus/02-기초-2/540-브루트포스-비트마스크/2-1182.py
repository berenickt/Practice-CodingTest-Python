# 💡 부분집합의 합 📚 https://www.acmicpc.net/problem/1182

# 입력: n은 원소의 개수, m은 목표 합
n, m = map(int, input().split())

# 입력: n개의 원소 리스트
a = list(map(int, input().split()))

# 가능한 부분집합 중 합이 m인 경우의 수를 저장할 변수
ans = 0

# 1부터 2^n까지의 모든 부분집합을 반복 탐색
for i in range(1, (1 << n)):
    # 현재 부분집합의 합을 계산
    s = sum(a[k] for k in range(n) if (i & (1 << k)) > 0)

    # 목표 합과 일치하는 경우, 가능한 경우의 수를 증가
    if m == s:
        ans += 1

# 결과 출력: 가능한 부분집합 중 합이 m인 경우의 수
print(ans)
