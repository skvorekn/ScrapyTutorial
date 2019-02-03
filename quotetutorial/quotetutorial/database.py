import sqlite3

# creates/opens file
conn = sqlite3.connect('myquotes.db')
# can look at with sqliteonline.com

# cursor
curr = conn.cursor()
# add into myquotes.db

# triple quotes for multiple line query
# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#                 )""")

curr.execute("""INSERT INTO quotes_tb VALUES ('Python is awesome!','buildwithpython','python')""")

conn.commit()
conn.close()