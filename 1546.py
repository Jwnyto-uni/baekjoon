import sys
input = sys.stdin.readline

A = []
n = 0

N = int(input())
a = list(map(int,input().split()))

for i in a :
  n = n + i/max(a)*100

print(n/N)
