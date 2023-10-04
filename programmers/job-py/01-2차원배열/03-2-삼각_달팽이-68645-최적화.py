# 💡 삼각 달팽이(Lv2) 📚 https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    y, x = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            # 순서대로 아래 -> 오른쪽 -> 위 (반시계 나선형)
            if angle == 0: y += 1
            elif angle == 1: x += 1   
            elif angle == 2: y -= 1; x -= 1      
            res[y][x] = num
            num += 1
            
    return [i for j in res for i in j]