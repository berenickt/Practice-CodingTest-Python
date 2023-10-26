# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""
조이스틱으로 알파벳 이름을 완성하세요.
맨 처음엔 A로만 이루어져 있습니다.
e.g.) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.
▲ - 다음 알파벳
▼ - 이전 알파벳
    (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 
    (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 
    (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)

만들고자 하는 이름 name이 매개변수로 주어질 때,
이름에 대해 조이스틱 조작 횟수의 최솟값을 return

입력 #1
"JEROEN"

출력 #1
56

cf. 
Greedy에 속해있는 문제지만 22년 1월 테스트케이스가 추가되면서
완전탐색( Brute Force ) 문제에 가까워짐

cf. 
A로만 이루어진 상태에서 문자열을 찾는 것이기 때문에 
마지막에 남은 문자열들이 연속된 A로 이루어져 있다면 이동하지 않고 문자열을 완성 가능

cf. 파란색 화살표 대로 왼쪽에서 오른쪽으로만 이동하는 경우
문자열 길이에서 1을 뺀만큼 이동

cf. 빨간색 화살표 대로 이동하는 경우
- 우선 A가 나오기 전까지 왼쪽에서 오른쪽으로 이동(1)
- 하다가 A를 마주치면 온만큼 되돌아 감(2)
- 그다음 문자열의 끝으로 돌아서 A가 나오기 전까지 이동(3)
"""


def solution(name):
    # 알파벳 변경 횟수( 상하 이동 )
    spell_move = 0

    # 커서 이동 횟수, 이름의 길이 - 1( 좌우 이동 )
    cursor_move = len(name) - 1

    for i, spell in enumerate(name):
        # 알파벳 변경 횟수, 위아래 중 최소 이동 값 ( 상하 이동 )
        ASCII_Sp_to_A = ord(spell) - ord("A")
        ASCII_Z_to_Sp = ord("Z") - ord(spell) + 1
        spell_move += min(ASCII_Sp_to_A, ASCII_Z_to_Sp)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min(
            [cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)]
        )

    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )
    return spell_move + cursor_move


print(solution("JEROEN"))
