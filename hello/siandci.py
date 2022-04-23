# Simple and Compound Interest
principal = float(input('Enter amount: '))
time = float(input('Enter time (in years): '))
rate = float(input('Enter rate (in percentage ): '))
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)
print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))
