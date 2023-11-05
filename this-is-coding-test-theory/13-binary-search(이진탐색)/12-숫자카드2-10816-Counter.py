# 📚 https://www.acmicpc.net/problem/10816
"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""
# Counter 함수 사용
import sys
from collections import Counter

n = int(input())
array = sys.stdin.readline().split()

m = int(input())
target = sys.stdin.readline().split()

count = Counter(array)

for i in target:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")
# 👉🏽 3 0 0 1 2 0 0 2
