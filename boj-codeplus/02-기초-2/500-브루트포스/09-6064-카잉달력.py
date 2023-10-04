# 💡 카잉 달력 📚 https://www.acmicpc.net/problem/6064
# 입력받은 테스트 케이스의 개수만큼 반복
TEST_CASE = int(input())

for _ in range(TEST_CASE):
    # 입력받은 네 개의 정수를 각각 m, n, x, y로 저장
    m, n, x, y = map(int, input().split())

    # x와 y를 1씩 감소
    x -= 1
    y -= 1

    # k를 x로 초기화
    k = x

    # k가 n * m보다 작거나 같은 동안 반복
    while k < n * m:
        # k가 n으로 나눈 나머지가 y와 같은 경우, 해당 위치의 값을 출력하고 반복을 종료
        if k % n == y:
            print(k + 1)
            break
        # k를 m만큼 증가
        k += m
    # k가 n * m보다 작거나 같은 동안 반복하면서, k가 n으로 나눈 나머지가 y와 같은 경우를 찾지 못한 경우, -1을 출력
    else:
        print(-1)
