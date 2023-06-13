import pymysql

conn = pymysql.connect(
    host='sql9.freesqldatabase.com',
    database='sql9625882',
    user='sql9625882',
    password='upYjSe6z46',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer AUTO_INCREMENT PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()
