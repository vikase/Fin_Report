'''
Runs analytics on postgres database of ~29 days of messages between 
Fin customers and agents and emails results to specified address.

fin.py runs and puts together the results of the following files:
1. sql_fin.py - queries postgres database 
2. plot_fin.py - creates image files of charts
3. email_fin.py - sends email with embedded charts and other analytics


'''

import os
import cgi
import uuid

import email_fin
import sql_fin
import plot_fin

emailUtil = email_fin.Emailer()
sqlUtil = sql_fin.Queries()
plotUtil = plot_fin.Plotter()


def volume_trends():
	'''
	purpose:
		Track use of Fin over time
	output:
		volume_trends.png
	'''
	volume_trend_imgs = []

	volume_trends = sqlUtil.get_volume_trends()

	#Message Trends
	title = "Messages per day"
	path = 'message_trends.png'


	img = plotUtil.make_message_trends(volume_trends, title, path)
	volume_trend_imgs.append(img)

	#Customer Trends
	title = "Customers per day"
	path = 'customer_trends.png'

	img = plotUtil.make_customer_trends(volume_trends, title, path)
	volume_trend_imgs.append(img)

	#Thread Trends
	title = "Threads per day"
	path = 'thread_trends.png'

	img = plotUtil.make_thread_trends(volume_trends, title, path)
	volume_trend_imgs.append(img)

	return volume_trend_imgs


def main(): 
	#Initialize charts
	image_list = []

	#Run analytics, create charts
	image_list += volume_trends()
	print image_list

	#Generate and send email
	msg = emailUtil.generate_email(image_list)
	emailUtil.send_email(msg)

	#Clean-up
	for image in image_list:
		os.remove(image['path'])

	sqlUtil.close()


if __name__=='__main__': 
	main()




