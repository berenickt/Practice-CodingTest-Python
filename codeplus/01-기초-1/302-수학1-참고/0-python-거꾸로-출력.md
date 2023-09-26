# 1. [python] 문자열 거꾸로 출력하기 [::-1]

```python
s = 'abcde'
print(s[3:0:-1]) # dcb
```

- `[3:0:-1]` : 3이상 0미만 역순으로 출력

```python
l = ['a', 'b', 'c', 'd', 'e']
print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']

t = ('a', 'b', 'c', 'd', 'e')
print(t[::-1])  # ('e', 'd', 'c', 'b', 'a')
```

결과적으로 [::-1] 인덱스를 주면 전체 문자열을 역순으로 출력
문자열 뿐 아니라 리스트나 튜플에도 적용 가능하다.

---

# 2. 다른 방법

## 2.1 for문을 통해 해결

```python
s = 'abcde'
s_reverse = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
for char in s:
    s_reverse = char + s_reverse

print(s_reverse)  # edcba
```

---

## 2.2 제공해주는 함수로 해결

```python
s = 'abcde'
s_list = list(s)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list.reverse()  # reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음

print(''.join(s_list))  # 거꾸로 뒤집어진 리스트를 연결해서 출력
```

파이썬에서 제공하는 reverse() 함수 사용
