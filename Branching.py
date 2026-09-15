hours = int(input('Enter the KW hours used: '))

if(hours <= 1000):
    amountO = (hours * 0.07633)
else:
    amountO = (hours * 0.09259)

print("Amount owed is", amountO)

