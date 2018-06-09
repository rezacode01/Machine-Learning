import numpy as np
import matplotlib.pyplot as plt


inputFile = open('housing.data')
line = inputFile.readlines();

crime = []
price = []

for l in line:
	detail = l.split()
	# print(detail[0])
	# print(detail[13])

	crime.append(float(detail[0]))
	price.append(float(detail[13]))

plt.plot(crime, price, ".")
plt.xlabel('crime')
plt.ylabel('price')
plt.show()
