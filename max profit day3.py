def profit(l):
    sum=0
    i=l
    for i in range(0,n-1):
        if(l[i+1]>l[i]):
            sum=sum+(l[i+1]-l[i])
            i=i+1
    return sum
n=int(input("eneter the elements:"))
l=[]
for j in range(n):
    m=int(input(""))
    l.append(m)
print(l)
print("profit=",profit(l))
