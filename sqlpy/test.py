import sqlhandler as sh










if __name__ == '__main__':
	data1=sh.select("select * from table1") 
	data2=sh.insert("insert into table1 value(NULL,'student') ")
	data3=sh.modify("update table1 set name='Teacher' where id =1")  
	print(data1,data2,data3)
