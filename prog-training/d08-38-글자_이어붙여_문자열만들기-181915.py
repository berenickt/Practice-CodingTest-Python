# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181915
"""
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 
이어 붙인 문자열을 return 

입력#1
"cvsgiorszzzmrpaqpe"
[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]

출력#1
"programmers"
"""


def solution(my_string, index_list):
    answer = ""
    for i in index_list:
        answer += my_string[i]
    return answer


print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
