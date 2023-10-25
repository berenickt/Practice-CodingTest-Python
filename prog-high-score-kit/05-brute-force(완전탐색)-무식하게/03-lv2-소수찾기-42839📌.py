# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
종이 조각으로 만들 수 있는 소수가 몇 개인지 return

입력#1
"17"

출력#1
3

입출력 예 설명#1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
"""


# 1. 결과물을 담고 있을 primeSet 정의
prime_set = set()


def isPrime(number):
    # 6. 0과 1은 False
    if number in (0, 1):
        return False

    # 7. 에라토스테네스의 체
    lim = int(number**0.5 + 1)
    for i in range(2, lim):
        if number % i == 0:
            return False

    return True


def makeCombinations(combination, others):
    # 5. 탈출 조건 / 비교 조건 : 지금까지 만들어진 조합을
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))

    # 4. 현재까지 만들어진 숫자에, 남아있는 숫자 중 하나를 붙여서 조합을 만든다
    for i in range(len(others)):
        makeCombinations(combination + others[i], others[:i] + others[i + 1 :])


def solution(numbers):
    # 2. 모든 조합을 만드는 recursive 함수를 수행한다.
    makeCombinations("", numbers)

    # 3. primeSet의 length를 반환해준다.
    return len(prime_set)


print(solution("17"))  # 3
