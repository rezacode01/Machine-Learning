import numpy as np
import matplotlib.pyplot as plt

NUM_OF_ITERATION = 1

def lossFunction():
	sum = 0
	for l in line:
		detail = l.split()

		x = float(detail[2])
		y = float(detail[13])

		hwx = w1 * x + w0
		sum = sum + (hwx - y) ** 2
	return sum / (2 * len(line))

inputFile = open('housing.data')
line = inputFile.readlines();

tax = []
price = []
lossArray = []

w0 = 1
w1 = 1
alpha = 0.001

for i in range(NUM_OF_ITERATION):
	for l in line:
		detail = l.split()

		xtax = float(detail[2])
		yPrice = float(detail[13])

		tax.append(xtax)
		price.append(yPrice)

		w0 = w0 + alpha * (yPrice - (w1 * xtax + w0))
		w1 = w1 + alpha * (yPrice - (w1 * xtax + w0)) * xtax

		# print(str(w1) + " " + str(w0))
		lossArray.append(lossFunction())

plt.plot(lossArray)
plt.xlabel('iteration')
plt.ylabel('loss')
plt.grid(True)
plt.show()
