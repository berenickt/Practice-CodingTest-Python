# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181938
# 방법 1
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)


# 방법 2
def solution(a, b):
    res = int(str(a) + str(b))
    comp = 2 * a * b
    return max(res, comp)
