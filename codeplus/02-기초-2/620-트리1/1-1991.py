# 💡 트리 순회 📚 https://www.acmicpc.net/problem/1991
# 이진 트리의 각 노드를 표현하는 클래스 정의
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


# 알파벳 'A'의 아스키 코드 값을 기준으로 한 딕셔너리 초기화
a = dict()
A = ord("A")


# 전위 순회(preorder) 함수 정의
def preorder(x):
    if x == -1:  # 노드가 비어있는 경우
        return
    print(chr(x + A), end="")  # 현재 노드의 값을 출력 (아스키 코드를 문자로 변환하여 출력)
    preorder(a[x].left)  # 왼쪽 서브트리를 전위 순회
    preorder(a[x].right)  # 오른쪽 서브트리를 전위 순회


# 중위 순회(inorder) 함수 정의
def inorder(x):
    if x == -1:  # 노드가 비어있는 경우
        return
    inorder(a[x].left)  # 왼쪽 서브트리를 중위 순회
    print(chr(x + A), end="")  # 현재 노드의 값을 출력 (아스키 코드를 문자로 변환하여 출력)
    inorder(a[x].right)  # 오른쪽 서브트리를 중위 순회


# 후위 순회(postorder) 함수 정의
def postorder(x):
    if x == -1:  # 노드가 비어있는 경우
        return
    postorder(a[x].left)  # 왼쪽 서브트리를 후위 순회
    postorder(a[x].right)  # 오른쪽 서브트리를 후위 순회
    print(chr(x + A), end="")  # 현재 노드의 값을 출력 (아스키 코드를 문자로 변환하여 출력)


# 입력 받을 이진 트리의 높이 n을 입력
n = int(input())

# 이진 트리의 각 노드 정보 입력 및 저장
for _ in range(n):
    x, y, z = input().split()
    x = ord(x) - A  # 현재 노드의 아스키 코드 값을 계산
    left = -1
    right = -1
    if y != ".":  # 왼쪽 자식 노드가 있는 경우
        left = ord(y) - A  # 왼쪽 자식 노드의 아스키 코드 값을 계산
    if z != ".":  # 오른쪽 자식 노드가 있는 경우
        right = ord(z) - A  # 오른쪽 자식 노드의 아스키 코드 값을 계산
    a[x] = Node(left, right)  # 노드 정보를 저장

# 전위 순회, 중위 순회, 후위 순회 결과 출력
preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
