# 💡 1, 2, 3 더하기 📚 https://www.acmicpc.net/problem/9095
# 사용자로부터 테스트 케이스의 개수를 입력받음
TEST_CASE = int(input())

# 테스트 케이스의 개수만큼 반복
for _ in range(TEST_CASE):
    # 결과값을 저장할 변수를 초기화
    ans = 0

    # 사용자로부터 숫자 n을 입력받음
    n = int(input())

    # 1부터 3까지의 숫자를 l1에 대입
    for l1 in range(1, 4):
        # 만약 l1이 n과 같다면 ans에 1을 더함
        if l1 == n:
            ans += 1

        # 1부터 3까지의 숫자를 l2에 대입
        for l2 in range(1, 4):
            if l1 + l2 == n:
                ans += 1

            # 1부터 3까지의 숫자를 l3에 대입
            for l3 in range(1, 4):
                if l1 + l2 + l3 == n:
                    ans += 1

                # 1부터 3까지의 숫자를 l4에 대입
                for l4 in range(1, 4):
                    if l1 + l2 + l3 + l4 == n:
                        ans += 1

                    # 1부터 3까지의 숫자를 l5에 대입
                    for l5 in range(1, 4):
                        if l1 + l2 + l3 + l4 + l5 == n:
                            ans += 1

                        # 1부터 3까지의 숫자를 l6에 대입
                        for l6 in range(1, 4):
                            if l1 + l2 + l3 + l4 + l5 + l6 == n:
                                ans += 1

                            # 1부터 3까지의 숫자를 l7에 대입
                            for l7 in range(1, 4):
                                if l1 + l2 + l3 + l4 + l5 + l6 + l7 == n:
                                    ans += 1

                                # 1부터 3까지의 숫자를 l8에 대입
                                for l8 in range(1, 4):
                                    if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == n:
                                        ans += 1

                                    # 1부터 3까지의 숫자를 l9에 대입
                                    for l9 in range(1, 4):
                                        if (
                                            l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
                                            == n
                                        ):
                                            ans += 1

                                        # 1부터 3까지의 숫자를 l0에 대입
                                        for l0 in range(1, 4):
                                            if (
                                                l1
                                                + l2
                                                + l3
                                                + l4
                                                + l5
                                                + l6
                                                + l7
                                                + l8
                                                + l9
                                                + l0
                                                == n
                                            ):
                                                ans += 1
    print(ans)
