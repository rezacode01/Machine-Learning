import numpy as np
import matplotlib.pyplot as plt

NUM_OF_ITERATION = 5

def lossFunction():
	sum = 0
	for l in line:
		detail = l.split()

		xCrime = float(detail[0])
		yPrice = float(detail[13])

		hwx = w1 * xCrime + w0
		sum += (hwx - yPrice) ** 2
	return sum / (2 * len(line))

inputFile = open('housing.data')
line = inputFile.readlines();

crime = []
price = []
lossArray = []

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

		lossArray.append(lossFunction())

plt.plot(lossArray)
plt.xlabel('iteration')
plt.ylabel('loss')
plt.grid(True)
plt.show()
