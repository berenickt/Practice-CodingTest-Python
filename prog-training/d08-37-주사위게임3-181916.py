# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181916
"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

(1) 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 x p점을 얻습니다.
(2) 세 주사위에서 나온 숫자가 p로 같고 
    나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 x p + q)2 점을 얻습니다.
(3) 주사위가 두 개씩 같은 값이 나오고, 
    나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) x |p - q|점을 얻습니다.
(4) 어느 두 주사위에서 나온 숫자가 p로 같고 
    나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q x r점을 얻습니다.
(5) 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 
정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return

입력#1
2	2	2	2	

출력#1
2222

입출력 예 #1
예제 1번에서 네 주사위 숫자가 모두 2로 같으므로 1111 x 2 = 2222점을 얻습니다. 
"""


def solution(a, b, c, d):
    answer = 0
    dic = {k: 0 for k in [a, b, c, d]}  # key : 0형태로 딕셔너리 생성
    keys = list(dic.keys())

    # 딕셔너리에 키별로 value 입력
    for k in [a, b, c, d]:
        dic[k] += 1

    # 딕셔너리 value 값을 기준으로 오름차순 정렬
    reverse_dic = {v: k for k, v in dic.items()}

    # (1) 네 주사위 숫자가 모두 동일
    if len(keys) == 1:
        answer = 1111 * a

    elif len(keys) == 2:
        # (2) 주사위의 숫자가 3, 1 개씩 동일
        if max(dic.values()) == 3:
            answer = (10 * reverse_dic[3] + reverse_dic[1]) ** 2
        # (3) 주사위의 숫자가 2, 2 개씩 동일
        else:
            answer = (keys[0] + keys[1]) * abs(keys[0] - keys[1])

    # (4) 주사위의 숫자가 2, 1, 1 인 경우
    elif len(keys) == 3:
        condition_list = [k for k, v in dic.items() if v == 1]
        answer = condition_list[0] * condition_list[1]

    # (5) 주사위의 숫자가 모두 다른 경우
    else:
        answer = min([a, b, c, d])

    return answer


# print(solution(2, 2, 2, 2))
print(solution(6, 3, 3, 6))
