import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

A = ",".join(result)

for i in range(0, 10, 1) :
  print(A.count("%d" % i))
