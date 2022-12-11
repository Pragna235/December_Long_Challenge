# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    pro=1 
    for i in arr:
        pro*=i 
    if(pro%k==0):
        print("Yes")
    else:
        print("No")