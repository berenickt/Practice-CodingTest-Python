# 📚 https://www.acmicpc.net/problem/11659
"""
수 N개가 주어졌을 때, 
i번째 수부터 j번째 수까지 합을 구하는 프로그램

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M
둘째 줄에는 N개의 수
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j
"""
import sys

n, m = map(int, input().split())
data_input = list(map(int, sys.stdin.readline().split()))

value_sum = 0
prefix_sum = [0]

for i in data_input:
    value_sum = value_sum + i
    prefix_sum.append(value_sum)

for i in range(m):
    left, right = map(int, sys.stdin.readline().split())
    result = prefix_sum[right] - prefix_sum[left - 1]
    print(result)
