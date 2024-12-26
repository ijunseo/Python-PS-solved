from collections import deque
numlist = deque()
num = int(input())
for i in range(1, num + 1):
    numlist.append(i)
anslist = []
while numlist:
    a = numlist.popleft()
    try:
        b = numlist.popleft()
        anslist.append(a)
        numlist.append(b)
    except:
        anslist.append(a)
        break
for i in anslist:
    print(i, end = " ")
    