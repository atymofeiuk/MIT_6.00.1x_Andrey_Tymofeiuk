# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 23:23:12 2017

MIT 6.00.1x course on edX.org: PSet2 P3

Task:
    
Well then, how can we calculate a more accurate fixed monthly payment than
we did in Problem 2 without running into the problem of slow code? We can make
this program run faster using a technique introduced in lecture - bisection 
search!

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""    
# Andrey Tymofeiuk: balance, monthlyPaymentRate and annualInterestRate are
# given by edX grader

#Andrey Tymofeiuk: Defining necessary constants and variables
monthlyInterestRate = annualInterestRate/12
lower_bound = round(balance//12,2)
upper_bound = round((balance*(1+monthlyInterestRate)**12)//12.0,2)
epsilon = 0.1
b0 = balance
annual_payment = 0
monthly_payment = 0

# Andrey Tymofeiuk: BISECTION SEARCH!

#Andrey Tymofeiuk: Using flags to mark what bound to move
flagLow = False
flagUp = False

#Andrey Tymofeiuk: Infinite loop until the balance-0 becomes less than epsilon
while True:
    balance = b0
    flagLow = False
    flagUp = False
    monthly_payment = lower_bound + (upper_bound - lower_bound)/2
    for month in range(12):
        balance -= monthly_payment
        if balance < 0 and abs(balance - 0) > epsilon and month == 11:
            flagUp = True
            break
        if balance > 0 and abs(balance - 0) > epsilon and month == 11:
            flagLow = True
            break
        if ((balance < 0 and abs(balance-0) <= epsilon) or (balance > 0 and abs(balance-0) <= epsilon)): 
            break
        balance += balance*monthlyInterestRate
    if ((balance < 0 and abs(balance-0) <= epsilon) or (balance > 0 and abs(balance-0) <= epsilon)): 
        break    
    if flagUp == True:
        upper_bound = lower_bound + (upper_bound - lower_bound)/2
    if flagLow == True:
        lower_bound = lower_bound + (upper_bound - lower_bound)/2
                
print("Lowest Payment: " + str(round(monthly_payment,2)))
