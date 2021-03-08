#!/usr/local/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='ping102528',
    database='zack'
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),age INT(5))")

sql = 'insert into student (name,age) values (%s,%s)'
val = ('zack','34')
mycursor.execute(sql,val)

'''
插入多条数据
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)
'''

'''
查询数据
mycursor.execute("SELECT * FROM sites")
 
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
myresult = mycursor.fetchone()     # fetchone() 读取一条数据
 
for x in myresult:
  print(x)
'''

mydb.commit() # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")
#数据记录插入后，获取该记录的 ID  print("1 条记录已插入, ID:", mycursor.lastrowid)