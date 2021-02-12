import dbcreds
import mariadb
import sys

conn = mariadb.connect(
    user = dbcreds.user,
    password = dbcreds.password,
    host = dbcreds.host,
    port = dbcreds.port,
    database = dbcreds.database    
)
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO blog_post (username, content) VALUES ('Howard', 'HoHo')",
)

conn.commit()
cursor.close()
conn.close()