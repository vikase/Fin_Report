import matplotlib.pyplot as plt
import seaborn
import uuid
from matplotlib.dates import DateFormatter


class Plotter(object):

	def __init__(self):
		pass


	def make_message_trends(self, volume_trends, title, path):
		weekFormatter = DateFormatter('%b %d')
		fig, ax = plt.subplots()
		ax.xaxis.set_major_formatter(weekFormatter)

		img = dict(title = title, path = path, cid = str(uuid.uuid4()))

		days, msgs, threads, agents, customers = zip(*volume_trends)

		plt.title(title)
		plt.xlabel("Day")
		plt.ylabel("No. of messages")

		plt.plot(days, msgs)

		plt.savefig(path)
		plt.close()

		return img

	def make_customer_trends(self, volume_trends, title, path):
		weekFormatter = DateFormatter('%b %d')
		fig, ax = plt.subplots()
		ax.xaxis.set_major_formatter(weekFormatter)

		img = dict(title = title, path = path, cid = str(uuid.uuid4()))

		days, msgs, threads, agents, customers = zip(*volume_trends)

		plt.title(title)
		plt.xlabel("Day")
		plt.ylabel("No. of customers")

		plt.plot(days, customers)

		plt.savefig(path)
		plt.close()

		return img

	def make_thread_trends(self, volume_trends, title, path):
		weekFormatter = DateFormatter('%b %d')
		fig, ax = plt.subplots()
		ax.xaxis.set_major_formatter(weekFormatter)

		img = dict(title = title, path = path, cid = str(uuid.uuid4()))

		days, msgs, threads, agents, customers = zip(*volume_trends)

		plt.title(title)
		plt.xlabel("Day")
		plt.ylabel("No. of threads")

		plt.plot(days, threads)

		plt.savefig(path)
		plt.close()

		return img

	