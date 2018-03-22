import pylab as plt

# mySamples = []
# myLinear = []
# myQuadratic = []
# myCubic = []
# myExponential = []
#
# for i in range(0, 30):
#     mySamples.append(i)
#     myLinear.append(i)
#     myQuadratic.append(i**2)
#     myCubic.append(i**3)
#     myExponential.append(1.5**i)
#
# plt.figure('lin quad')
# plt.title('Linear vs Quadratic')
# plt.ylim(0, 1000)
# plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth = 2.0)
# plt.plot(mySamples, myQuadratic, 'r-', label='quadratic', linewidth = 3.0)
# plt.legend(loc='upper left')
# plt.show()
# plt.clf()
#
# plt.figure('cub exp')
# plt.xlabel('sample')
# plt.ylabel('functions')
# plt.subplot(121)
# plt.ylim(0, 140000)
# plt.plot(mySamples, myCubic, 'g^', label='cubic')
# plt.subplot(122)
# plt.ylim(0, 140000)
# plt.plot(mySamples, myExponential, 'r--', label='exponential')
# plt.legend()
# plt.show()
# plt.clf()
#
# plt.figure('cube exp log')
# plt.plot(mySamples, myCubic, 'r--', label='cubic')
# plt.plot(mySamples, myExponential, 'k--', label='exponential')
# plt.yscale('log')
# plt.legend()
# plt.title('Cubic vs Exponential')
# plt.show()
# plt.clf()

# ------------------------------------------

# calculate compound interest
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for m in monthlies:
        x, y = retire(m, rate, terms)
        plt.plot(x, y, label='retire:'+str(m))
        plt.legend(loc='upper left')
    plt.show()

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for r in rates:
        x, y = retire(month, r, terms)
        plt.plot(x, y, label='retire'+str(month)+':'+str(int(r*100))+'%')
    plt.legend(loc='upper left')
    plt.show()

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12) # last 10 years of investment
    monthLabels = ['r', 'b', 'g', 'k'] # different colors for monthlies
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        m = monthlies[i]
        mLabel = monthLabels[i % len(monthLabels)] # modular so if list increases it fits
        for j in range(len(rates)):
            r = rates[j]
            rLabel = rateLabels[j % len(rateLabels)] # modular so if list increases it fits
            x, y = retire(m, r, terms)
            plt.plot(x, y, mLabel+rLabel, label='retire' + str(m) + ':' + str(int(r * 100)) + '%')
    plt.legend(loc='upper left')
    plt.show()


displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)
displayRetireWRates(800, [.03, .05, .07], 40*12)
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)