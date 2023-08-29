# 💡 요세푸스 문제 @https://www.acmicpc.net/problem/1158
from collections import deque   # 덱을 사용하기 위해 collections 모듈 임포트
n, m = map(int,input().split()) # n과 m을 입력받아 정수로 변환하여 할당
q = deque()                     # 덱(큐) 초기화

for i in range(1, n+1): # 1부터 n까지의 숫자에 대해 반복
  q.append(i)           # 덱에 숫자 추가

ans = [] # 결과를 저장할 리스트 초기화

for i in range(n-1):      # n-1번 반복 (마지막 한 개의 숫자는 따로 처리)
  for j in range(m-1):    # m-1번 반복 (m-1번째 숫자까지 왼쪽으로 이동)
    q.append(q.popleft()) # 맨 앞 숫자를 빼서 뒤로 옮김
  ans += [q.popleft()]    # m-1번 이동 후 맨 앞 숫자를 결과 리스트에 추가

ans += [q[0]]             # 마지막으로 남은 숫자를 결과 리스트에 추가

# 결과 리스트를 문자열로 변환하여 출력
print('<' + ', '.join(map(str,ans)) + '>')