# 💡 스타트와 링크 📚 https://www.acmicpc.net/problem/14889
# 입력: 팀원의 수
n = int(input())

# 입력: 능력치 행렬
s = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 변수, 초기값은 -1로 설정
ans = -1

# 모든 가능한 팀 조합을 검사하기 위한 반복문
for i in range((1 << n)):
    # 현재 팀의 멤버 수를 저장하는 변수
    cnt = 0
    for j in range(n):
        # 비트마스크를 사용하여 현재 팀의 멤버 수 계산
        if (i & (1 << j)) > 0:
            cnt += 1

    # 팀의 크기가 반씩 나뉘지 않으면 스킵
    if cnt != n // 2:
        continue

    first = []  # 첫 번째 팀의 멤버를 저장하는 리스트
    second = []  # 두 번째 팀의 멤버를 저장하는 리스트

    for j in range(n):
        # 비트마스크를 사용하여 팀 멤버를 구분
        if (i & (1 << j)) > 0:
            first += [j]
        else:
            second += [j]

    # 팀의 크기가 반씩 나뉘지 않으면 스킵
    if len(first) != n // 2:
        continue

    t1 = 0  # 첫 번째 팀의 능력치 합을 저장하는 변수
    t2 = 0  # 두 번째 팀의 능력치 합을 저장하는 변수

    for l1 in range(n // 2):
        for l2 in range(n // 2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]  # 첫 번째 팀의 능력치 합 계산
            t2 += s[second[l1]][second[l2]]  # 두 번째 팀의 능력치 합 계산

    # 두 팀 능력치 차이의 절대값 계산
    diff = abs(t1 - t2)

    # 현재 차이가 최소인 경우 ans 업데이트
    if ans == -1 or ans > diff:
        ans = diff

# 최소 능력치 차이 출력
print(ans)
