import sys
num = int(sys.stdin.readline().strip())
count = 0
peoplelist = []
for i in range(num):
    com = str(sys.stdin.readline().strip())
    if com != "ENTER":
        peoplelist.append(com)
    if com == "ENTER" or i == num - 1:
        count += len(set(peoplelist))
        peoplelist = []
print(count)