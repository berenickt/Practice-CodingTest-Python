# 📚 https://www.acmicpc.net/problem/18310
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])
