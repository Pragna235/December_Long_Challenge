# cook your dish here
from math import * 

for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    first=arr[0]
    for i in arr:
        first=gcd(first,i) 
    for  j in arr:
        print(j//first,end=" ") 
    print()
    