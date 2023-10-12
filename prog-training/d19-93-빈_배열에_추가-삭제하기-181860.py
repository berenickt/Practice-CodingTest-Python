# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181860
"""
아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때,
flag를 차례대로 순회하며 
flag[i]가 True라면 X의 뒤에 arr[i]를 arr[i] x 2 번 추가하고,
flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return

입력#1
arr  : [3, 2, 4, 1, 3]
flag : [True, False, True, False, False]

출력#1
[3, 3, 3, 3, 4, 4, 4, 4]
"""


def solution(arr, flag):
    li = []
    for idx, bol in zip(arr, flag):
        if bol:
            for _ in range(idx):
                li.append(idx)
                li.append(idx)
        else:
            li = li[:-idx]
    return li


print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))


##############################
def solution2(arr, flag):
    li = []
    for idx, bol in zip(arr, flag):
        if bol:
            li += [idx] * idx * 2
        else:
            li = li[:-idx]
    return li
