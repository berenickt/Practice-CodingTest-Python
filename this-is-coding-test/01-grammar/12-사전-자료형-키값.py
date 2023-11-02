"""
사전자료형은 키(Key) 와 값(Value)의 쌍을 데이터로 가지는 자료형이다.
이런점에서 우리가 원하는 변경 불가능한 데이터를 키로 사용 할 수 있다.
파이썬의 대표적인 예시는 사전(Dictionary)이다.

파이썬의 사전자료형은 해시 테이블(Hash table)을 이용하므로, 
기본적으로 데이터의 검색 및 수정에 있어 O(1)의 시간에 처리 할 수 있다.
"""
data = dict()
data["사과"] = "Apple"
data["바나나"] = "Banana"
data["수박"] = "Watermelon"

# 👉🏽 {'사과': 'Apple', '바나나': 'Banana', '수박': 'Watermelon'}

"""
사전 자료형을 잘 이용하기 위해서는 
다양한 함수에 대해 알아야한다.
대표적으로 키와 값을 별도로 뽑아내기 위한 함수가 있다. 

키 데이터는 keys(), 
값 데이터는 values() 함수를 이용한다.
"""
data = dict()

data["사과"] = "Apple"
data["바나나"] = "Banana"
data["수박"] = "Watermelon"

key_list = data.keys()
value_list = data.values()

print(key_list)
# 👉🏽 dict_keys(['사과', '바나나', '수박'])

print(value_list)
# 👉🏽 dict_values(['Apple', 'Banana', 'Watermelon'])
