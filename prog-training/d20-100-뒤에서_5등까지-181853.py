# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181853
"""
정수로 이루어진 리스트 num_list가 주어집니다.
num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return

입력#1
[12, 4, 15, 46, 38, 1, 14]

출력#1
[1, 4, 12, 14, 15]
"""


# 오름차순으로 정렬시키고, idx 0~4까지 return
def solution(num_list):
    return sorted(num_list)[:5]


print(solution([12, 4, 15, 46, 38, 1, 14]))
