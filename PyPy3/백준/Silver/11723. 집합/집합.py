import sys
num = int(input())
numset = set()
def add(a):
  global numset
  numset.add(a)
def remove(a):
  global numset
  numset.discard(a)
def check(a):
  if a in numset:
    print("1")
  else:
    print("0")
def toggle(a):
  if a in numset:
    numset.remove(a)
  else:
    numset.add(a)
def all():
  global numset
  numset = set(range(1, 21))
def empty():
  global numset
  numset = set()
for i in range(num):
  ex = sys.stdin.readline().split()
  if len(ex) == 2:
    defwhat = ex[0]
    whichnum = int(ex[1])
  else:
    defwhat = ex[0]
    whichnum = None
  if defwhat == "add":
    add(int(whichnum))
  elif defwhat == "remove":
    remove(int(whichnum))
  elif defwhat == "check":
    check(int(whichnum))
  elif defwhat == "toggle":
    toggle(int(whichnum))
  elif defwhat == "all":
    all()
  elif defwhat == "empty":
    empty()