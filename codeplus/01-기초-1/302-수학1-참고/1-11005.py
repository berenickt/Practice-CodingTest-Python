# 💡 진법 변환 2 @https://www.acmicpc.net/problem/11005
n, b = map(int,input().split())
ans = ''

while n > 0:
  r = n % b
  if r < 10: ans += str(r)
  else: ans += chr(r - 10 + ord('A'))
  n //= b

ans = ans[::-1]
print(ans)