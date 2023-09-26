# 💡 스타트와 링크 📚 https://www.acmicpc.net/problem/14889
def go(index, first, second):
    # 모든 사람이 팀을 선택한 경우
    if index == n:
        # 팀의 크기가 n/2와 다른 경우, 유효하지 않으므로 -1을 반환
        if len(first) != n // 2:
            return -1
        if len(second) != n // 2:
            return -1

        # 팀의 능력치 차이 계산
        t1 = 0
        t2 = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff

    # 첫 번째 팀의 크기가 n/2를 넘어가는 경우 유효하지 않음
    if len(first) > n // 2:
        return -1

    # 두 번째 팀의 크기가 n/2를 넘어가는 경우 유효하지 않음
    if len(second) > n // 2:
        return -1
    ans = -1

    # 현재 인덱스를 첫 번째 팀에 추가하고 다음 인덱스로 이동
    t1 = go(index + 1, first + [index], second)

    # 현재까지 최소 능력치 차이보다 작은 값이 나오면 갱신
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1

    # 현재 인덱스를 두 번째 팀에 추가하고 다음 인덱스로 이동
    t2 = go(index + 1, first, second + [index])

    # 현재까지 최소 능력치 차이보다 작은 값이 나오면 갱신
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 함수 호출 및 결과 출력
print(go(0, [], []))
