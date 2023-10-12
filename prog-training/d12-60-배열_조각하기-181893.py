# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181893
"""
정수 배열 arr와 query가 주어집니다.
query를 순회하면서 다음 작업을 반복합니다.

짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 
배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.

홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 
배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.

위 작업을 마친 후 남은 arr의 부분 배열을 return

입력#1
arr        : [0, 1, 2, 3, 4, 5]
query      : [4, 1, 2]

출력#1
[1, 2, 3]

📌 enumerate() : 인덱스(index)와 원소를 동시에 접근하면서 루프돌릴 떄
"""


def solution(arr, query):
    for idx, el in enumerate(query):
        if idx % 2 == 0:
            arr = arr[: el + 1]
        else:
            arr = arr[el:]
    return arr


print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))
