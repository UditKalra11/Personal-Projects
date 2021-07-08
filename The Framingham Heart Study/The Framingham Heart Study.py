import pandas as pd
stats=pd.read_csv("C:\\Users\\hp\\Desktop\\framingham.csv")

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='education',data=stats)
plot1=plt.figure(1)


sns.catplot(x='TenYearCHD',y='cigsPerDay',kind='bar',data=stats)
plot2=plt.figure(2)


plot3=plt.figure(3)
sns.boxplot(x='TenYearCHD',y='age',hue='currentSmoker',data=stats)
plt.legend()


plot4=plt.figure(4)
sns.boxplot(x='TenYearCHD',y='age',hue='prevalentStroke',data=stats)
plt.legend()


plot5=plt.figure(5)
sns.boxplot(x='TenYearCHD',y='age',hue='diabetes',data=stats)
plt.legend()


plot6=plt.figure(6)
sns.boxplot(x='TenYearCHD',y='totChol',data=stats)


sns.catplot(x='TenYearCHD',y='sysBP',kind='bar',data=stats)
plot7=plt.figure(7)


sns.catplot(x='TenYearCHD',y='diaBP',kind='bar',data=stats)
plot8=plt.figure(8)


sns.catplot(x='TenYearCHD',y='BMI',kind='bar',data=stats)
plot9=plt.figure(9)

sns.catplot(x='TenYearCHD',y='BPMeds',kind='bar',data=stats)
plot10=plt.figure(10)

plt.show()
