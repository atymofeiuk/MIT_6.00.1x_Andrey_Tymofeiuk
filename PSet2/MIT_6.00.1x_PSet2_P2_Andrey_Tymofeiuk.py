# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 23:05:03 2017

MIT 6.00.1x course on edX.org: PSet2 P2

Task:

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
# Andrey Tymofeiuk: balance, monthlyPaymentRate and annualInterestRate are
# given by edX grader
monthlyInterestRate = annualInterestRate/12
b0 = balance
lowest_payment = 0

while balance > 0:
    balance = b0
    for cf_month in range(12):
        balance -= lowest_payment
        balance += balance*monthlyInterestRate
    if balance == 0 or balance < 0:
        break
    lowest_payment += 10

print("Lowest Payment: " + str(lowest_payment))