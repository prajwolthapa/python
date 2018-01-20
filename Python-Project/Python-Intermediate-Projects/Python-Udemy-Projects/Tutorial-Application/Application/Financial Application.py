<<<<<<< HEAD
=======
# # # Finance Application
# # up_eqn=(float(4.5)/100)*(1+float(4.5)/100)**5
# down_eqn=((1+float(4.5)/100)**5 -1)
# monthly_eqn = (1000.0 * up_eqn/down_eqn)/int(12)
# print(monthly_eqn)

# Finance Calculator For Loans Payments Calculations

#
# def subscribe(first_name):

#
#     short_name=input("What is your name??")
#     return  short_name
#
# name = subscribe('short_name')
# print(name)

# Calculator 1


# def calculate_rate_payment(principle,interest_payment,duartion):
#     if interest_payment == 0 :
#         return principle/(duartion*12)
#
#     r= interest_payment/100/12
#     n= duartion*12
#     monthly_payment = principle * (r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
#     return  monthly_payment
#
# payment = calculate_rate_payment (1000.0, 4.5, 5)
#
#
# print("Monthly Payment Based on current inputs = $ "+ str((payment)))

# annual_interest_rate=0
# duration=0
# principal=0
# number_payments=
#

user_principal = float(input("What is your princial amount of the loan????"))
user_annual_interest_rate = float(input("What is your annual interest rate for the loan???"))
user_duration = int(input("What was the duration of the loan????"))
>>>>>>> b2136e858b5073f5887cd22a251ddc3434839540

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
