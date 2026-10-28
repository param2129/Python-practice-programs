income = float(input("Enter your income => "))

tax = 0.0
remaining = income

while remaining > 200000:
    if remaining > 1000000:
        tax += (remaining - 1000000) * 0.15
        remaining = 1000000
    elif remaining > 500000:
        tax += (remaining - 500000) * 0.07
        remaining = 500000
    elif remaining > 200000:
        tax += (remaining - 200000) * 0.05
        remaining = 200000

print("Payable Tax =>", tax)

    