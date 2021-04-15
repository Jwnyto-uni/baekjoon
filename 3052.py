import sys
imput = sys.stdin.readline

b = []
number = 0, 0

for i in range(0, 10) :
  a = int(input())
  if i == 0 :
    b.append(a%42)
  for m in range(len(b)) :
    if b[m] != a%42 :
      number += 1
  if number == len(b) :
    b.append(a%42)
  number = 0

print(len(b))



