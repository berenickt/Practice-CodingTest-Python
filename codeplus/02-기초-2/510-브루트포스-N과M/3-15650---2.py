# 💡 N과 M (2) 📚 https://www.acmicpc.net/problem/15650
import sys

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# a 배열을 m 크기로 생성하고 모두 0으로 초기화
a = [0] * m


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, selected, n, m):
    # 만약 선택된 숫자가 m과 같다면, a 배열을 출력하고 종료
    if selected == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return

    # 만약 index가 n보다 크다면, 더 이상 숫자를 선택할 수 없으므로 종료
    if index > n:
        return

    # a 배열의 선택된 위치에 index를 저장
    a[selected] = index

    # 다음 선택된 위치에서 재귀적으로 호출
    go(index + 1, selected + 1, n, m)

    # 선택된 위치의 값을 다시 0으로 초기화
    a[selected] = 0

    # 다음 선택된 위치에서 재귀적으로 호출
    go(index + 1, selected, n, m)


# 첫 번째 선택된 위치에서 go 함수를 호출하여 a 배열을 채워나감
go(1, 0, n, m)
