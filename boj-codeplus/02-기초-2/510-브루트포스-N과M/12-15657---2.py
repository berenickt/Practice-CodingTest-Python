# 💡 N과 M (8) 📚 https://www.acmicpc.net/problem/15657
import sys

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# 사용자로부터 n개의 숫자를 입력받아 num 리스트에 저장
num = list(map(int, input().split()))

# num 리스트를 오름차순으로 정렬
num.sort()

# cnt 배열을 n 크기로 생성하고 모두 0으로 초기화
cnt = [0] * n


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, selected, n, m):
    # 만약 선택된 숫자가 m과 같다면, a 배열을 출력하고 종료
    if selected == m:
        # n까지 반복
        for i in range(n):
            # cnt[i]까지 반복
            for j in range(cnt[i]):
                # num[i]를 출력
                sys.stdout.write(str(num[i]) + " ")
        sys.stdout.write("\n")  # 줄바꿈
        return

    # 만약 index가 n보다 크다면, 더 이상 숫자를 선택할 수 없으므로 종료
    if index >= n:
        return

    # m - selected부터 0까지 역순으로 반복
    for i in range(m - selected, 0, -1):
        # cnt[index]에 i를 저장
        cnt[index] = i

        # 다음 선택된 위치에서 재귀적으로 호출
        go(index + 1, selected + i, n, m)

    # cnt[index]에 0을 저장
    cnt[index] = 0

    # 다음 선택된 위치에서 재귀적으로 호출
    go(index + 1, selected, n, m)


# 첫 번째 선택된 위치에서 go 함수를 호출하여 a 배열을 채워나감
go(0, 0, n, m)
