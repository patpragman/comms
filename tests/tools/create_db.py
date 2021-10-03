# create a database if it's not already there
import sqlite3
import config


pwd_context = config.Config.pwd_context
path = config.DatabaseConfig.path

# first, make a database in the main directory of the app
create_users_table_sql = """
                        CREATE TABLE users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                        );
                        """

create_messages_table_sql = """
                        CREATE TABLE messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender TEXT NOT NULL,
                        recipient TEXT NOT NULL,
                        datetime TEXT NOT NULL
                        );
"""

connection = sqlite3.connect(path)
cursor = connection.cursor()
cursor.execute(create_users_table_sql)
cursor.execute(create_messages_table_sql)
connection.commit()
connection.close()

