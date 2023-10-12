# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181866
"""
문자열 myString이 주어집니다.
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return
단, 빈 문자열은 반환할 배열에 넣지 않습니다.


입력#1
"axbxcxdx"

출력#1
['a', 'b', 'c', 'd']

📌 cf. filter(조건 함수, 순회 가능한 데이터)
두 번째 인자로 넘어온 데이터 중에서 첫 번째 인자로 넘어온 조건 함수를 만족하는 데이터만 찾아서 반환
"""


def solution(myString):
    l = filter(None, myString.split("x"))  # e.g.1) ['a', 'b', 'c', 'd', '']
    return sorted(l)


print(solution("axbxcxdx"))
