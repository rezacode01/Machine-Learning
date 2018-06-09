import numpy as np
import matplotlib.pyplot as plt


inputFile = open('housing.data')
line = inputFile.readlines();

tax = []
price = []

for l in line:
	detail = l.split()
	# print(detail[9])
	# print(detail[13])

	tax.append(float(detail[9]))
	price.append(float(detail[13]))


plt.plot(tax, price, ".")
plt.xlabel('tax')
plt.ylabel('price')
plt.show()
