# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중,
h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면,
h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return

입력 #1
[3, 0, 6, 1, 5]

출력 #1
3

입출력 예 설명 #1
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3

Pseudo-Code
1. 인용횟수가 담긴 리스트를 내림차순으로 정렬한다. [6, 5, 3, 1, 0]
2. 정렬한 리스트를 for문으로 돌리는데 enumerate로 index값과 요소를 같이 가져올 수 있도록 한다.
3. index값이 리스트 내 인용횟수보다 큰 경우, index값을 반환한다.
4. 만약 index값이 인용횟수보다 큰 경우가 없다면 리스트의 개수를 반환한다
"""


def solution(citations):
    des_order = sorted(citations, reverse=True)
    for i, el in enumerate(des_order):
        if i >= el:
            return i
    return len(citations)


print(solution([3, 0, 6, 1, 5]))
