# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181938
def solution1(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)


def solution2(a, b):
    res = int(str(a) + str(b))
    comp = 2 * a * b
    return max(res, comp)
