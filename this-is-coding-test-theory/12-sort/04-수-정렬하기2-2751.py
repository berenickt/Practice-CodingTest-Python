# 📚 https://www.acmicpc.net/problem/2751
"""
문제는 2750과 유사하나 N의 범위가 (1 <= N <= 1,000,000)로 늘어났다.
이때는, input() 대신 sys.stdin.readline()을 사용하여 시간을 단축시키자.
또, 선택정렬과 삽입정렬을 사용했더니 시간초과 판정이 나서 기본 라이브러리인 sort()로 푼다
"""
import sys

n = int(input())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array = sorted(array)

for i in array:
    print(i)
