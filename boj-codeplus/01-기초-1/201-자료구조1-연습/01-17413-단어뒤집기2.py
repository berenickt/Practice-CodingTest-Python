# 💡 단어 뒤집기2 📚 https://www.acmicpc.net/problem/17413  --- 스택
"""
태그는 뒤집지 않고, 단어만 뒤집는 프로그램

📌 isalnum() : 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드
📌 len()     : 문자열의 길이 반환하는 함수, 
(cf. 한글도 1로, 공백도 1로 처리함)
(cf. 리스트나 튜플 등에서는 그 안에 속한 값의 개수를 반환)

e.g.)
len( "한글과 공백" )                  # 6
len( [ 11, 22, 33, 44, 55, 66 ] )  # 6
"""
import sys

# 입력받은 문자열을 리스트로 변환하여 처리
word = list(sys.stdin.readline().rstrip())

# 인덱스와 시작 위치 변수를 초기화
i = 0
start = 0

# 문자열의 끝까지 반복하며 처리
while i < len(word):
    # 만약 현재 문자가 "<"이라면,
    if word[i] == "<":
        i += 1
        # "<" 다음 문자부터 ">"를 찾을 때까지 인덱스를 증가
        while word[i] != ">":
            i += 1
        # ">"를 찾으면 인덱스를 한 번 더 증가시켜서 ">"를 건너뜀
        i += 1

    # 현재 문자가 알파벳이나 숫자라면,
    elif word[i].isalnum():
        start = i
        # 현재 문자부터 연속된 알파벳이나 숫자를 찾을 때까지 인덱스를 증가
        while i < len(word) and word[i].isalnum():
            i += 1
        # 단어를 임시 변수에 저장하고 뒤집습니다.
        temp = word[start:i]
        temp.reverse()
        # 원래 위치에 뒤집은 단어를 다시 저장합니다.
        word[start:i] = temp

    # 현재 문자가 특수 문자나 공백이라면,
    else:
        i += 1

# 리스트의 문자들을 합쳐서 출력합니다.
print("".join(word))
