n=int(input("Enter the number: "))
s=0
for i in range(1,n+1):
    s=i
    for j in range(0,i):
        s=i+(j*n)-j
        print(s,end=" ")
    print()
