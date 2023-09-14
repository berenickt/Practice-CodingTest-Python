# 💡 외판원 순회 2 📚 https://www.acmicpc.net/problem/10971
def next_permutation(a):
    i = len(a) - 1

    # 다음 순열을 찾을 때까지 i를 감소
    # a[i-1]이 a[i]보다 크거나 같은 경우를 찾음
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1

    # 더 이상 다음 순열이 없는 경우 False를 반환
    if i <= 0:
        return False

    j = len(a) - 1

    # a[j]가 a[i-1]보다 작거나 같은 경우를 찾음
    while a[j] <= a[i - 1]:
        j -= 1

    # a[i-1]과 a[j]를 교환합
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1

    # i부터 j까지의 요소들을 뒤집음
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # 다음 순열을 찾았으므로 True를 반환
    return True


# 사용자로부터 n을 입력받아 n개의 행렬을 입력받아 w 리스트에 저장
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
d = list(range(n))
ans = 2147483647

while True:
    ok = True
    s = 0

    # 모든 도시를 순회하며 경로의 유효성을 확인
    for i in range(0, n - 1):
        if w[d[i]][d[i + 1]] == 0:
            ok = False
            break
        else:
            s += w[d[i]][d[i + 1]]

    # 마지막 도시에서 시작 도시로 돌아갈 수 있는 경우 경로를 완성하고 최솟값을 갱신
    if ok and w[d[-1]][d[0]] != 0:
        s += w[d[-1]][d[0]]
        ans = min(ans, s)

    # 모든 순열을 시도
    if not next_permutation(d):
        break

    # 시작 도시가 0인 순열만 고려
    if d[0] != 0:
        break

# 최소 경로 출력
print(ans)
