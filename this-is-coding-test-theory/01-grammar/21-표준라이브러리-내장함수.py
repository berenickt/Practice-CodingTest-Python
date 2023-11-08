"""
내장 함수는 import 명령어 없이 바로 사용할 수 있다.
"""

"""(1) sum()
"""
result = sum([1, 2, 3, 4, 5])
print(result)


"""(2) min(), max()
"""
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

""" (3) eval()
해당 수식을 계산한 결과를 반환
"""
result = eval("(3+5) * 7")
# 👉🏽 56


""" (4) sorted()
sorted(): iterable 객체가 들어왔을 때, 정렬된 결과를 반환
- iterable: [ List ], ( Tuple ), [ Dictionary ]
- key = lambda a: a[x], 원소기준으로 오름 / 내림 차순 정렬가능

sort(): list iterable 객체는 기본으로 sort() 함수 사용 가능
- iterable: [ List ], ( Tuple ), [ Dictionary ]
"""
# sorted ()
data_list = [3, 1, 2, 5]
data_tuple = (3, 1, 2, 5)
data_dict = [("안영우", 26), ("동생1", 23), ("동생2", 13), ("동생3", 11)]
data_dict_key = sorted(
    [("안영우", 26), ("동생1", 23), ("동생2", 13), ("동생3", 11)],
    key=lambda x: x[1],
    reverse=True,
)

print(sorted(data_list))
# 👉🏽 [1, 2, 3, 5]
print(sorted(data_list, reverse=True))
# 👉🏽 [5, 3, 2, 1]

print(sorted(data_tuple))
# 👉🏽 [1, 2, 3, 5]
print(sorted(data_tuple, reverse=True))
# 👉🏽 [5, 3, 2, 1]

print(sorted(data_tuple))
# 👉🏽 [('동생1', 23), ('동생2', 13), ('동생3', 11), ('안영우', 26)]
print(sorted(data_tuple), lambda a: a[1])
# 👉🏽 [('안영우', 26), ('동생1', 23), ('동생2', 13), ('동생3', 11)]

# sort(only list)
data_list = [3, 1, 2, 5]
data_list.sort()

print(data_list)
# 👉🏽 [1, 2, 3, 5]
