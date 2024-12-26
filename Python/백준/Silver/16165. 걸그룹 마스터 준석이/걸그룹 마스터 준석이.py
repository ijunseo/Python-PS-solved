import sys
input = sys.stdin.readline
teamnum, q = map(int,input().split())

teamdic = {}
memdic = {}
for i in range(teamnum):
    list1 = []
    team = input().strip()
    memnum = int(input().strip())
    for j in range(memnum):
        mem = input().strip()
        list1.append(mem)
    list1.sort()
    teamdic[team] = list1
    for k in list1:
        memdic[k] = team
for i in range(q):
    ques = input().strip()
    quesnum = int(input().strip())
    if quesnum == 0:
        for j in teamdic[ques]:
            print(j)
    if quesnum == 1:
        ans = memdic[ques]
        print(ans)