import math

#explaining to the user the difference between the 2 and then ask which they want to proceed with .
print("Investment - To calculate the amount of interest , you'll earn on your investment\n")
print("Bond - to calculate the amount you'll have to pay on a home loan\n")

menu=input('Enter either investment or bond  from the menu above and proceed\n').lower()
if menu=="" :
    print("choose from above ")

if menu=='investment':
    deposit=float(input('what is the amount of money you want to deposit ?'))
    interest_rate=(float(input('interest rate ?')))
    interest_divided=(interest_rate / 100)


    years=(int(input(' number of years you planning on investing ?')))
    interest=(input('do you want simple or compound interest ?'))
    if interest=='simple interest':
        print(int(deposit*(1+years*interest_divided)))
    else:
        interest=='compound interest'
        print(deposit * (pow((1 + interest_divided),years)))

print()
if menu=='bond':
    house_value=(float(input(' what is the house value ?\n')))

    int_rate=(float(input('what is your interest rate?\n')))

    i=(int_rate/ 100)
    divided_by_twelve=(float(i / 12))
    month_pay_bond=(int(input(' how many months you planning on paying the bond?\n')))
    print((divided_by_twelve * house_value)/(1 - (1 + divided_by_twelve)**(-1*month_pay_bond)))

















 
 
    


