sales = float(input("Enter your monthly sales in euros:" ))
if (sales > 40000):
    commission = sales * 0.15
else:
    commission = sales * 0.05
print("Your commission for the month is:", commission)