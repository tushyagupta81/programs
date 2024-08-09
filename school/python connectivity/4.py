import mysql.connector

conn = mysql.connector.connect(
    user='root', password='12345', host='localhost', database='tushya')
curosr = conn.cursor()
sql = '''
select * from tushya
'''

curosr.execute(sql)
print(curosr.fetchall())
conn.commit()
conn.close()
