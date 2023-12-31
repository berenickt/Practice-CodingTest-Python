"""그리디(greedy) 알고리즘
1. 최종 해답을 찾기 위해 각 단계마다 하나의 답을 고름
2. 각 단계에서 답을 고를 때 가장 좋아 보이는 답을 선택
3. 선택할 당시 최적의 답을 고르지만, 최종 해답이 반드시 최적임을 보증하지 않음

앞으로 다루게 될 알고리즘과 다르게 
사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형
다익스트라 알고리즘 같은 특이 케이스는 제외

보통 코딩테스트에서 출제되는 그리디 알고리즘 유형의 문제는 창의력 
즉, 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구

문제에서 가장 큰 순서대로, 가장 작은 순서대로와 같은 기준을 알게 모르게 제시해줌
이러한 문제는 정렬을 사용하면 만족시킬 수 있으므로, 
자주 정렬 알고리즘과 짝을 이뤄 출제
"""

"""
거스름 돈 문제를 예를 들면, 간단한 아이디어만 떠올릴 수 있으면 문제를 해결할 수 있다.
가장 큰 화폐 단위부터 돈을 거슬러주는 것이다.

N원을 거슬러줘야한다고 가정하면,
가장 큰 단위인 500원, 100원... 차례로 거슬러주면 
최소의 동전개수로 모두 거슬러 줄 수 있다.

N=1,260이라고 하면 500원 2개, 100원 2개, 50원 1개, 10원 1개로 
최소한의 동전으로 거스를 수 있다.
"""
n = 1260
# 큰 단위의 화폐부터 차례대로 확인하기
coin_array = [500, 100, 50, 10]
count = 0

# count: n을 coin으로 나눈 몫
# `n`을 `coin`으로 나눈 나머지를 0이될때까지 지속함
for coin in coin_array:
    count = count + n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n = n % coin

print(count)  # 👉🏽 6

"""
코드를 보면 화폐의 단위만큼 반복수행해야하므로 시간복잡도는 O(K)이다.
또, 거슬러줘야 할 돈 N은 찾아 볼 수 없는것을 알 수 있는데, 
이 알고리즘의 시간 복잡도는 동전의 총 종류에만 영향을 받고, 
거슬러줘야 하는 금액의 크기와는 무관하다는 것을 알 수 있다.

그리디 알고리즘의 또 다른 특징은 해법이 정당한지 검토해야하는데, 
거스름돈문제를 그리디 알고리즘으로 풀 수 있는 이유는 가지고 있는 동전 중 
큰 단위가 항상 작은 단위의 배수이므로 
작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.

예를 들어, 동전의 화폐 단위가 500원, 400원, 100원일 경우를 생각해보자.
그리디 알고리즘으로는 4개의 동전(500원 1, 100원 3)을 거슬러줘야하지만, 
최적의 해는 2개의 동전(400원 * 2)을 거슬러 주는 것이다.

아이디어까지는 동일하다는 점에서 정당하다.
이처럼 최소한의 아이디어를 떠올리고 
이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.

만약 어떤 코딩테스트를 만났을 때, 
바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심해보고, 
문제를 해결 할 수 있는 탐욕적인 해결법이 존재하는지 참고해보자. 
그래도 찾기 어렵다면, 
그때는 다이나믹 프로그래밍이나 
그래프 알고리즘 등으로 문제를 해결할수있는지 재차 고민해보자.

마지막으로 거스름돈 문제에서 동전(화폐)의 단위가 서로 배수의 형태가 아니라, 
무작위로 주어진 경우에는 그리디 알고리즘으로 해결할 수 없다.
이때는 다이나믹 프로그래밍으로 해결 할 수 있으며 이는 뒤에서 배우기로 하자.
"""
