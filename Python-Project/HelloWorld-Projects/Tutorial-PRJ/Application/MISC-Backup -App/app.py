__author__ = 'pthapax'
def monthly_calc(amt,ir,dur):
    if ir ==0:
        return amt/(dur*12)

    r= ir/100/12
    n= dur*12
    monthly_payment = amt * (r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return  monthly_payment

monthly_payment = int(monthly_calc(1000.0, 10.0, 5))

def rem_bal(amt,ir,dur,pymnt):
    if ir == 0:
        return principal*((1)-(principal/duration))
    rate = ir/100/12.0
    n= dur*12
    p=pymnt
    ramain_bal = amt*((1.0+rate)**n - (1.0+rate)**p) / (((1.0+rate)**n)-1)

    return ramain_bal


"""************************************Main App************************************************"""
amt = float(input("PLease enter your Loan Amt: "))
ir = float(input("Please enter your interest rate: "))
dur = int(input("Please enter your loan duration: "))
pymnt = monthly_calc(amt,ir,dur)

print("LOAN AMOUNT:", amt, "INTEREST RATE (PERCENT):", ir, '\n', "DURATION (YEARS): ", dur, " MONTHLY PAYEMNT: ", pymnt)
for year_number in range(1,dur+1):
    """ First calculate remaing balance"""
    bal = int(rem_bal(amt,ir,dur,year_number*12))
    print("YEAR:", year_number, "BALANCE: ", bal,"TOTAL PAYMENT :", pymnt*year_number*12)
