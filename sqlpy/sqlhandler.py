#!/usr/bin/env Python
# coding=utf-8

from connectsql import * 


def select(sql):
	try:
		cur.execute(sql)
		lines=cur.fetchall()
		return lines
	except Exception as e:
		print(e)
		return -1


def insert(sql):
	try:
		cur.execute(sql)
		conn.commit()
		return 0
	except Exception as e:
		print(e)
		return -1

def modify(sql):
	try:
		cur.execute(sql)
		conn.commit()
		return 0
	except Exception as e:
		print(e)
		return -1





if __name__== '__main__':
	data1=select("select * from table1")
	data2=insert("insert into table1 value(NULL,'student') ")
	data3=modify("update table1 set name='Teacher' where id =1")
	print(data1,data2,data3)
	
