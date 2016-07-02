
# Calulator 3 inputs
def calculate_monthly_payment(principal,annual_interest_rate,duration):

    if annual_interest_rate ==0:
        return principal/(duration*12)

    r= annual_interest_rate/100/12
    n= duration*12
    monthly_payment =principal * (r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return  monthly_payment



# # # # Remaining Balance 4 inputs Calculator

def remainigg_balance(pay):
    number_payments = pay
    rt =user_annual_interest_rate
    duration=user_duration
    principal=user_principal
    if rt == 0:
        return principal*((1)-(principal/duration))
    rate = rt/100/12.0
    n= duration*12
    p=number_payments
    ramain_bal = principal * ((1.0+rate)**n-(1.0+rate)**p)/(((1+rate)**n)-1)
    return ramain_bal
# remaing_balance = remainigg_balance(number_payments)
# print(remaing_balance)


# While loop to repeat this application base don user decesion 

name_user = raw_input("May i know your name????")
print("Welcome to the loan calculator application, " + name_user + ' !!!!!')
user_input = 1 
while user_input == 1 :
    user_principal = float(input("What is your princial amount of the loan????"))
    user_annual_interest_rate = float(input("What is your annual interest rate for the loan???"))
    user_duration = int(input("What was the duration of the loan????"))
    number_payments = int(calculate_monthly_payment(user_principal,user_annual_interest_rate,user_duration))
    rem_bal =remainigg_balance(number_payments)
    print("Your Monthly Payment will be : "+ str(number_payments))
    print("Your Remainig Balance ins  : "+ str(rem_bal))
    user_input = int(input("Do you need to calculate more?? Press 1 for Yes and 0 for No :"))
    if user_input == 0:
        print("Thank you for using this Awesome App!!! Byee Byeeee!!!!")
    else:
        print("WLet do it all over again " + name_user)
