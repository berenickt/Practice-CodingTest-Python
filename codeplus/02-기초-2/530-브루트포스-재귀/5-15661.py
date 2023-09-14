# 💡 링크와 스타트 📚 https://www.acmicpc.net/problem/15661
def go(index, first, second):
    # 모든 사람이 팀을 선택한 경우
    if index == n:
        # 첫 번째 팀 또는 두 번째 팀이 비어있는 경우 유효하지 않으므로 -1을 반환
        if len(first) == 0:
            return -1
        if len(second) == 0:
            return -1
        t1 = 0
        t2 = 0

        # 첫 번째 팀의 능력치 합 계산
        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue
                t1 += s[p1][p2]

        # 두 번째 팀의 능력치 합 계산
        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]
        diff = abs(t1 - t2)
        return diff
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
