# 💡 가장 긴 증가하는 부분 수열 @https://www.acmicpc.net/problem/11053
n = int(input())
a = list(map(int,input().split()))
d = [0]*n

for i in range(n):
  d[i] = 1
  for j in range(i):
    if a[j] < a[i] and d[j]+1 > d[i]:
      d[i] = d[j]+1

print(max(d))