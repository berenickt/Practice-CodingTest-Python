# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181931
"""
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return
"""
# 📌 enumerate() : 인덱스(index)와 원소를 동시에 접근하면서 루프를 돌리기


def solution1(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer


def solution2(a, d, included):
    return sum(a + idx * d for idx, bol in enumerate(included) if bol)
