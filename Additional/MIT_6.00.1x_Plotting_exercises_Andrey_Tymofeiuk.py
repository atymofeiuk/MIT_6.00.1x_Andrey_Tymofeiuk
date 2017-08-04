# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:58:29 2017

MIT 6.00.1x course on edX.org: Notes from the last Lecture 7: Plotting

"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#first trial
#plt.plot(mySamples, myLinear)
#plt.plot(mySamples, myQuadratic)
#plt.plot(mySamples, myCubic)
#plt.plot(mySamples, myExponential)

#adding figure
#plt.figure('lin')
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.plot(mySamples, myCubic)
#plt.figure('exp')
#plt.plot(mySamples, myExponential)

#adding labels
#plt.figure('lin')
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.plot(mySamples, myLinear)

#we can come back to the figure we want
#plt.figure('quad')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
#plt.figure('quad')
#plt.ylabel('quadratic function')

#adding titles
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')

#adding clf(to clear figure)
#plt.figure('lin')
#plt.clf()
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.clf()
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.clf()
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.clf()
#plt.plot(mySamples, myExponential)
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')

#changing limits on the axis
#plt.figure('lin')
#plt.clf()
#plt.ylim(0, 1000)
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.clf()
#plt.ylim(0, 1000)
#plt.plot(mySamples, myQuadratic)
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')

#overlay the plots
#plt.figure('lin quad')
#plt.clf()
#plt.plot(mySamples, myLinear)
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube exp')
#plt.clf()
#plt.plot(myLinear, myCubic)
#plt.plot(myLinear, myExponential)
#plt.figure('lin quad')
#plt.title('Linear vs Quadratic')
#plt.figure('cube exp')
#plt.title('Cubic vs Exponential')

#adding legends
#plt.figure('lin quad')
#plt.clf()
#plt.plot(mySamples, myLinear, label = 'linear')
#plt.plot(mySamples, myQuadratic, label = 'quadratic')
#plt.legend(loc = 'upper left')
#plt.title('Linear vs Quadratic')
#plt.figure('cube expo')
#plt.clf()
#plt.plot(mySamples, myCubic, label = 'cube')
#plt.plot(mySamples, myExponential, label = 'expo')
#plt.legend()
#plt.title('Cubic vs Exponential')

#changing data display
#plt.figure('lin quad')
#plt.clf()
#plt.plot(mySamples, myLinear, 'b-', label = 'linear')
#plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic')
#plt.legend(loc = 'upper left')
#plt.title('Linear vs Quadratic')
#plt.figure('cube expo')
#plt.clf()
#plt.plot(mySamples, myCubic, 'g^', label = 'cubic')
#plt.plot(mySamples, myExponential, 'r--', label = 'exponential')
#plt.legend()
#plt.title('Cubic vs Exponential')

#changing linewidth
#plt.figure('lin quad')
#plt.clf()
#plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
#plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth = 3.0)
#plt.legend(loc = 'upper left')
#plt.title('Linear vs Quadratic')
#plt.figure('cube expo')
#plt.clf()
#plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
#plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0)
#plt.legend()
#plt.title('Cubic vs Exponential')

#using subplots
#plt.figure('lin quad')
#plt.clf()
#plt.subplot(211)
#plt.ylim(0, 900)
#plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
#plt.subplot(212)
#plt.ylim(0, 900)
#plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth = 3.0)
#plt.legend(loc = 'upper left')
#plt.title('Linear vs Quadratic')
#plt.figure('cube expo')
#plt.clf()
#plt.subplot(121)
#plt.ylim(0, 140000)
#plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
#plt.subplot(122)
#plt.ylim(0, 140000)
#plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0)
#plt.legend()
#plt.title('Cubic vs Exponential')

#changing scales
#plt.figure('cube exp log')
#plt.clf()
#plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
#plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0)
#plt.yscale('log')
#plt.legend()
#plt.title('Cubic vs Exponential')
#plt.figure('cube exp linear')
#plt.clf()
#plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
#plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0)
#plt.legend()
#plt.title('Cubic vs Exponential')

#EXAMPLE
#Goal: planning for retirement
#intend to save an amount of m each month
#expect to earn a percentage r of income on investments each month
#want to explore how big retirement fund will be compounded by time ready to retire

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings
    
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')

#displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(month) + ':' + str(int(rate*100)))
        plt.legend(loc = 'upper left')

#displayRetireWRates(800, [.03, .05, .07], 40*12)

#def displayRetireWMonthsAndRate(monthlies, rates, terms):
#    plt.figure('retireBoth')
#    plt.clf()
#    plt.xlim(30*12, 40*12)
#    for monthly in monthlies:
#        for rate in rates:
#            xvals, yvals = retire(monthly, rate, terms)
#            plt.plot(xvals, yvals, label = 'retire' + str(monthly) + ':' + str(int(rate*100)))
#            plt.legend(loc = 'upper left')
#        
#displayRetireWMonthsAndRate([500, 700, 900, 1100], [.03,.05,.07],40*12)

#visualising separately

def displayRetireWMonthsAndRate(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '-']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire' + str(monthly) + ':' + str(int(rate*100)))
            plt.legend(loc = 'upper left')
        
displayRetireWMonthsAndRate([500, 700, 900, 1100], [.03,.05,.07],40*12)