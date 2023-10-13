# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181834
"""
알파벳 소문자로 이루어진 문자열 myString이 주어집니다.
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return

입력#1
"abcdevwxyz"

출력#1
"lllllvwxyz"

입출력 예#1
0 ~ 4번 인덱스의 문자 "a","b","c","d","e"는 각각 "l"보다 앞서는 문자입니다. 따라서 "l"로 고쳐줍니다.
그 외의 문자는 모두 "l"보다 앞서지 않는 문자입니다. 따라서 바꾸지 않습니다.
따라서 "lllllvwxyz"을 return
"""


def solution(myString):
    answer = ""
    for s in myString:
        if s < "l":
            answer += "l"
        else:
            answer += s
    return answer


print(solution("abcdevwxyz"))


################################
def solution2(myString):
    answer = [s if s > "l" else "l" for s in myString]
    return "".join(answer)
