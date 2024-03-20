##  :Problem statement: ##

#They're in a 12% tax bracket (in other words, 12% of their salary is taken for taxes, and they only take home 88%)
#, and they're paid hourly, at a rate of $15/hour. 40 hours per week...

def get_pay(num_hours):
    pay_pretax   = num_hours * 15
    pay_aftertax = pay_pretax - (pay_pretax * 0.12)
    return(pay_aftertax)

# pay for 40 and 60 hours per week

pay_fulltime = get_pay(40)
print(pay_fulltime)

pay_fulltime = get_pay(60)
print(pay_fulltime)