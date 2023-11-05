# 📚 https://codeup.kr/problem.php?id=3704
"""
피보나치 수열 변형 문제이다.
d[i] = d[i-1] + d[i-2] + d[i-3]
점화식이 3개까지 있기 때문에 초기값도 3개를 선언해줬다.
for문 범위설정에 주의하자.

input #1
5

output #1
13
"""
n = int(input())

d = [0] * 100001

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, n + 1):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000

print(d[n])
