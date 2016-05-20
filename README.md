# Fin_Report

Runs analytics on postgres database of ~29 days of messages between 
Fin customers and agents and emails results to specified address.

fin.py runs and puts together the results of the following files:
1. sql_fin.py - queries postgres database 
2. plot_fin.py - creates image files of charts
3. email_fin.py - sends email with embedded charts and other analytics

A copy of the resulting email as of 5/29 is also included as fin_email.pdf.


##PostGres

Assumes postgres database is named 'Vikas' and user is 'Vikas'

postgres database details:
	table: 'messages'
	columns: 'id', 'user_id', 'agent_id', 'created_at', 'message_thread_id'

##Email

Current sender and recipient are set in email_fin.py.

	self.gmail_user = 'vikasfintest123@gmail.com'
	self.gmail_pwd = 'sativfintest123'
	self.to_email = 'vikase@gmail.com'


