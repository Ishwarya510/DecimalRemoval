#for walmart
n=int(input())
a=[]
for i in range(0,n):
    ele=float(input())
    j=ele*100
    if(j%100==99):
        continue
    else:
         a.append(int(j)/100)
print(a)
#sobeys
n=int(input())
a=[]
for i in range(0,n):
    ele=float(input())
    j=ele*100
    if(j%100==94):
        continue
    else:
         a.append(int(j)/100)
print(a)