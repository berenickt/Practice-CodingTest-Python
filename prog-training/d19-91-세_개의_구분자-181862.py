# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181862
"""
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.
e.g. 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 
문자열을 순서대로 저장한 배열을 return

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며,
return할 배열이 빈 배열이라면 ["EMPTY"]를 return

입력#1
"baconlettucetomato"

출력#1
["onlettu", "etom", "to"]

📌 cf. sub()
문자열에서 특정 문자 혹은 문자열을 다른 문자 혹은 문자열로 바꾸는 함수

📌 cf. strip()
문자열의 앞과 뒤에 있는 공백을 제거하는 함수
"""
import re


def solution(myStr):
    # a, b, c를 공백으로 치환 후, 앞뒤 공백 제거
    myStr = re.sub("a|b|c", " ", myStr).strip()

    # 구분자 사이에 문자열이 있으면, 문자열을 나누어 리스트로 반환
    return myStr.split() if len(myStr) > 0 else ["EMPTY"]


print(solution("baconlettucetomato"))
