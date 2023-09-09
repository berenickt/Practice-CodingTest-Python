# 💡 골드바흐 파티션 📚 https://www.acmicpc.net/problem/17103
check = [False] * 1000001
primes = []

for i in range(2, 1000001):
    if check[i] == False:
        primes.append(i)
        j = i + i
        while j <= 1000000:
            check[j] = True
            j += i

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for p in primes:
        if n - p >= 2 and p <= n - p:
            if check[n - p] == False:
                ans += 1
        else:
            break
    print(ans)
