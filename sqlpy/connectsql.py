#!/usr/bin/env Python
#coding=utf-8

from configparser import ConfigParser
import pymysql

cp=ConfigParser()
cp.read("mysql.conf")
host=cp.get("mysql","db_host")
port=int(cp.get("mysql","db_port"))
user=cp.get("mysql","db_user")
passwd=cp.get("mysql","db_password")
database=cp.get("mysql","db_database")


conn=pymysql.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset="utf8") #connect object

cur=conn.cursor()












print("hello,world")
