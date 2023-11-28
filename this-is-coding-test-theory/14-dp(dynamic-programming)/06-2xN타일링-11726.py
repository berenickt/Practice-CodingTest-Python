# 📚 https://www.acmicpc.net/problem/11726
"""
2 x n 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2x5 크기의 직사각형을 채운 한 가지 방법의 예이다.

input #1
2

output #1 2 x n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지
2

input #2
9

output #2 
55

Tip 
타일은 1x2 이나 2x1 타일 중 한가지 종류만 사용해서 채워도 괜찮습니다.
해당 문제는 단순한 점화식으로 해결할 수 있습니다.
dp[i] = dp[i-1] + dp[i-2]

점화식을 구할 때 N=1, N=2일 때의 경우의 수를 구하고 
처음에 선언해준 뒤 나중에 N-1, N-2의 경우의 수를 구하면 끝이었다.
"""

n = int(input())

# memoization을 위함
cache = [0] * 1001

# n이 1,2인 경우는 명확하니까 미리 선언해둔다.
cache[1] = 1
cache[2] = 2

# dynamic programming
for i in range(3, 1001):
    cache[i] = (cache[i - 1] + cache[i - 2]) % 10007

print(cache[n])
