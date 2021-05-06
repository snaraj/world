"""
Base settings to build other settings files upon.
"""

import psycopg2
from psycopg2 import OperationalError

from pathlib import Path

# Grab the path to the ROOT_DIR
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# Connecting to the database
def create_connection(name, user, password, host, port):
	# Creating the pointer object for interacting with the db.
	connection = None
	try:
		connection = psycopg2.connect(
				database = name,
				user = user,
				password = password,
				host = host,
				port = port
			)
		print(f'Connection to database: {name} is succesful.')
	except OperationalError as e:
		print(f'The error {e} occured.')
	#returns the pointer object.
	return connection

# Executing queries to the DB.
def execute_query(connection, query):
	connection.autocommit = True
	cursor = connection.cursor()
	try:
		# Executes the given query
		cursor.execute(query)
		print(f'Query {query} was succesfully executed.')
	except OperationalError as e:
		print(f'The error{e} occured.')










