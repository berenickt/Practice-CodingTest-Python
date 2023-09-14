# 💡 N과 M (4) 📚 https://www.acmicpc.net/problem/15652
import sys

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# cnt 배열을 n + 1 크기로 생성하고 모두 0으로 초기화
cnt = [0] * (n + 1)


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, selected, n, m):
    # 만약 선택된 숫자가 m과 같다면, a 배열을 출력하고 종료
    if selected == m:
        # 1부터 n까지 반복하면서 cnt 배열의 값을 출력
        for i in range(1, n + 1):
            # cnt[i]만큼 반복하면서 i를 출력
            for j in range(cnt[i]):
                sys.stdout.write(str(i) + " ")
        sys.stdout.write("\n")  # 줄바꿈
        return

    # 만약 index가 n보다 크다면, 더 이상 숫자를 선택할 수 없으므로 종료
    if index > n:
        return

    # m - 선택된 숫자부터 0까지 역순으로 반복
    for i in range(m - selected, 0, -1):
        # cnt 배열의 index 위치에 i를 저장
        cnt[index] = i

        # 다음 선택된 위치에서 재귀적으로 호출
        go(index + 1, selected + i, n, m)

    # cnt 배열의 index 위치에 0을 저
    cnt[index] = 0

    # 다음 선택된 위치에서 재귀적으로 호출
    go(index + 1, selected, n, m)


# 첫 번째 선택된 위치에서 go 함수를 호출하여 a 배열을 채워나감
go(1, 0, n, m)
