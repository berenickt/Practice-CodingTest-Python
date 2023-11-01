# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""
출발지점부터 도착지점까지의 거리 distance, 
바위들이 있는 위치를 담은 배열 rocks, 
제거할 바위의 수 n이 매개변수로 주어질 때,
바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 
가장 큰 값을 return

입력 #1
distance : 25
rocks    : [2, 14, 11, 21, 17]
n        : 2

출력 #1
4
"""


def solution(distance, rocks, n):
    maxOfmin = 0
    start, end = 0, distance
    rocks.append(distance)  # 마지막 도착지까지 거리를 계산하기 위해 추가
    rocks.sort()  # 오름차순 정렬

    # 이분 탐색 수행
    while start <= end:
        mid = (start + end) // 2  # 특정한 최소거리
        current, remove = 0, 0  # 현재 위치, 제거할 바위 수
        min_distance = float("inf")  # mid에서 최소 거리

        # 거리 구하기
        for rock in rocks:
            dis = rock - current
            # mid 보다 작으면, 바위 제거
            if dis < mid:
                remove += 1
            # mid 보다 작지 않다면, 현재 위치 옮기고 mid에서 최소 거리 계산
            else:
                current = rock
                min_distance = min(min_distance, dis)

        # n보다 많다면 mid를 줄임
        if remove > n:
            end = mid - 1
        # n보다 많지 않다면 최소 거리를 answer에 저장하고 mid를 늘림
        else:
            maxOfmin = min_distance
            start = mid + 1

    return maxOfmin


print(solution(25, [2, 14, 11, 21, 17], 2))
