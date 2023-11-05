# 📚 https://www.acmicpc.net/problem/1920
# 이진탐색(재귀)
"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
import sys


def find_number(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return find_number(array, target, start, mid - 1)
    else:
        return find_number(array, target, mid + 1, end)


n = int(input())
array = sorted(list(map(int, sys.stdin.readline().split())))

m = int(input())
target = list(map(int, sys.stdin.readline().split()))

for i in target:
    if find_number(array, i, 0, n - 1):
        print(1)
    else:
        print(0)
# 👉🏽
# 1
# 1
# 0
# 0
# 0
# 1
