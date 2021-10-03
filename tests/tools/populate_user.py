# create abunch of users
import sqlite3
import config

sql = config.DatabaseConfig.user_upsert_sql

tuple_list = [("user_" + str(i), config.Config.pwd_context.hash(str(i))) for i in range(0, 100)]
conn = sqlite3.connect("../../" + config.DatabaseConfig.path)
cur = conn.cursor()
for tupl in tuple_list:
    cur.execute(config.DatabaseConfig.add_user_sql, tupl)

conn.commit()
conn.close()
