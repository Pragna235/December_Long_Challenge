# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    sp=(n*(n+1)//2) 
    if(k<sp):
        print(-1)
    else:
        for i in range(n-1):
            print(1,end=" ")
        print(k-sp+1)