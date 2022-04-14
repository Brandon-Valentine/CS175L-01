import matplotlib.pyplot as plt

expenses=open('expenses.txt','r')
bills=[]

for line in expenses:
    l=line.rstrip('\n')
    cols=l.split('\t')
    bills.append(cols)
print(bills)

for item in bills:
    print(item[0], item[1])
    
values=[1000,250,350,200,375,800]
names=['Rent','Gas','Food','Clothing','Car Payment','Misc']


plt.pie(values, labels=names)
plt.title('Monthly Expenses')
plt.show()
