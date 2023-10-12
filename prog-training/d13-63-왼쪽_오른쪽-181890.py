# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181890
"""
문자열 리스트 str_list에는 
"u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
str_list에서 "l"과 "r" 중 

먼저 나오는 문자열이 "l"이라면
해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 

먼저 나오는 문자열이 "r"이라면
해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return

"l"이나 "r"이 없다면 빈 리스트를 return

입력#1
["u", "u", "l", "r"]

출력#1
["u", "u"]
"""


def solution(str_list):
    # l, r 모두 없다면
    if ("l" not in str_list) and ("r" not in str_list):
        return []

    # l, r 모두 존재
    elif ("l" in str_list) and ("r" in str_list):
        # l이 먼저오는 경우
        if str_list.index("l") < str_list.index("r"):
            return str_list[: str_list.index("l")]
        return str_list[str_list.index("r") + 1 :]

    # l이 존재하는 경우와 그 외의 경우(r만 존재하는 경우)
    elif "l" in str_list:
        return str_list[: str_list.index("l")]
    return str_list[str_list.index("r") + 1 :]


print(solution(["u", "u", "l", "r"]))


def solution2(str_list):
    for idx, el in enumerate(str_list):
        if el == "l":
            return str_list[:idx]
        elif el == "r":
            return str_list[idx + 1 :]
    return []
