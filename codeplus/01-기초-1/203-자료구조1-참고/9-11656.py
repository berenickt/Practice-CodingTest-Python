# 💡 접미사 배열 📚 https://www.acmicpc.net/problem/11656
'''
입력된 문자열의 접미사들을 사전순으로 정렬하여 출력하는 코드
'''
s = input()                   # 문자열을 입력받습니다
n = len(s)                    # 입력된 문자열의 길이를 구함
a = [s[i:] for i in range(n)]  # 접미사들을 저장할 리스트를 생성
a.sort()                      # 접미사들을 사전순으로 정렬
print('\n'.join(a))           # 각 접미사들을 개행 문자로 연결하여 출력
