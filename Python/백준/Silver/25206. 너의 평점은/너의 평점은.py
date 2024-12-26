import sys
testnum = 0
score = 0
while True:
    try:
        test = list(map(str, sys.stdin.readline().split()))
        test1 = test[-1]
        num = float(test[-2])
        if test1 == "A+":
            score += 4.5 * num

        if test1 == "A0":
            score += 4 * num

        if test1 == "B+":
            score += 3.5 * num

        if test1 == "B0":
            score += 3 * num

        if test1 == "C+":
            score += 2.5 * num

        if test1 == "C0":
            score += 2 * num

        if test1 == "D+":
            score += 1.5 * num

        if test1 == "D0":
            score += 1 * num

        if test1 == "F":
            score += 0 * num

        if test1 == "P":
            continue
        testnum += num
    except:
        if testnum == 0:
            print("0")
        else:
            print(score / testnum)
        break

