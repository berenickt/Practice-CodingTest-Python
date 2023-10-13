# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181855
"""
문자열 배열 strArr이 주어집니다.
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때
가장 개수가 많은 그룹의 크기를 return

입력#1
["a", "bc", "d", "efg", "hi"]

출력#1
2
"""


def solution(strArr):
    dic = {len(str): 0 for str in strArr}
    for str in strArr:
        dic[len(str)] += 1
    return max(dic.values())


print(solution(["a", "bc", "d", "efg", "hi"]))


#############리스트(제한사항을 보면 원소의 길이는 1 ~ 30)
def solution2(strArr):
    arr = [0] * 31
    for s in strArr:
        arr[len(s)] += 1
    return max(arr)
