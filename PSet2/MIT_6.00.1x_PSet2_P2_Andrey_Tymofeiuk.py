# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 23:05:03 2017

MIT 6.00.1x course on edX.org: PSet2 P2

@author: Andrey
"""

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