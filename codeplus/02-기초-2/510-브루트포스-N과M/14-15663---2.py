# 💡 N과 M (9) 📚 https://www.acmicpc.net/problem/15663
import sys
from collections import Counter

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# 사용자로부터 n개의 숫자를 입력받아 temp 리스트에 저장함
temp = list(map(int, input().split()))

# Counter를 사용하여 각 숫자의 빈도를 계산
temp = list(Counter(temp).items())

# temp 리스트를 오름차순으로 정렬
temp.sort()

# n의 값을 갱신
n = len(temp)

# num과 cnt 리스트를 생성
num, cnt = map(list, zip(*temp))

# a 배열을 m 크기로 생성하고 모두 0으로 초기화
a = [0] * m


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, n, m):
    # 만약 index가 m과 같다면, a 배열을 출력하고 종료
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    # n까지 반복
    for i in range(n):
        # 만약 cnt[i]가 0보다 크다면, 해당 숫자를 선택
        if cnt[i] > 0:
            cnt[i] -= 1  # cnt[i]를 1 감소
            a[index] = num[i]  # a 배열의 index 위치에 num[i]를 저장
            go(index + 1, n, m)  # 다음 인덱스에서 재귀적으로 호출
            cnt[i] += 1  # cnt[i]를 1 증가


# 첫 번째 인덱스에서 go 함수를 호출하여 a 배열을 채워나감
go(0, n, m)
