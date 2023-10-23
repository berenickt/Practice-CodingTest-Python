# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때,
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return

cf.
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

입력 #1
begin  : "hit"
target : "cog"
words  : ["hot", "dot", "dog", "lot", "log", "cog"]

출력 #1
4
"""

from collections import deque


# 최소 단계를 찾아야 하므로 bfs
def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])  # 시작 단어와 단계 0으로 초기화

    while queue:
        now, step = queue.popleft()
        if now == target:
            return step

        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)):  # 단어의 길이만큼 반복하여
                if now[i] != word[i]:  # 단어에 알파벳 한개씩 체크하기
                    count += 1

            if count == 1:
                queue.append([word, step + 1])


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
