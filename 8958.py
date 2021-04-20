n=int(input())

for i in range(1, n+1):
    a=list(map(str,input()))
    num=0
    sum=0
    for j in range(len(a)):
        if a[j] in a:      
            if a[j] == 'O':
                num += 1
                sum += num              
            if a[j]=='X':
                num = 0
    print(sum)
