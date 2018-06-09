import numpy as np
import matplotlib.pyplot as plt

NUM_OF_ITERATION = 10

inputFile = open('housing.data')
line = inputFile.readlines();

crime = []
price = []

w0 = 1
w1 = 1
alpha = 0.001

for i in range(NUM_OF_ITERATION):
	for l in line:
		detail = l.split()

		xCrime = float(detail[0])
		yPrice = float(detail[13])

		crime.append(xCrime)
		price.append(yPrice)


		w0 = w0 + alpha * (yPrice - (w1 * xCrime + w0))
		w1 = w1 + alpha * (yPrice - (w1 * xCrime + w0)) * xCrime

hwx = []
x = np.arange(0, 80)
hwx = w1 * x + w0
# print(hwx)

print("hw(x) = " + str(w1) + "x + " + str(w0))

plt.plot(x, hwx)
plt.plot(crime, price, ".")
plt.xlabel('crime')
plt.ylabel('price')
plt.grid(True)
plt.show()
