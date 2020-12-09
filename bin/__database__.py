import sqlite3 as sq

conn = sq.connect('./bin/test.db')
conn.close()