low=int(input("Enter the lower limit"))
high=int(input("Enter the upper limit"))
for i in range(low,high+1):
    p=i
    flag=1
    while(p!=0):
        if((p%10)%2==0):
            flag=0
            break
        p//=10
    if(flag):
        print(i, end=",")