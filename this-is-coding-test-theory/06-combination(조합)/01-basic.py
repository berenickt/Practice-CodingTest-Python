"""조합(combination) 
- 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
- nCr으로 불림
- 순서에 의미가 없을 때 주로 사용함.
@see https://www.youtube.com/watch?v=1I6fAgEOPt4 --- 수학삼촌
"""
import itertools

data = [1, 2, 3]

### 사용법 : combinations(객체, r) :
# 반복가능한 객체(리스트,튜플,문자열)안에서 r개를 선택
for i in itertools.combination(data, 3):
    print(list(i), end=" ")

# 👉🏽 [1, 2][1, 3][2, 3]
