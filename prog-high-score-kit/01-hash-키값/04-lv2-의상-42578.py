# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때,
서로 다른 옷의 조합의 수를 return

의상 종류가 다 같으면 조합할 수 있는 수는 스파이가 가진 의상 수 이다.

1. clothes 에 있는 모든 리스트 중 [1]번 인덱스에 있는 값들을 가져와 새로운 리스트로 만든다. 
(type_clothes)

2. type_clothes 를 set (집합 자료형) 을 통해 중복 제거하여 
종류의 개수를 변수 (type_num) 에 할당한다.

3. 만약, type_num 이 1이라면 len(clothes)을 정답값으로 반환한다.
4. 만약, type_num 이 1이 아니라면 !
5. type_clothes 에 의상 종류 값을 새로운 딕셔너리의 key 값으로 만들고, 
value는 0으로 설정해 둔다.

6. clothes 에 있는 요소들 중 의상의 종류가 dict의 키 값과 같으면 
해당 value의 값에 +1 처리해 준다.

7. 마지막으로, type_num 만큼 반복문을 돌리고 조합이 가능한 경우의 수를 구한다.
e.g.) 얼굴 - 2개, 의상 - 3개 
    => 한 개씩 착용 = 5, 
    두 개씩 착용 : 2*3 = 6 ==> 총 11가지의 경우의 수
적용) 얼굴 -2개, 의상 - 3개 => (2+1)*(3+1)-1 = 11개 (착용하는 경우와 착용하지 않는 경우)

입력 #1
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

출력 #1
5
"""


def solution(clothes):
    answer = 1

    # 의상 종류의 개수 가져오기
    type_clothes = [x[1] for x in clothes]
    type_num = len(set(type_clothes))

    # 의상 종류를 key값으로, 종류에 대한 값을 values로 가져오기
    dict_clothes = {}

    # 만약, 의상 종류가 1개라면 clothes 길이를 반환하기
    if type_num == 1:
        return len(clothes)
    else:
        # 딕셔너리의 키값 저장하고, 개수를 0으로 임의 설정하기
        for i in type_clothes:
            dict_clothes[i] = 0
        # clothes 의 의상종류가 딕셔너리의 키값과 같다면 개수를 늘리기
        for c in clothes:
            dict_clothes[c[1]] += 1
        # 의상 종류별 개수에 대해 경우의 수 만들기
        for val in dict_clothes.values():
            answer *= val + 1

        return answer - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)
