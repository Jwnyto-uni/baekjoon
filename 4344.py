C = int(input())

for i in range(0, C) :
  a = list(map(int,input().split()))
  N = a[0]
  above = []
  sum = 0
  sum2 = 0
  for j in range(1, len(a)) :
    sum = sum + a[j]
  for j in range(1, len(a)) :
    M = sum/N
    if a[j] > M :
      above.append(a[j])
  
  n = len(above)/(len(a)-1)*100
  print("%s%%"%'{:.3f}'.format(round(n, 3)))
