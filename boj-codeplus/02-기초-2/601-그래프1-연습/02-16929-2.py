# 💡 Two Dots 📚 https://www.acmicpc.net/problem/16929
dx = [0, 0, 1, -1]  # 이동 방향: 오른쪽, 왼쪽, 아래, 위
dy = [1, -1, 0, 0]  # 이동 방향: 오른쪽, 왼쪽, 아래, 위

n, m = map(int, input().split())  # 입력: 행과 열의 크기 n, m
a = [input() for _ in range(n)]  # 입력: 문자열로 이루어진 2차원 배열 a
check = [[False] * m for _ in range(n)]  # 방문 여부를 저장하는 2차원 배열 초기화


def go(x, y, px, py, color):
    if check[x][y]:  # 이미 방문한 위치인 경우
        return True  # 사이클 발견
    check[x][y] = True  # 현재 위치 방문 처리
    for k in range(4):  # 상하좌우 방향에 대해서
        nx, ny = x + dx[k], y + dy[k]  # 새로운 위치 계산
        if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있는지 확인
            if (nx, ny) == (px, py):  # 이전 위치로 되돌아가는 경우 건너뛰기
                continue
            if a[nx][ny] == color:  # 같은 색상의 공이라면
                if go(nx, ny, x, y, color):  # 재귀 호출
                    return True  # 사이클 발견
    return False  # 사이클을 찾지 못한 경우


for i in range(n):
    for j in range(m):
        if check[i][j]:  # 이미 방문한 위치라면 건너뛰기
            continue
        ok = go(i, j, -1, -1, a[i][j])  # 탐색 시작
        if ok:
            print("Yes")  # 사이클 발견
            exit()  # 프로그램 종료

print("No")  # 모든 탐색을 마치고도 사이클을 찾지 못한 경우 출력
