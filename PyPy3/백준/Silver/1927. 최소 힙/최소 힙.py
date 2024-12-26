import heapq
import sys
heaplist = []
def push(a):
  global heaplist
  heapq.heappush(heaplist, a)
def pop():
  global heaplist
  print(heapq.heappop(heaplist))
num = int(input())
for i in range(num):
  a = int(sys.stdin.readline().strip())
  if a == 0 and len(heaplist) == 0:
    print("0")
  elif a == 0:
    pop()
  else:
    push(a)