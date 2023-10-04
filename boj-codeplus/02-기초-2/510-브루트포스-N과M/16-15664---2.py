# 💡 N과 M (11) 📚 https://www.acmicpc.net/problem/15664
import sys

# 사용자로부터 n과 m을 입력받음
n, m = map(int, input().split())

# 사용자로부터 n개의 숫자를 입력받아 num 리스트에 저장
num = list(map(int, input().split()))

# num 리스트를 오름차순으로 정렬
num.sort()

# c 배열을 n 크기로 생성하고 모두 False로 초기화
c = [False] * n

a = [0] * m  # a 배열을 m 크기로 생성하고 모두 0으로 초기화
d = []  # d 리스트를 생성


# 재귀 함수를 사용하여 a 배열을 채워나가는 함수
def go(index, start, n, m):
    # 만약 index가 m과 같다면, a 배열을 기반으로 d 리스트에 튜플을 추가
    if index == m:
        d.append(tuple(a))  # d 리스트에 튜플을 추가
        return
    # start부터 n까지 반복
    for i in range(start, n):
        # c[i]를 True로 설정하고, a[index]에 num[i]를 저장
        c[i] = True

        # a 배열의 index 위치에 num[i]를 저장
        a[index] = num[i]

        # 다음 인덱스에서 재귀적으로 호출
        go(index + 1, 0, n, m)

        # c[i]를 False로 다시 설정하여 다음 호출에서 사용할 수 있도록 함
        c[i] = False


go(0, 0, n, m)  # 첫 번째 인덱스에서 go 함수를 호출하여 a 배열을 채워나감
d = sorted(list(set(d)))  # d 리스트에서 중복된 요소를 제거하고, 오름차순으로 정렬

# d 리스트의 각 요소를 출력
for v in d:
    # 각 요소를 공백으로 구분하여 출력
    sys.stdout.write(" ".join(map(str, v)) + "\n")
