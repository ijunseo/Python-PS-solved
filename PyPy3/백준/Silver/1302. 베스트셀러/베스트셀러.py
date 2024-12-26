import sys
n = int(sys.stdin.readline())
bookdic = {}
for i in range(n):
    a = sys.stdin.readline().strip()
    if a not in bookdic:
        bookdic[a] = 1
    else:
        bookdic[a] += 1
answerlist = []
for a , b in bookdic.items():
    answerlist.append([a, b])
answerlist.sort()
answerlist.sort(key = lambda x : x[1], reverse = True)
print(answerlist[0][0])