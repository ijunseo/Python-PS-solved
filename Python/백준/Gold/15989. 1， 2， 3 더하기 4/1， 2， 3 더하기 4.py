import sys
num = int(sys.stdin.readline())
listans = [0, 1, 2, 3]
def findnum(a):
    global listans
    try:
        return listans[a]
    except:
        for i in range(len(listans), a + 1):
            listans.append(1 + i // 2 + int(listans[i - 3]))
        return listans[-1]

for i in range(num):
    c = int(sys.stdin.readline())
    print(findnum(c))