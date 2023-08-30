# 💡 단어 뒤집기2 @https://www.acmicpc.net/problem/17413
import sys

# 입력 받은 문자열을 리스트로 변환하여 처리합니다.
word = list(sys.stdin.readline().rstrip())

# 인덱스와 시작 위치 변수를 초기화합니다.
i = 0
start = 0

# 문자열의 끝까지 반복하며 처리합니다.
while i < len(word):
  if word[i] == "<":       
    i += 1 
    while word[i] != ">":      
      i += 1 
    i += 1               
  elif word[i].isalnum(): 
    start = i
    while i < len(word) and word[i].isalnum():
      i += 1
    tmp = word[start:i] 
    tmp.reverse()       
    word[start:i] = tmp
  else:                   
    i += 1                

# 리스트의 문자들을 합쳐서 출력합니다.
print("".join(word))
