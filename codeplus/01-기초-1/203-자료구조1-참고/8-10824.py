# 💡 네 수 📚 https://www.acmicpc.net/problem/10824
# 네 개의 정수를 입력받습니다.
a, b, c, d = map(int, input().split())

# 두 개의 정수를 문자열로 합칩니다.
s1 = str(a) + str(b)
s2 = str(c) + str(d)

# 문자열을 정수로 변환합니다.
l1 = int(s1)
l2 = int(s2)

# 두 정수를 더한 결과를 출력
print(l1+l2)
