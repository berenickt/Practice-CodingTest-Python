# 💡 N과 M (4) 📚 https://www.acmicpc.net/problem/15652
import sys

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# c 배열을 n + 1 크기로 생성하고 모두 False로 초기화
c = [False] * (n + 1)

# a 배열을 n 크기로 생성하고 모두 0으로 초기화
a = [0] * n


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, start, n, m):
    # 만약 index가 m과 같다면, a 배열을 출력하고 종료
    if index == m:
        # m까지 반복하면서 a 배열의 값을 출력
        for i in range(m):
            sys.stdout.write(str(a[i]) + " ")
        sys.stdout.write("\n")  # 줄바꿈
        return

    # start부터 n까지 반복
    for i in range(start, n + 1):
        # c[i]를 True로 설정하고, a[index]에 i를 저장
        c[i] = True

        # a 배열의 index 위치에 i를 저장
        a[index] = i

        # 다음 인덱스에서 재귀적으로 호출
        go(index + 1, i, n, m)

        # c[i]를 False로 다시 설정하여 다음 호출에서 사용
        c[i] = False


# 첫 번째 인덱스에서 go 함수를 호출하여 a 배열을 채워나감
go(0, 1, n, m)
