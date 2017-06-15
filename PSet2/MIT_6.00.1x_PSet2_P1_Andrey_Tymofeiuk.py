# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:42:15 2017

MIT 6.00.1x course on edX.org: PSet2 P1

@author: Andrey Tymofeiuk
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
monthlyInterestRate = annualInterestRate/12 

for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate

print("Remaining balance: " + str(round(balance,2)))            