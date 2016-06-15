# Finance Application
up_eqn=(float(4.5)/100)*(1+float(4.5)/100)**5
down_eqn=((1+float(4.5)/100)**5 -1)
monthly_eqn = (1000.0 * up_eqn/down_eqn)/int(12)
print(monthly_eqn)

#Finance Calculator For Loans Payments Calculations

def subscribe(first_name):
    short_name=input("What is your name??")
    return  short_name

name=subscribe('short_name')
print(name)


# Remaining Balance Calculator

def remainigg_Balance (principal,annual_interest_rate,duration,number_payments):
    principal=float(input("What is your princial amount of the loan????"))
    annual_interest_rate=float(input("What is your annual interest rate for the loan???"))
    duration=int(input("What was the duration of the loan????"))
    number_payments=int(input("How many payments have you made???"))
    if annual_interest_rate ==0:
        return principal((1)-(principal/duration))
    rate=annual_interest_rate/100/12.0
    n= duration*12
    p=number_payments
    ramain_bal =principal*((1.0+rate)**n-(1.0+rate)**p)/(((1+rate)**n)-1)
    return ramain_bal
remaing_balance=remainigg_Balance ('principal','annual_interest_rate','duration','number_payments')
print("Your remainig balance on the loan is : $" + str(remaing_balance))









