import sys
testcase = int(sys.stdin.readline())
for i in range(testcase):
    choco = int(sys.stdin.readline())
    if choco == 1:
        print("0")
    else:
        choconum = 11 * (10 ** (choco - 2)) + 11
        print(choconum)