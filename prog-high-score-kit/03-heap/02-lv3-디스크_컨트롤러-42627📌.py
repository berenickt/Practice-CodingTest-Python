# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 
2차원 배열 jobs가 매개변수로 주어질 때, 
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 
평균이 얼마가 되는지 return 

입력 #1
[[0, 3], [1, 9], [2, 6]]

출력 #1
9

입출력 예 설명 #1
0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다. (4)
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다. (9)
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다. (5)
"""
from heapq import heappush, heappop


def solution(jobs):
    jobs.sort()
    num = len(jobs)
    waiting = []  # (소요시간, 요청시점)
    count = []  # 각 작업이 몇초 걸렸는지
    now_time = 0

    while len(count) != num:
        while jobs and now_time >= jobs[0][0]:
            top = jobs.pop(0)
            heappush(waiting, (top[1], top[0]))

        if jobs and waiting == []:
            top = jobs.pop(0)
            now_time = top[0]
            heappush(waiting, (top[1], top[0]))

        x, y = heappop(waiting)
        now_time += x
        count.append(now_time - y)

    return sum(count) // num


print(solution([[0, 3], [1, 9], [2, 6]]))

##################################
import heapq


def solution2(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업들 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0]))
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    return answer // i
