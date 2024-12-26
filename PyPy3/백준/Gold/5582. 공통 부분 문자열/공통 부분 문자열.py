import sys
input = sys.stdin.readline
str1 = input().strip() #短い
str2 = input() #長い
if len(str1) > len(str2):
  str1, str2 = str2, str1
  
str2 = "0" * (len(str1)) + str2 + "0" * (len(str1))
ans = 0
trynum = len(str2) - len(str1) + 1 #実行する回数
for i in range(trynum):
  now = 0
  for j in range(len(str1)):
    if str1[j] == str2[i + j]:
      now += 1
    else:
      ans = max(ans, now)
      now = 0
    ans = max(ans, now)
print(ans)