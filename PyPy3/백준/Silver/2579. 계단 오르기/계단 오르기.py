import sys
num = int(input())
list1 = [0]
list2 = [0]
first_step = int(sys.stdin.readline())
list1.append(first_step)
list2.append(0)
for i in range(num - 1):
  a = int(sys.stdin.readline())
  max1 = max(list1[0] + a, list2[0] + a)
  max2 = list1[1] + a
  list1.append(max1)
  list2.append(max2)
  list1.pop(0)
  list2.pop(0)
real_max = max(list1[1], list2[1])
print(real_max)