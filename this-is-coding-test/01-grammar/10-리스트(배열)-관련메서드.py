"""
(1) append()	
- 변수명.append()	
- 리스트에 원소를 하나 삽입한다.
- O(1)

(2) sort()	
- 변수명.sort()	
- 오름차순 정렬	
- O(NlogN)

(3) sort()	
- 변수명.sort(reverse = True)	
- 내림차순 정렬
- O(NlogN)

(4) reverse()	
- 변수명.reverse()
- 리스트의 원소순서를 뒤집는다.
- O(N)

(5) insert()	
- insert(삽입 할 위치 인덱스, 삽입 값)
- 특정한 인덱스 위치에 원소를 삽입한다.
- O(N)

(6) count()	
- 변수명.count(특정 값)
- 리스트에서 특정한 값을 가지는 데이터의 개수를 셀때 사용한다.
- O(N)

(7) remove()
- 변수명.remove(특정 값)
- 특정한 값을 갖는 원소를 제거하는데, 여러 개면 하나만 제거한다.
- O(N)
"""

"""
주의 할 점은 insert()와 remove()인데, 
둘다 중간에 원소를 삽입 / 삭제 한 뒤, 
리스트의 원소 위치를 조정해주기 때문에 시간복잡도가 O(N)이 소요된다,

따라서 
insert()는 append()를 사용하고, 
remove()는 다음과 같이 사용하자
"""
array = [1, 2, 3, 4, 5]
remove_set = {1, 2}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in array if i not in remove_set]
# 👉🏽 [3, 4, 5]

"""
실제로 동일조건에서 remove()를 사용했을 때 3.814697265625e-06초가 걸렸고, 
remove_set으로 사용했을 때 2.86102294921875e-06초가 걸렸다. 
약 1초정도 빠른것을 확인 할 수 있다
"""
