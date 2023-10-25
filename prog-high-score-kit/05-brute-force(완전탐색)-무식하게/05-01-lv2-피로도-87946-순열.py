# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
유저의 현재 피로도 k와 
각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons가 매개변수로 주어질 때, 
유저가 탐험할수 있는 최대 던전 수를 return

입력#1
k        : 80
dungeons : [[80, 20], [50, 40], [30, 10]]

출력#1
3

입출력 예 설명#1
첫 번째 → 두 번째 → 세 번째 던전 순서로 탐험한다면 2번밖에 못함
첫 번째 → 세 번째 → 두 번째 던전 순서로 탐험한다면 3번 가능
"""

# 던전 입장 조건 : 피로도 >= 최소 피로도, 던전 입장 후 : 피로도 -= 소모 피로도
# 최소 피로도 >= 소모 피로도
# 최대한 많이 탐험 -> 각 던전은 한번만 가능
# 가능한 경우의 수 : 8! : 40320 -> 완전 탐색으로도 풀 수 있음
from itertools import permutations


def solution(k, dungeons):
    dun_cnt_list = []
    # 방문 순서 확인
    for perm in permutations(range(len(dungeons)), len(dungeons)):
        # 피로도, 방문 수 초기화
        temp_k = k
        dun_cnt = 0
        # 던전 방문
        for i in perm:
            need_k, use_k = dungeons[i]
            # 방문 가능한 경우
            if temp_k >= need_k:
                dun_cnt += 1
                temp_k -= use_k
        # 방문한 던전의 수
        dun_cnt_list.append(dun_cnt)
    # 최대 방문 횟수
    return max(dun_cnt_list)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
