# 💡 알파벳 찾기 📚 https://www.acmicpc.net/problem/10809
str = input()  # 입력으로 문자열을 받음

# 알파벳 소문자의 개수만큼 순회
for i in range(26):
    # 현재 알파벳 소문자를 chr 함수를 사용하여 구함
    char = chr(i + ord("a"))

    # 현재 알파벳 소문자가 문자열 내에서 처음으로 등장하는 위치를 찾고 출력
    # 존재하지 않으면 -1을 출력합니다.
    print(str.find(char), end=" ")
