annual_salary = int(input("Enter the annual salary: "))
portion_saved = float(input("Enter the savings in decimals: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Semi annual raise is : "))
down_pay = 0.25*total_cost
current_savings = 0
r = 0.04/12 #calculated for each month
i=0
while(current_savings < down_pay):
    # print("C1:",current_savings)
    if(i%6==0):
        annual_salary+=(annual_salary*semi_annual_raise)
    current_savings += portion_saved*(annual_salary/12)
    current_savings += r+0.01*(annual_salary/12)
    # print("C2:",current_savings)
    i+=1
print("Total months required to save an amount equal to the down payment is : ",i)