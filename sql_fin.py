import psycopg2

'''

Assumes postgres database is named 'Vikas' and user is 'Vikas'

postgres database details:
	table: 'messages'
	columns: 'id', 'user_id', 'agent_id', 'created_at', 'message_thread_id'


'''

class Queries():
	def __init__(self):
		self.conn = psycopg2.connect(dbname='Vikas', user='Vikas')
		self.c = self.conn.cursor()


	def get_volume_trends(self):
		self.c.execute(
			'''SELECT date_trunc('day', created_at) "day", count(id) msgs, 
			count(distinct message_thread_id) threads, count(distinct agent_id) agents,  
			count(distinct user_id) customers from messages group by 1 order by 1;'''
		)

		volume_trends = self.c.fetchall()

		return volume_trends


	def get_users(self):
		self.c.execute(
			'''select count(distinct user_id) total_users from messages;''' 
		)

		return self.c.fetchone()[0]


	# def threads_initated(self):
	# 	self.c.execute(
	# 		'''select count(distinct user_id) total_users from messages;''' 
	# 	)

	# 	return self.c.fetchone()[0]


	def close(self):
		self.c.close()
		self.conn.close()