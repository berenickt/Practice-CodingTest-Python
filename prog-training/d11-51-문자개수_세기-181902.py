# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181902
"""
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, 
my_string에서 'B'의 개수,..., 
my_string에서 'Z'의 개수, 
my_string에서 'a'의 개수, 
my_string에서 'b'의 개수,..., 
my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return

입력#1
"Programmers"

출력#1
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]

📌 ord(문자)
하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
ord('a')를 넣으면 정수 97을 반환
a~z 문자는 97~122 숫자로 반홤됨

📌 chr(정수)
하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
"""


def solution(my_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    dic = {k: 0 for k in alphabet}
    for str in my_string:
        dic[str] += 1
    return [v for v in dic.values()]


print(solution("Programmers"))
