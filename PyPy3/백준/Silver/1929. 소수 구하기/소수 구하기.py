def prime_number(num):
  if num == 1:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True
prime_number(9)
prime_list = []
a, b = map(int, input().split())
for i in range(a, b+1):
  if prime_number(i) == True:
    prime_list.append(i)
  else:
    continue
for i in prime_list:
  print(i)