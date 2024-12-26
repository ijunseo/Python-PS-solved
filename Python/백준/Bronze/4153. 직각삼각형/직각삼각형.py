while True:
  a, b, c = map(int, input().split())
  longest = max(a, b, c)
  if a == 0 and b == 0 and c == 0:
    break
  if 2*(longest **2) == a**2 + b**2 + c**2:
    print("right")
  else:
    print("wrong")