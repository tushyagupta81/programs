import mysql.connector

conn = mysql.connector.connect(
    user='root', password='12345', host='localhost', database='tushya')
curosr = conn.cursor()
sql = '''
update tushya
set age = 17
where name = 'Tushya'
'''

curosr.execute(sql)
conn.commit()
conn.close()
