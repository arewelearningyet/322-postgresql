# app/pg_queries.py
## connect to elephantsql-hosted postgresql:

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env vars add them to env

DB_NAME=os.getenv('DB_NAME', default="OOPS")
DB_USER=os.getenv('DB_USER', DEFAULT='OOPS')
DB_PASSWORD=os.getenv('DB_PASSWORD', DEFAULT='OOPS')
DB_HOST=os.getenv('DB_HOST', DEFAULT-'OOPS')

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
print("cursor:", cursor)

# table creation

query = '''
creat table if doesn't exist
'''

cursor.execute('SELECT * from test_table;')

result= cursor.fetchone()
print('result:', result)

#data insertion

insertion_query ="""
insert into test_table (name, data)
values


"""
cursor.execute(insertion_query)

cursor.execute("select * from test_table")
result = cursor.fetchall()
print("result:", len(result))


# actually save the transactions
connection.commit()




