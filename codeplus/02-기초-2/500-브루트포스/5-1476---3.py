# 💡 날짜 계산 📚 https://www.acmicpc.net/problem/1476
"""
모든 E, S, M에서 1을 빼면, 이 문제는 당므을 만족하는 가장 작은 자연수 year를 찾는 문제
"""
e, s, m = map(int, input().split())
print((6916 * e + 4845 * s + 4200 * m - 1) % (15 * 28 * 19) + 1)
