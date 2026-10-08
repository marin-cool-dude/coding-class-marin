sales_total = float(input("Input the sales total for this month."))
bonus = sales_total/0.15
if(sales_total < 40000):
    print("Bonus earned:", bonus)
