#基本操作
import sys
input = sys.stdin.readline

#input
lst = list(input().rstrip())
anslst = []
for i in range(len(lst)):
    now = lst[i]
    if now == '+':
        b = anslst.pop()
        a = anslst.pop()
        anslst.append(a + b)
    elif now == '-':
        b = anslst.pop()
        a = anslst.pop()
        anslst.append(a - b)
    elif now == '*':
        b = anslst.pop()
        a = anslst.pop()
        anslst.append(a * b)
    elif now == '/':
        b = anslst.pop()
        a = anslst.pop()
        anslst.append(a // b)
    else:
        now = int(now)
        anslst.append(now)
print(*anslst)