# 💡 접미사 배열 📚 https://www.acmicpc.net/problem/11656
"""
입력된 문자열의 접미사들을 사전순으로 정렬하여 출력하는 코드

이상:미만:간격
[i:] i이상
"""
str = input()  # 문자열을 입력받음
strLength = len(str)

# 접미사(suffix)들을 저장할 리스트를 생성
# 0~7(i) 8번 순회, 그 값을 접미사(suffix) 리스트에 저장
# suffixs: ['baekjoon', 'aekjoon', 'ekjoon', 'kjoon', 'joon', 'oon', 'on', 'n']
suffixs = [str[i:] for i in range(strLength)]

# 접미사들을 사전순으로 정렬
suffixs.sort()

print("\n".join(suffixs))  # 각 접미사들을 개행 문자로 연결하여 출력
