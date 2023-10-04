# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181939
# 방법 1
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


# 방법 2
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a + b, b + a))
