# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""
0 또는 양의 정수가 주어졌을 때,
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면,
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return

입력 #1
[6, 10, 2]

출력 #1
"6210"

📌 cf. `lambda 매개변수 : 표현식`
>>> (lambda x, y: x + y)(10, 20)
30

📌 cf. sotred(정렬하고자 하는 리스트 개수, key매개변수(어떤 값을 기준으로 정렬할지), reverse = False)
'어떤 값을 기준으로 정렬할지' 에 해당하는 key 매개변수를 선언할 때  lambda 함수가 많이 사용되는 편

📌 lambda 함수란? 
파이썬에 존재하는 특이한 문법으로 임시로 만드는 함수를 의미합니다.
한 번 사용하고 버리는 일회용 함수같은 느낌
"""


def solution(numbers):
    # 숫자를 문자열로 바꿔줌
    number = [str(num) for num in numbers]

    # 원소 범위 0 이상 1000 이하, 3자리수 처리
    # 만약, 앞자리가 같은 문자가 있다면 명확한 순서 비교를 위해 3자리수 처리
    # ex 10, 1 => 101010 111 => 111이 먼저올 수 있게 처리
    number = sorted(number, key=lambda x: x * 3, reverse=True)

    # int -> str 이유 : 0으로만 구성되는 경우, 0 하나만 반환되도록 설정
    return str(int("".join(number)))
