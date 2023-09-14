# 💡 차이를 최대로 📚 https://www.acmicpc.net/problem/10819
# 주어진 배열의 다음 순열을 반환하는 함수
def next_permutation(a):
    # 배열의 마지막 요소부터 시작
    i = len(a) - 1

    # 만약 이전 요소가 현재 요소보다 크거나 같다면, 이전 요소를 찾음
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1  # 이전 요소를 찾았다면, 다음 요소를 찾음

    # 만약 이전 요소가 없다면, 다음 순열이 존재하지 않으므로 False를 반환
    if i <= 0:
        return False

    # 다음 요소를 찾았다면, 그 다음 요소를 찾음
    j = len(a) - 1

    # 만약 다음 요소가 이전 요소보다 작거나 같다면, 그 다음 요소를 찾음
    while a[j] <= a[i - 1]:
        j -= 1  # 그 다음 요소를 찾았다면, 이전 요소와 그 다음 요소를 교환

    # 이전 요소와 그 다음 요소를 교환
    a[i - 1], a[j] = a[j], a[i - 1]

    # 그 다음 요소부터 마지막 요소까지 역순으로 교환
    j = len(a) - 1

    # i와 j가 교차할 때까지 반복
    while i < j:
        a[i], a[j] = a[j], a[i]  # 두 요소를 교환
        i += 1  # i를 증가
        j -= 1  # j를 감소

    # 다음 순열이 존재한다면 True를 반환
    return True


# 주어진 배열의 차이의 합을 계산하는 함수
def calc(a):
    ans = 0  # 결과값을 저장할 변수를 초기화

    # 배열의 각 요소에 대해 이전 요소와의 차이를 계산
    for i in range(1, len(a)):
        ans += abs(a[i] - a[i - 1])  # 차이의 합을 계산
    # 결과값을 반환
    return ans


# 사용자로부터 n을 입력받음
n = int(input())

# 사용자로부터 n개의 숫자를 입력받아 a 리스트에 저장
a = list(map(int, input().split()))

# a 리스트를 오름차순으로 정렬
a.sort()

# 결과값을 저장할 변수를 초기화
ans = 0

# 다음 순열이 존재할 때까지 반복
while True:
    # 계산 함수를 호출하여 차이의 합을 계산
    temp = calc(a)

    # 결과값과 비교하여 더 큰 값을 결과값으로 저장
    ans = max(ans, temp)

    # 만약 다음 순열이 존재하지 않는다면, 반복을 종료
    if not next_permutation(a):
        break

# 결과값을 출력
print(ans)
