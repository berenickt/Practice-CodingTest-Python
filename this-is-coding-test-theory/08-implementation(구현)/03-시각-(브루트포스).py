"""📍 brute_force
모든 경우의 수를 판단하는 알고리즘
브루트 포스(BruteForce)라고 불리며,
보통 데이터가 1,000,000개 이하 일때 완전탐색을 이용하면 적절하다.
"""
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)
