# 성적 구간에 따른 학점 정보 출력코드
score = 85

if score >= 90:
    print("성적은 90이상입니다.")
elif score >= 80:
    print("성적은 80이상입니다.")
elif score >= 70:
    print("성적은 70이상입니다.")
else:
    print("성적은 70이하입니다.")
# 👉🏽 성적은 80이상 입니다.

"""비교 연산자
X == Y	:  X와 Y가 서로 같을 때 참(True)이다.
X != Y	:  X와 Y가 서로 다를 때 참(True)이다.
X > Y	  :  X가 Y보다 클 때 참(True)이다.
X < Y	  :  X가 Y보다 작을 때 참(True)이다.
X >= Y	:  X가 Y보다 크거나 같을 때 참(True)이다.
X <= Y	:  X가 Y보다 작거나 같을 때 참(True)이다.
"""

"""논리연산자
X and Y	:  X와 Y가 모두 참(True)일 때 참(True)이다.
X or Y	:  X와 Y중 하나만 참이어도 참이다.
not X	  :  X가 거짓일 때 참이다
"""

"""기타 연산자
X in 리스트     :	리스트 안에 X가 들어가 있을 때 참이다.
X not in 문자열 :	문자열 안에 X가 들어가 있지 않을 때 참이다.


파이썬에서 추가적으로 in 연산자와 not in 연산자를 제공한다.
여러 개의 데이터를 담는 자료형으로 
리스트, 튜플, 문자열, 사전과 같은 자료형이 존재한다.

이러한 자료형은 여러 개의 데이터를 담고 있기 때문에, 
자료형 안에 어떤 값이 존재하는지 확인
"""

"""
리스트에서 특정한 원소의 값만 없앤다면?
"""
#### (1) 일반적인 코드
array = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = []

for i in array:
    if i not in remove_set:
        result.append(i)

print(result)  # [1, 2, 4]

#### (2) 간결한 코드
array = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in array if i not in remove_set]
print(result)  # [1, 2, 4]
