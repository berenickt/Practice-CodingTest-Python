# 📚 https://www.acmicpc.net/problem/1759
"""
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
최소 한 개의 모음(a, e, i, o, u)과 
최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 

또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 
암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 
암호를 추측해 보려고 한다. 

C개의 문자들이 모두 주어졌을 때, 
가능성 있는 암호들을 모두 구하는 프로그램

첫째 줄에 두 정수 L, C가 주어진다. (L: 서로 다른 L개 알파벳 소문자, C : 입력받는 개수)
다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다

input #1
4 6
a t c i s w
"""
from itertools import combinations


vowels = ("a", "e", "i", "o", "u")  # 5개의 모음 정의
L_alpabet_cnt, C_input_cnt = map(int, input().split(" "))

### 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
array = input().split(" ")
array.sort()
# testcase #1 : array === ['a', 'c', 'i', 's', 't', 'w']

### 길이가 L_alpabet_cnt인 모든 암호 조합을 확인
for password in combinations(array, L_alpabet_cnt):
    ## 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    vowel_cnt = 0
    for i in password:  # testcase #1 : password ('a', 'c', 'i', 's')
        if i in vowels:  # testcase #1 : vowel ('a', 'e', 'i', 'o', 'u')
            vowel_cnt += 1
    ## 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if vowel_cnt >= 1 and vowel_cnt <= L_alpabet_cnt - 2:
        print("".join(password))
