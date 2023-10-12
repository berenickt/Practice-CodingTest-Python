# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181858
"""
랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다.
적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후,
지금까지 나온적이 없는 수이면, 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.

이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고,
실제 만들어질 길이 k의 배열을 예상해봅시다.

정수 배열 arr가 주어집니다. 
문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return

단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return

입력#1
arr : [0, 1, 1, 2, 2, 3]
k   : 3

출력#1
[0, 1, 2]
"""


def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    while len(answer) < k:
        answer.append(-1)
    return answer[:k]


print(solution([0, 1, 1, 2, 2, 3], 3))

"""
set으로 중복된 숫자를 제거하지 않은 이유는 배열의 순서가 무너질 수 있기 때문이다.
arr을 set으로 중복제거하여 다시 list로 변환하는 과정에서 이전의 배열이 무너질 수 있기 때문
"""
