year = int(input("Enter the year: "))
if(year%4==0):
    if(year%400==0):
        print("Leap year")
    elif(year%100!=0):
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")