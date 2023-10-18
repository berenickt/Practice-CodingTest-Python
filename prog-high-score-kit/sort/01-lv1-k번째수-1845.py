# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

e.g. array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return

입력 #1
array   : [1, 5, 2, 6, 3, 7, 4]	
command : [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

출력 #1
[5, 6, 3]

입출력 설명 #1
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. 
[2, 3, 5, 6]의 세 번째 숫자는 5
"""


def solution(array, commands):
    answer = []

    for command in commands:
        # 📌 아래처럼 선언해도 가능함
        # i, j, k = command
        i = command[0]
        j = command[1]
        k = command[2]

        # 범위에 맞게 자르고 정렬 후 k번째 수 구하기
        a = sorted(array[i - 1 : j])
        answer.append(a[k - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
