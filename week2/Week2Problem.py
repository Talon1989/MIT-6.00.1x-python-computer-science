annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def balanceAfterOneYear(balance):
    monthlyInterestRate = annualInterestRate / 12
    for i in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * balance;
        monthlyUnpaidBalance = balance - minimumMonthlyPayment;
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance);
        print(balance)
    print("Remaining balance:", round(balance, 2));


def minimumFixedAnnualPayment(balance):
    monthlyInterestRate = annualInterestRate / 12
    fixedMonthlyPayment = 0;
    temp_balance = balance;
    while True:
        for i in range(12):
            temp_balance = temp_balance - fixedMonthlyPayment + ((temp_balance - fixedMonthlyPayment) * monthlyInterestRate);
        if temp_balance > 0:
            temp_balance = balance;
            fixedMonthlyPayment += 10;
        else:
            break;
    print("Lowest Payment:", fixedMonthlyPayment)


def fasterMinimumFixedAnnualPayment(balance):
    epsilon = 0.01
    monthlyInterestRate = annualInterestRate / 12
    lower = balance / 12
    upper = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
    temp_balance = balance;
    while abs(temp_balance) > epsilon:
        fixedMonthlyPayment = (lower + upper) / 2;
        temp_balance = balance;
        for i in range(12):
            temp_balance = temp_balance - fixedMonthlyPayment + ((temp_balance - fixedMonthlyPayment) * monthlyInterestRate);
        if temp_balance > epsilon:
            lower = fixedMonthlyPayment
        elif temp_balance < -epsilon:
            upper = fixedMonthlyPayment
    print("Lowest Payment:", round(fixedMonthlyPayment, 2))


fasterMinimumFixedAnnualPayment(999999);