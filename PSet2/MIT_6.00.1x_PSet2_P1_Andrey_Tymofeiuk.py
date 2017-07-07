# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:42:15 2017

MIT 6.00.1x course on edX.org: PSet2 P1

Task: 
    
Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""	      
# Andrey Tymofeiuk: balance, monthlyPaymentRate and annualInterestRate are
# given by edX grader
monthlyInterestRate = annualInterestRate/12 

for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate

print("Remaining balance: " + str(round(balance,2)))            