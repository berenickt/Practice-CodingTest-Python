# 💡 큐 📚 https://www.acmicpc.net/problem/10845
import sys

input = sys.stdin.readline  # 입력 속도 향상을 위해 사용
n = int(input())           # 명령어 개수 입력

queue = [0] * n  # 큐를 나타낼 리스트 초기화
begin = 0       # 큐의 시작 인덱스 초기화
end = 0         # 큐의 끝 인덱스 초기화

for _ in range(n):
    # 명령어와 추가 값들을 공백을 기준으로 나눠 리스트에 저장
    cmd, *val = input().split()

    if cmd == 'push':
        num = int(val[0])  # 추가할 숫자 추출
        queue[end] = num  # 큐의 끝에 숫자 추가
        end += 1          # 끝 인덱스 증가
    elif cmd == 'front':
        if begin == end:  # 큐가 비어있는 경우
            print(-1)
        else:
            print(queue[begin])  # 큐의 시작값 출력
    elif cmd == 'size':
        print(end-begin)  # 큐에 있는 원소 개수 출력
    elif cmd == 'empty':
        if begin == end:  # 큐가 비어있는 경우
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if begin == end:      # 큐가 비어있는 경우
            print(-1)
        else:
            print(queue[begin])  # 큐의 시작값 출력
            begin += 1          # 시작 인덱스 증가
    elif cmd == 'back':
        if begin == end:      # 큐가 비어있는 경우
            print(-1)
        else:
            print(queue[end-1])  # 큐의 끝값 출력
