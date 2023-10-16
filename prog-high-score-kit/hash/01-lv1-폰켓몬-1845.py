# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""
주어진 폰켓몬 개수의 반만 가져갈 수 있다.
폰켄몬 종류 개수의 최댓값만 반환하면 된다.

1. 최대로 가져갈 수 있는 폰켄몬 수를 구한다. (=get_num)
2. 주어진 폰켄몬 종류를 중복 제거하여 종류가 몇 개인지 확인한다.
3. 만약, 중복 제거 수가 get_num 보다 같거나 작으면 중복 제거 수를 반환한다.
4. 만약, 중복 제거 수가 get_num 보다 크면 get_num을 반환한다.

입력 #1
[3,1,2,3]

출력 #1
2
"""


def solution(nums):
    # 1. 가질 수 있는 최대 포켓몬 수
    get_num = int(len(nums) / 2)

    # 2. 중복 제거하였을 때, 종류가 몇 개인지 확인
    set_nums = set(nums)
    set_num = len(set_nums)

    ### 폰켓몬 종류 수의 최댓값을 0으로 설정
    answer = 0

    # 3. 폰켄몬 가져갈 수 있는 수 >= 폰켄몬 종류 개수
    if get_num >= set_num:
        answer = set_num
    # 4. 폰켄몬 가져갈 수 있는 수 < 폰켄몬 종류 수
    else:
        answer = get_num

    return answer


print(solution([3, 1, 2, 3]))


#################################
def solution2(ls):
    return min(len(ls) / 2, len(set(ls)))
