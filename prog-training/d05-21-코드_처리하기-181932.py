# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181932
"""
문자열 code가 주어집니다.
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다.
mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

mode가 0일 때
  code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
  code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
mode가 1일 때
  code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
  code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.

문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수
단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return
"""
"""
인덱스(index)와 원소를 동시에 접근하면서 루프를 돌리려면?
📌 enumerate() : for 문의 in 뒷 부분을 enumerate() 함수로 한 번 감싸주면 됨

📌 enumerate() 시작 인덱스 변경
for i, letter in enumerate(['A', 'B', 'C'], start=101):
  print(i, letter)

출력결과
101 A
102 B
103 C
"""


def solution1(code):
    return "".join(code.split("1"))[::2] or "EMPTY"


def solution2(code):
    answer = ""
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            mode ^= 1  # XOR(^) 연산자를 사용하여 토글, 즉, 0에서 1로, 또는 1에서 0으로 변경
        else:
            if i % 2 == mode:
                answer += code[i]
    return answer if answer else "EMPTY"


def solution3(code):
    mode = False
    ret = ""
    for index, char in enumerate(code):
        if char == "1":
            mode = not mode
        else:
            ret += char if index % 2 == int(mode) else ""
    return ret if len(ret) else "EMPTY"
