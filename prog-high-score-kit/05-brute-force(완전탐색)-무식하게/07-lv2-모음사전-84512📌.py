# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/84512
"""
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 
길이 5 이하의 모든 단어가 수록되어 있습니다.
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 
마지막 단어는 "UUUUU"이다.

단어 하나 word가 매개변수로 주어질 때,
이 단어가 사전에서 몇 번째 단어인지 return

입력#1
"AAAAE"

출력#1
6

입출력 예 설명#1
사전에서 첫 번째 단어는 "A"이고, 
그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다

풀이
1. 모음단어 만들기
2. 정렬
3. 매개변수의 인덱스 반환
"""
from itertools import product


def solution(word):
    answer = []
    li = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for per in product(li, repeat=i):
            answer.append("".join(per))
    answer.sort()
    return answer.index(word) + 1


print(solution("AAAAE"))
