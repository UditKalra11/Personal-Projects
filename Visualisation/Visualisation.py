import numpy as np

import matplotlib.pyplot as plt

month_number=[1,2,3,4,5,6,7,8,9,10,11,12]

facecream=[2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]

facewash=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]

toothpaste=[5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]

bathingsoap=[9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]

shampoo=[1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]

moisturizer=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]

total_units=[21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020]

total_profit=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]

plot1=plt.figure(1)
plt.plot(month_number,total_profit,c='r',ls='--',marker='o',mfc='black')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title('Company Sales data of last year')

plt.legend(["Profit"],loc='lower right')

plt.xticks(range(13))
plt.yticks([100000, 200000, 300000, 400000, 500000])


plot2=plt.figure(2)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])

plt.plot(month_number,facewash,label='Facewash')
plt.plot(month_number,toothpaste,label='Toothpaste')
plt.plot(month_number,bathingsoap,label='Soap')

col=np.array(range(12))

plt.scatter(month_number,facecream,c=col, cmap='viridis',label='Facecream')

plt.legend()
plt.show()