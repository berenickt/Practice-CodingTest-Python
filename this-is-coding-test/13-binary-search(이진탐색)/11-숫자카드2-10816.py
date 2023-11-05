# 📚 https://www.acmicpc.net/problem/10816
"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""

# 딕셔너리 선언 후 값 비교
import sys

n = int(input())
array = sys.stdin.readline().split()
n_dict = {}

for i in array:
    if i in n_dict:
        n_dict[i] = n_dict[i] + 1
    else:
        n_dict[i] = 1

m = int(input())
target = sys.stdin.readline().split()

for i in target:
    if i in n_dict:
        print(n_dict[i], end=" ")
    else:
        print(0, end=" ")
# 👉🏽 3 0 0 1 2 0 0 2
