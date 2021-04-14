A = []
a = []
while len(A) < 9 :
  a = list(map(int,input().split()))
  A.append(a)
b = max(A)

print(*b)
print(A.index(b)+1)
