# 💡 이전 순열 📚 https://www.acmicpc.net/problem/10973
# 주어진 배열의 이전 순열을 반환하는 함수
def prev_permutation(a):
    # 배열의 마지막 요소부터 시작
    i = len(a) - 1

    # 만약 이전 요소가 현재 요소보다 작거나 같다면, 이전 요소를 찾음
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1  # 이전 요소를 찾았다면, 다음 요소를 찾음
    # 만약 이전 요소가 없다면, 이전 순열이 존재하지 않으므로 False를 반환
    if i <= 0:
        return False
    # 다음 요소를 찾았다면, 그 다음 요소를 찾음
    j = len(a) - 1

    # 만약 다음 요소가 이전 요소보다 크거나 같다면, 그 다음 요소를 찾음
    while a[j] >= a[i - 1]:
        # 그 다음 요소를 찾았다면, 이전 요소와 그 다음 요소를 교환
        j -= 1

    # 이전 요소와 그 다음 요소를 교환
    a[i - 1], a[j] = a[j], a[i - 1]

    # 그 다음 요소부터 마지막 요소까지 역순으로 교환
    j = len(a) - 1

    # i와 j가 교차할 때까지 반복
    while i < j:
        a[i], a[j] = a[j], a[i]  # 두 요소를 교환
        i += 1  # i를 증가
        j -= 1  # j를 감소

    # 이전 순열이 존재한다면 True를 반환
    return True


# 사용자로부터 n을 입력받음
n = int(input())

# 사용자로부터 n개의 숫자를 입력받아 a 리스트에 저장
a = list(map(int, input().split()))

# 만약 이전 순열이 존재한다면, a 리스트를 출력
if prev_permutation(a):
    print(" ".join(map(str, a)))  # a 리스트의 요소를 공백으로 구분하여 출력
# 만약 이전 순열이 존재하지 않는다면, -1을 출력
else:
    print(-1)
