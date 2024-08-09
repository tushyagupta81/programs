import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '12345' , host = 'localhost' , database = 'tushya')
curosr = conn.cursor()
sql = '''
create table tushya(
    name char(25),
    age int,
    gender char(1),
    school char(100)
)
'''
curosr.execute(sql)
conn.commit()
conn.close()
