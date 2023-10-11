# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181904
"""
문자열 my_string과 두 정수 m, c가 주어집니다.
my_string을 한 줄에 m 글자씩 가로로 적었을 때, 
왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return

입력#1
my_string : "ihrhbakrfpndopljhygc"
m         : 4
c         : 2

출력#1
"happy"
"""


def solution(my_string, m, c):
    l = []
    answer = []
    # 문자열 분해 과정
    for _ in range(len(my_string) // m):
        l.append(my_string[:m])
        my_string = my_string[m:]

    # 특정 열에 위치한 문자열만 가져오는 과정
    for j in l:
        answer.append(j[c - 1])

    return "".join(answer)


print(solution("Progra21Sremm3", 6, 12))


###############################
def solution2(my_string, m, c):
    return my_string[c - 1 :: m]
