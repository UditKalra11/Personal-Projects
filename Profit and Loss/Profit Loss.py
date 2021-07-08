revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expense = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
profit = []
for i in range(12):
    profit.append(revenue[i]-expense[i])

print("Profit : %s"%(profit))

tax =[]
for i in range(12):
    tax.append(0.3*profit[i])

taxround=[]
for i in range(12):
    taxround.append(round(tax[i]))
print("\nTax : %s"%(taxround))

pat=[]
for i in range(12):
    pat.append(profit[i]-taxround[i])
print("\nProfit After Tax : %s"%(pat))

profitmargin=[]
for i in range(12):
    profitmargin.append(pat[i]/revenue[i]*100)


pmr=[]
for i in range(12):
    pmr.append(round(profitmargin[i]))

print("\nProfit Margin : %s" %(pmr))

mean=sum(pat)/len(pat)
print("\nGood Months:")
for i in range(12):
    if mean>pat[i]:
        print(i,end=",")
print("\nBad Months:")
for i in range(12):
    if mean<pat[i]:
        print(i,end=",") 