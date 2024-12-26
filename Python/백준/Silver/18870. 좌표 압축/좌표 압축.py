import sys
num = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
numset = set(numlist)
numsetlist = sorted(list(numset))

numsetdict = {}

for i in range(len(numsetlist)):
    a = numsetlist[i]
    numsetdict[a] = i

answerlist = [0] * num

for i in range(num):
    ansnum = numlist[i]
    ansnum = numsetdict.get(ansnum)
    answerlist[i] = ansnum
    
for i in answerlist:
    print(i, end = ' ')