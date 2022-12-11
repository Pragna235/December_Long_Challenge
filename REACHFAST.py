# cook your dish here
for t in range(int(input())):
    x,y,k=map(int,input().split())
    #prinT(x,y,k)
    diff=abs(x-y)
    if(diff==0):
        print(0)
    else:
        if(diff%k==0):
            print(diff//k)
        else:
            print((diff//k)+1)