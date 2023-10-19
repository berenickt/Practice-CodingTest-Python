# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어  | 수신 탑(높이)
I숫자  	| 큐에 주어진 숫자를 삽입합니다.
D 1	    | 큐에서 최댓값을 삭제합니다.
D -1	  | 큐에서 최솟값을 삭제합니다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
모든 연산을 처리한 후 큐가 비어있으면 [0,0]
비어있지 않으면 [최댓값, 최솟값]을 return

입력 #1
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

출력 #1
[0, 0]
"""
import heapq


def solution(operations):
    answer = []

    q = []
    for operation in operations:
        x, num = operation.split()
        num = int(num)

        if x == "I":
            heapq.heappush(q, num)
        elif x == "D" and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value)
        else:
            if len(q) != 0:
                heapq.heappop(q)

    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [max(q), heapq.heappop(q)]

    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
