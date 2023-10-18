# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/12906
"""
배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 

예를 들면,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return

입력 #1
[1, 1, 3, 3, 0, 1, 1]

출력 #1
[1, 3, 0, 1]

Pseudo-Code
1. 주어지는 배열은 중복된 값이 있다면 붙어있다.
2. 0~9 사이의 값만 존재한다는 점을 이용해 변수에 10을 기본값으로 설정한다.
3. 이전 값을 변수에 계속 할당하여 이전값과 현재값이 같으면 패스하고, 같지않으면 리스트에 넣는다.
4. 위 과정을 통해 연속되는 값을 1개만 불러온다.
"""


def solution(arr):
    answer = []
    max = 10

    for num in arr:
        if max != num:
            answer.append(num)
        max = num

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))


####빈 배열 만들고 [0] 인덱스 넣어준 후
# 그 다음 숫자부터는 전 인덱스랑 비교해서 다르면 새 열에 넣어주기.
def solution2(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer


####빈 비열를 만들어주고 거기에 비교해서 없으면 하나씩 넣어주기.
def solution3(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)
    return answer
