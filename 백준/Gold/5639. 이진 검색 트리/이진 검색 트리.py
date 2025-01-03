import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break
treelist = [[i, None, None] for i in range(len(nums))]
def find(nowindex, nodeindex):
    global treelist
    if nums[nowindex] < nums[nodeindex]:
        if treelist[nodeindex][1] == None:
            treelist[nodeindex][1] = nowindex
        else:
            find(nowindex, treelist[nodeindex][1])
    if nums[nowindex] > nums[nodeindex]:
        if treelist[nodeindex][2] == None:
            treelist[nodeindex][2] = nowindex
        else:
            find(nowindex, treelist[nodeindex][2])
    
for i in range(1, len(nums)):
    find(i, 0)
def printans(start):
    if treelist[start][1] != None:
        printans(treelist[start][1])
    if treelist[start][2] != None:
        printans(treelist[start][2])
    print(nums[treelist[start][0]])
printans(0)