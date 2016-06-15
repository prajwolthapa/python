# Finance Application
up_eqn=(float(4.5)/100)*(1+float(4.5)/100)**5
down_eqn=((1+float(4.5)/100)**5 -1)
monthly_eqn = (1000.0 * up_eqn/down_eqn)/int(12)
print(monthly_eqn)




