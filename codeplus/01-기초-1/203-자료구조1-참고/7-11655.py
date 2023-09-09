# 💡 ROT13 📚 https://www.acmicpc.net/problem/11655
'''
입력된 문자열을 ROT13 암호화 방식으로 변환하여 출력하는 코드
'''
import sys


# 문자열을 ROT13 암호화하는 함수를 정의
def rot13(s):
    ans = ''  # 결과 문자열을 초기화

    # 문자열의 각 문자를 처리
    for ch in s:
        # 문자의 아스키 코드에 13을 더하여 ROT13을 수행
        if 'a' <= ch <= 'm' or 'A' <= ch <= 'M':
            ans += chr(ord(ch)+13)
        # 문자의 아스키 코드에서 13을 빼서 ROT13을 수행
        elif 'n' <= ch <= 'z' or 'N' <= ch <= 'Z':
            ans += chr(ord(ch)-13)
        # 알파벳이 아닌 경우, 그대로 결과에 추가
        else:
            ans += ch

    return ans  # ROT13으로 암호화된 결과를 반환


# 입력된 문자열을 ROT13으로 암호화하여 출력
print(rot13(sys.stdin.readline()))
