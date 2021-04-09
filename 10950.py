T = int(input())
i = 0
while T > i :
  try :
    a, b = map(int,input().split())
    print(a+b)
    i = i+1
  except EOFError :
    break
