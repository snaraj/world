"""
Base settings to build other settings files upon.
"""

from pathlib import Path

import sqlite3

# Grab the path to the ROOT_DIR
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# Define connection (db name)
connection = sqlite3.connect('civilization.db')
# Define cursor, used to interact with the db through sql commands.
cursor = connection.cursor()

# Creating a basic Human Table.
create_human_table = """CREATE TABLE IF NOT EXISTS
human(human_identifier TEXT PRIMARY KEY, name VARCHAR, age VARCHAR)"""
cursor.execute(create_human_table)

# Creating a basic Tribe Table.
create_tribe_table = """CREATE TABLE IF NOT EXISTS
tribe(tribe_identifier INTEGER PRIMARY KEY, name TEXT, population VARCHAR,
name_of_founder TEXT, roles_directory TEXT)"""
cursor.execute(create_tribe_table)