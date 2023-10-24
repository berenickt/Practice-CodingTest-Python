# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
전화번호부에 있는 요소들을 정렬하였을 때,
첫 번째 값만 접두사가 되는 것이 아니다.

1. 전화번호부에 있는 요소는 정렬되어있지 않기 때문에 sort로 순서를 정렬
2. for문으로 i번째 값과 i+1번째 값의 길이가 다른 경우, 
    i+1 값을 i 값의 길이로 슬라이싱하여 같은 지를 확인
3. 같으면 False 를 변수에 할당하고, 반복문을 종료

입력 #1
["119", "97674223", "1195524421"]

출력 #1
false
"""


def solution(phone_book):
    # 순서 정렬하여 접두사가 0번 위치에 있도록 설정
    phone_book = sorted(phone_book)

    # 접두사를 제외한 나머지 번호에서 접두사가 포함되었는지 확인
    answer = True

    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1][: len(phone_book[i])] == phone_book[i]:
                answer = False
                break

    return answer


print(solution(["119", "97674223", "1195524421"]))


#### startswith() : 문자열이 특정 문자열로 시작하는지 확인
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
