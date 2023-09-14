# 💡 암호 만들기 📚 https://www.acmicpc.net/problem/1759
def check(password):
    ja = 0
    mo = 0

    # 패스워드 문자열에서 자음과 모음을 세는 함수
    for x in password:
        if x in "aeiou":
            mo += 1
        else:
            ja += 1

    # 자음이 2개 이상이고 모음이 1개 이상인 경우 True를 반환
    return ja >= 2 and mo >= 1


def go(n, alpha, password, i):
    # 패스워드의 길이가 n과 같으면 검사 함수를 호출하고 결과를 출력
    if len(password) == n:
        if check(password):
            print(password)
        return

    # 아직 패스워드를 구성 중인 경우, 현재 알파벳을 사용하거나 사용하지 않는 두 가지 경우를 고려
    if i == len(alpha):
        return

    # 현재 알파벳을 사용하는 경우
    go(n, alpha, password + alpha[i], i + 1)

    # 현재 알파벳을 사용하지 않는 경우
    go(n, alpha, password, i + 1)


n, m = map(int, input().split())
a = input().split()
a.sort()

# 패스워드를 구성하기 위한 함수 호출
go(n, a, "", 0)
