import cgi
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header
import os
import smtplib
from email.MIMEBase import MIMEBase
from email import Encoders


class Emailer(object):
	def __init__(self):
		self.gmail_user = 'vikasfintest123@gmail.com'
		self.gmail_pwd = 'sativfintest123'
		self.to_email = 'vikase@gmail.com'

	def attach_image(self, img_dict):
	    with open(img_dict['path'], 'rb') as file:
	        msg_image = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
	        msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
	    return msg_image

	# def attach_file(filename):
	#     part = MIMEBase('application', 'octect-stream')
	#     part.set_payload(open(filename, 'rb').read())
	#     Encoders.encode_base64(part)
	#     part.add_header('Content-Disposition', 'attachment; filename=%s' % os.path.basename(filename))
	#     return part

	def generate_email(self, image_list):   #gmail_user, to_list, img1,img2):
	    '''
	    For attachments:
	        unblock attach_file method above.
	        add back data_path_1, data_path_2 above to allow generate_email to add attachments.
	        email_msg = generate_email(gmail_user, [to_email], 'test_data.txt', 'test_data_2.txt', img1, img2).
	        add msg.attach(attach_file(data_path_1)), etc. below.
	    '''
	    
	    msg =MIMEMultipart('related')
	    msg['Subject'] = Header(u'Fin Daily Metrics', 'utf-8')
	    msg['From'] = self.gmail_user
	    msg['To'] = ','.join([self.to_email])

	    msg_alternative = MIMEMultipart('alternative')
	    msg_text = MIMEText(u'Image not working - maybe next time', 'plain', 'utf-8')
	    msg_alternative.attach(msg_text)
	    msg.attach(msg_alternative)

	    msg_html = u'<h1>Benchmark Performance</h1>'
	    for image in image_list:
	    	msg_html += u'<h3></h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(image['title'], quote=True), **image)
	    
	    msg_html = MIMEText(msg_html, 'html', 'utf-8')
	    msg_alternative.attach(msg_html)

	    for image in image_list:
	    	msg.attach(self.attach_image(image))

	    return msg

	def send_email(self, msg):
	    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
	    mailServer.ehlo()
	    mailServer.starttls()
	    mailServer.ehlo()
	    mailServer.login(self.gmail_user, self.gmail_pwd)
	    mailServer.sendmail(self.gmail_user, self.to_email, msg.as_string())
	    mailServer.quit()






###LEGACY

# self.gmail_user = 'vikasfintest123@gmail.com'
# self.gmail_pwd = 'sativfintest123'
# self.to_email = 'vikase@gmail.com'

# def attach_image(img_dict):
# 	with open(img_dict['path'], 'rb') as file:
# 	    msg_image = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
# 	    msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
# 	return msg_image

# 	# def attach_file(filename):
# 	#     part = MIMEBase('application', 'octect-stream')
# 	#     part.set_payload(open(filename, 'rb').read())
# 	#     Encoders.encode_base64(part)
# 	#     part.add_header('Content-Disposition', 'attachment; filename=%s' % os.path.basename(filename))
# 	#     return part

# def generate_email(image_list):   #gmail_user, to_list, img1,img2):
# 	'''
# 	For attachments:
# 	    unblock attach_file method above.
# 	    add back data_path_1, data_path_2 above to allow generate_email to add attachments.
# 	    email_msg = generate_email(gmail_user, [to_email], 'test_data.txt', 'test_data_2.txt', img1, img2).
# 	    add msg.attach(attach_file(data_path_1)), etc. below.
# 	'''

# 	msg =MIMEMultipart('related')
# 	msg['Subject'] = Header(u'Images and Words', 'utf-8')
# 	msg['From'] = gmail_user
# 	msg['To'] = ','.join([to_email])

# 	msg_alternative = MIMEMultipart('alternative')
# 	msg_text = MIMEText(u'Image not working - maybe next time', 'plain', 'utf-8')
# 	msg_alternative.attach(msg_text)
# 	msg.attach(msg_alternative)

# 	msg_html = u'<h1>Some images coming up</h1>'
# 	for image in image_list:
# 		msg_html += u'<h3>Image</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(image['title'], quote=True), **image)

# 	msg_html = MIMEText(msg_html, 'html', 'utf-8')
# 	msg_alternative.attach(msg_html)

# 	for image in image_list:
# 		msg.attach(attach_image(image))

# 	return msg

# def send_email(self, msg):
# 	mailServer = smtplib.SMTP('smtp.gmail.com', 587)
# 	mailServer.ehlo()
# 	mailServer.starttls()
# 	mailServer.ehlo()
# 	mailServer.login(gmail_user, gmail_pwd)
# 	mailServer.sendmail(gmail_user, to_list, msg.as_string())
# 	mailServer.quit()




# import smtplib

# class Emailer(object):
# 	def __init__(self):
# 		self.to = 'vikase@gmail.com'

# 		self.gmail_user = 'vikasfintest123@gmail.com'
# 		gmail_pwd = 'sativfintest123'

# 		self.smtpserver = smtplib.SMTP("smtp.gmail.com",587)
# 		self.smtpserver.ehlo()
# 		self.smtpserver.starttls()
# 		self.smtpserver.ehlo
# 		self.smtpserver.login(self.gmail_user, gmail_pwd)

# 		self.header = 'To:' + self.to + '\n' + 'From: ' + self.gmail_user + '\n' + 'Subject:testing \n'
# 		print self.header

# 	def get_header(self):
# 		return self.header

# 	def send_mail(self, msg): 
# 		self.smtpserver.sendmail(self.gmail_user, self.to, msg)
# 		print 'done!'

# 	def close(self):
# 		self.smtpserver.close()



