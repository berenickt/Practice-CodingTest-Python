# 💡 퇴사 📚 https://www.acmicpc.net/problem/14501
inf = -(10**9)
n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)

# 각 날짜에 대한 상담 시간과 보수 입력
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

ans = 0


# 가능한 모든 일정을 확인하며 최대 보수를 구하는 함수
def go(day, s):
    global ans

    # 모든 일정을 확인한 경우 최대 보수 갱신
    if day == n + 1:
        ans = max(ans, s)
        return

    # 이미 마감일이 지난 경우와 아직 마감일이 지나지 않은 경우를 각각 고려
    if day > n + 1:
        return

    # 현재 일정을 선택하지 않고 다음 날짜로 진행
    go(day + 1, s)

    # 현재 일정을 선택하고 해당 일정 종료일에 보수를 더함
    go(day + t[day], s + p[day])


# 첫 날부터 시작하여 최대 보수 계산
go(1, 0)
print(ans)
