# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return

입력 #1
[1,2,3,4,5]

출력 #1
[1]
"""


def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            score[0] += 1
        if answers[i] == student2[i % 8]:
            score[1] += 1
        if answers[i] == student3[i % 10]:
            score[2] += 1

    for idx, num in enumerate(score):
        if num == max(score):
            answer.append(idx + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))
