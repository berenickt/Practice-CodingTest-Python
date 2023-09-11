# 💡 2×n 타일링 2 📚 https://www.acmicpc.net/problem/9095
# 각 경우의 수를 저장하기 위한 배열 d를 초기화
d = [0] * 11

# 0의 경우의 수는 1로 초기화
d[0] = 1

# 배열 d를 채워나감
for i in range(1, 11):
    if i - 1 >= 0:
        d[i] += d[i - 1]  # 현재 항은 이전 항의 경우의 수를 더함
    if i - 2 >= 0:
        d[i] += d[i - 2]  # 현재 항은 그 이전 항의 경우의 수를 더함
    if i - 3 >= 0:
        d[i] += d[i - 3]  # 현재 항은 그 이전 항의 경우의 수를 더함

# 테스트 케이스의 개수를 입력받음
TEST_CASE = int(input())

# 각 테스트 케이스에 대해 경우의 수를 출력
for _ in range(TEST_CASE):
    n = int(input())  # n을 입력받음
    print(d[n])  # n에 대한 경우의 수를 출력
