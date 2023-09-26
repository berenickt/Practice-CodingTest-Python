# 💡 로또 📚 https://www.acmicpc.net/problem/6603
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

    # a[i-1]과 a[j]를 교환
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1

    # i부터 j까지의 요소들을 뒤집음
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # 다음 순열을 찾았으므로 True를 반환
    return True


while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break

    # 조합을 생성할 리스트 d 초기화
    d = [0] * (n - 6) + [1] * 6
    ans = []

    while True:
        # 현재 조합에 해당하는 숫자들을 선택
        cur = [a[i] for i in range(n) if d[i] == 1]
        ans.append(cur)

        # 다음 순열을 생성하거나 종료
        if not next_permutation(d):
            break
    # 조합을 정렬
    ans.sort()

    # 결과 출력
    for v in ans:
        print(" ".join(map(str, v)))
    print()
