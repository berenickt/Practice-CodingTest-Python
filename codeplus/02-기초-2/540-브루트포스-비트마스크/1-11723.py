# 💡 집합 📚 https://www.acmicpc.net/problem/11723
import sys

n = 20  # 비트 벡터의 크기 (비트 벡터의 길이)
m = int(sys.stdin.readline())  # 입력: 명령어의 개수
s = 0  # 초기 비트 벡터

for _ in range(m):
    # 입력: 명령어와 숫자 (op는 명령어, num은 명령어와 함께 주어진 숫자)
    op, *num = sys.stdin.readline().split()

    # 숫자가 주어진 경우 0부터 시작하는 인덱스로 변환
    if len(num) > 0:
        x = int(num[0]) - 1

    # 비트 벡터에서 해당 비트를 1로 설정 (OR 연산)
    if op == "add":
        s = s | (1 << x)

    # 비트 벡터에서 해당 비트를 0으로 설정 (AND 연산 후 NOT 연산)
    elif op == "remove":
        s = s & ~(1 << x)

    elif op == "check":
        # 비트 벡터에서 해당 비트의 상태 확인 (AND 연산)
        res = s & (1 << x)

        # 해당 비트가 1로 설정되어 있으면 1 출력
        if res > 0:
            sys.stdout.write("1\n")

        # 해당 비트가 0으로 설정되어 있으면 0 출력
        else:
            sys.stdout.write("0\n")

    # 비트 벡터에서 해당 비트를 반전 (XOR 연산)
    elif op == "toggle":
        s = s ^ (1 << x)

    # 모든 비트를 1로 설정 (2^n - 1로 계산)
    elif op == "all":
        s = (1 << n) - 1

    # 비트 벡터를 모두 0으로 초기화
    else:
        s = 0
