"""Itertools, 이터툴즈
파이썬에서 반복되는 데이터(iterable 한 데이터)를 처리하는 기능을 포함
즉 이터러블(iterable)한 데이터는 반복문에서 사용할 수 있는 데이터를 의미

💡 permutation() : 순열
- list iterable 객체에서 r개의 데이터를 뽑아 
- 일렬로 나열하는 모든 경우(순열)

💡 combination() : 조합
- list iterable 객체에서 r개의 데이터를 뽑아 
- 순서를 고려하지 않고 나열하는 모든 경우(조합)
"""
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement


data = ["A", "B", "C"]

# 📌 (1) 순열
data_permutation = list(permutations(data, 2))
# 👉🏽 [('A', 'B'), ('B', 'A')]

# 📌 (2) 순열(중복허용) ===> 2개를 뽑는 모든 순열 구하기(중복 허용)
data_product = list(product(data, repeat=2))
# 👉🏽 [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

# 📌 (3) 조합(중복허용) ===> 2개를 뽑는 모든 조합 구하기(중복허용)
data_combination = list(combinations_with_replacement(data, 2))
# 👉🏽 [('A', 'A'), ('A', 'B'), ('B', 'B')]
