import numpy as np
import matplotlib.pyplot as plt

NUM_OF_ITERATION = 100

inputFile = open('housing.data')
line = inputFile.readlines();

tax = []
price = []

w0 = 1
w1 = 1
alpha = 0.001

for i in range(NUM_OF_ITERATION):
	for l in line:
		detail = l.split()

		xTax = float(detail[2])
		yPrice = float(detail[13])

		tax.append(xTax)
		price.append(yPrice)


		w0 = w0 + alpha * (yPrice - (w1 * xTax + w0))
		w1 = w1 + alpha * (yPrice - (w1 * xTax + w0)) * xTax


hwx = []
x = np.arange(0, int(max(tax)))
hwx = w1 * x + w0

print("hw(x) = " + str(w1) + " * x + " + str(w0))

plt.plot(x, hwx)
plt.plot(tax, price, ".")
plt.xlabel('tax')
plt.ylabel('price')
plt.grid(True)
plt.show()
