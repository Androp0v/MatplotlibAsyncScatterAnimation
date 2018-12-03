import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
from matplotlib.animation import FuncAnimation
import time

#Set-up the queue for listening to the data stream
queue = mp.Queue()

#Funcion where data is retrieved. Here, as an example, random gaussian distribution centered in (0,0)
def numGen(queue):
	while True:
		x = np.random.normal(loc = 0, scale = 0.3)
		y = np.random.normal(loc = 0, scale = 0.3)
		#Put generated data in the queue
		queue.put((x,y))


if __name__ == '__main__':
	#Store all read data
	dataX = []
	dataY = []

	# Create new Figure and set axis
	fig, ax = plt.subplots()
	ax.set_xlim(-1, 1) 
	ax.set_ylim(-1, 1)

	# Construct the scatter plot which we will update during animation, initialized empty
	scatter, = ax.plot([],[], marker = 'o', ls = '', alpha = 1.0, markeredgewidth = 0)

	#Define the function that will update the scatter plot
	def update(frame_number):
		#Read data from the queue
		data = queue.get()
		x = data[0]
		y = data[1]
		print((x,y))
		dataX.append(x)
		dataY.append(y)
		scatter.set_data(dataX, dataY)
		return scatter,

	#Launch the asynchronous process for generating/reading data and putting it in the queue
	process = mp.Process(target = numGen, args = (queue,))
	process.start()

	#Construct the animation, using the update function as the animation director
	animation = FuncAnimation(fig, update, interval=1, blit = True) #Blit enabled updates the plot without redrawing the whole image
	plt.show()