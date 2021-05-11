'''
	Defines the queries to create tables neccesary.
'''
from config.settings.base import create_connection, execute_query

connection = create_connection('world', '', 'user', '127.0.0.1', '5432')

# Add tables here 