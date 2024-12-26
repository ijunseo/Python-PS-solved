import sys
num = int(input())
answerlist = []
def push(a):
  global answerlist
  answerlist.append(int(a))
def top():
  global answerlist
  if len(answerlist) == 0:
    print("-1")
  else:
    print(answerlist[len(answerlist) - 1])
def pop():
  global answerlist
  if len(answerlist) == 0:
    print("-1")
  else:
    print(answerlist[len(answerlist) - 1])
    answerlist.pop()
def size():
  global answerlist
  print(len(answerlist))
def empty():
  global answerlist
  if len(answerlist) == 0:
    print("1")
  else:
    print("0")
for i in range(num):
  com = sys.stdin.readline().split()
  if len(com) == 2: 
    a, b = com
  else:  
    a = com[0]
    b = None 

  if a == "pop":
    pop()
  elif a == "size":
    size()
  elif a == "empty":
    empty()
  elif a == "top":
    top()
  elif a == "push":
    push(b)
  