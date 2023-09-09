# 💡 트리 순회 📚 https://www.acmicpc.net/problem/1991
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


a = dict()
A = ord('A')


def preorder(x):
    if x == -1:
        return
    print(chr(x+A), end='')
    preorder(a[x].left)
    preorder(a[x].right)


def inorder(x):
    if x == -1:
        return
    inorder(a[x].left)
    print(chr(x+A), end='')
    inorder(a[x].right)


def postorder(x):
    if x == -1:
        return
    postorder(a[x].left)
    postorder(a[x].right)
    print(chr(x+A), end='')


n = int(input())
for _ in range(n):
    x, y, z = input().split()
    x = ord(x)-A
    left = -1
    right = -1
    if y != '.':
        left = ord(y)-A
    if z != '.':
        right = ord(z)-A
    a[x] = Node(left, right)

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
