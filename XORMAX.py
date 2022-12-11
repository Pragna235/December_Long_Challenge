# cook your dish here
for t in range(int(input())):
    str1=input()
    str2=input()
    c=[0,0]
    for i in str1:
        c[int(i)]+=1 
    for j in str2:
        c[int(j)]+=1 
    xor='1'*min(c)
    xor+='0'*(len(str1) - min(c))
    print(xor)
        