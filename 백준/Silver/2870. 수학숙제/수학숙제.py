import sys
input = sys.stdin.readline

#input 
n = int(input())
s = []
nn = ''
for _ in range(n):
    now = str(input().rstrip())
    for i in range(len(now)):
        try:
            nowstr = int(now[i])
            nn = nn + str(nowstr)
        except:
            if nn != '':
                nn = int(nn)
                s.append(nn)
                nn = ''
    if nn != '':
        nn = int(nn)
        s.append(nn)
        nn = ''

#output
for i in sorted(s):
    print(i)