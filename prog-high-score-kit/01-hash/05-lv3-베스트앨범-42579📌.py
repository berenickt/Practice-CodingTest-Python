# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
노래의 장르를 나타내는 문자열 배열 genres와
노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return

1. 노래 장르별 총 재생 횟수를 계산하기 위해 딕셔너리를 만든다. 
(key:노래장르, value:총 재생횟수)

2. 노래 장르별 재생횟수와 인덱스를 딕셔너리로 만든다. 
(key:노래장르, value:(인덱스, 재생횟수)) => 3번 조건

3. for문으로 이전에 만든 딕셔너리의 value 값을 채운다.
4. 노래 장르별 총 재생횟수를 내림차순으로 정렬하여 장르에 대해 
재생횟수가 큰 2개의 항목을 가져와 정답값에 반환한다.

입력 #1
genres : ["classic", "pop", "classic", "classic", "pop"]
plays  : [500, 600, 150, 800, 2500]

출력 #1
[4, 1, 3, 0]

cf. enumerate : 인덱스와 원소를 동시에 접근
cf. zip : 두 배열 합치기
cf. `lambda 매개변수 : 표현식`
>>> (lambda x, y: x + y)(10, 20)
30
"""


def solution(genres, plays):
    answer = []

    # 노래 장르별 재생횟수 및 인덱스 딕셔너리
    top_index = {g: [] for g in genres}
    # 노래 장르별 총 재생 횟수 딕셔너리
    top_play = {g: 0 for g in genres}

    # 딕셔너리의 value 값을 채움
    for i, (g, p) in enumerate(zip(genres, plays)):
        top_play[g] += p
        top_index[g].append((i, p))

    # 노래 장르별 총 재생 횟수를 내림차순으로 정렬
    for k, v in sorted(top_play.items(), key=lambda x: x[1], reverse=True):
        # 노래 장르에 대해 재생횟수가 높은 항목 2개 가져옴
        for i, p in sorted(top_index[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
