# 💡 소인수분해 @https://www.acmicpc.net/problem/11653
n = int(input())
i = 2
while i*i <= n:
  while n % i == 0:
    print(i)
    n //= i
  i += 1

if n > 1:
  print(n)