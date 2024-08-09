import mysql.connector

conn = mysql.connector.connect(
    user='root', password='12345', host='localhost', database='tushya')
curosr = conn.cursor()
sql = '''
insert into tushya
values(
    'Shamm',
    19,
    'M',
    'Vivek High School'
)
'''

curosr.execute(sql)
conn.commit()
conn.close()
