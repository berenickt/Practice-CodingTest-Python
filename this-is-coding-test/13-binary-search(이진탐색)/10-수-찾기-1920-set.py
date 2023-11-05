# 📚 https://www.acmicpc.net/problem/1920
# set 자료형
"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
import sys

n = int(input())
array = set(map(int, sys.stdin.readline().split()))

m = int(input())
target = list(map(int, sys.stdin.readline().split()))

for i in target:
    if i in array:
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
"""
결론적으로 둘 다 정답판정을 받았지만,
set자료형을 이용한 풀이가 이진탐색(재귀)의 경우보다 3.8배 정도 시간이 단축된 것을 확인할 수 있었다.
"""
