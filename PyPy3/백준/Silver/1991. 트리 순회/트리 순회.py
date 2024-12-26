import sys
treedic = {}
num = int(sys.stdin.readline())
for i in range(num):
    a, b, c = map(str, sys.stdin.readline().split())
    treedic[a] = [b, c]
def preorder(node):
    if node != ".":
        print(node, end = '')
        preorder(treedic[node][0])
        preorder(treedic[node][1])
        
def inorder(node):
    if node != ".":
        inorder(treedic[node][0])
        print(node, end = '')
        inorder(treedic[node][1])

def postorder(node):
    if node != ".":
        postorder(treedic[node][0])
        postorder(treedic[node][1])
        print(node, end = '')
    
preorder("A")
print()
inorder("A")
print()
postorder("A")

