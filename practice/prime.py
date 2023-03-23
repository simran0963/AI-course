num = int(input("Enter the number: "))
cnt=0
for i in range(2, int(num/2), 1):
    if(num%i==0):
        cnt+=1
if(cnt==0):
    print("Prime")
else:
    print("Not prime") 