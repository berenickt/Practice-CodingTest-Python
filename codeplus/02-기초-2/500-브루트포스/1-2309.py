# 💡 일곱 난쟁이 📚 https://www.acmicpc.net/problem/2309
import sys

# 입력받은 숫자의 개수
n = 9

# 입력받은 숫자 리스트
a = [int(input()) for _ in range(n)]

# 숫자 리스트 정렬
a.sort()

# 숫자 리스트의 합
total = sum(a)

# 두 개의 숫자를 선택하여 합이 100이 되는 경우를 찾는 반복문
for i in range(0, n):
    for j in range(i + 1, n):
        # 합이 100인 경우
        if total - a[i] - a[j] == 100:
            # 두 개의 숫자를 제외한 나머지 숫자를 출력하는 반복문
            for k in range(0, n):
                # 이미 출력한 숫자이거나 선택한 두 개의 숫자일 경우 continue
                if i == k or j == k:
                    continue
                # 출력
                print(a[k])
            # 종료
            sys.exit(0)
