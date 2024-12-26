num=int(input())

numlist = [0,1]

for i in range(2,1500001):
    numlist.append((numlist[i-1]+numlist[i-2])%1000000)
    
num %= 1500000
print(numlist[num])