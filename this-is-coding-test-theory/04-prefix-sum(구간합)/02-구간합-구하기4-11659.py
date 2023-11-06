# 📚 https://www.acmicpc.net/problem/11659
"""
수 N개가 주어졌을 때, 
i번째 수부터 j번째 수까지 합을 구하는 프로그램

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M
둘째 줄에는 N개의 수
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j

input #1
5 3
5 4 3 2 1
1 3
2 4
5 5

output #1
12
9
1
"""
import sys

n, m = map(int, input().split())
data_input = list(map(int, sys.stdin.readline().split()))

# 접두사 합(Prefix Sum) 배열 계산
value_sum = 0
prefix_sum = [0]

for i in data_input:
    value_sum = value_sum + i  # 15
    prefix_sum.append(value_sum)  # [0, 5, 9, 12, 14, 15]

# 구간 합 계산
for i in range(m):  # 0 ~ 2
    left, right = map(int, sys.stdin.readline().split())
    # testcase #1 : p[3] - p[0]
    result = prefix_sum[right] - prefix_sum[left - 1]
    print(result)
