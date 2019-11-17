import sqlite3
from datetime import  datetime

from env import *

now = datetime.now()

def conn_db():
	try:
		conn= sqlite3.connect('discord.db')
	except Exception as e:
		raise e
	return conn

def insert_sqlite(message,key):
	conn =conn_db()
	query = "INSERT INTO discord (NAME,KEYWORD,Timestamp) VALUES (" +"'"+message +"'" +", "+ "'"+key + "'"+", "+ "'"+str(now) +"'"+")"
	conn.execute(query)
	conn.commit()

def show_recent(key,user):
	conn = conn_db()
	conn= conn.cursor()
	query = "SELECT KEYWORD FROM discord WHERE  NAME = "+ "'"+user +"'"+ " AND KEYWORD LIKE  "+"'%"+key+"%'" 
	#query= "SELECT KEYWORD FROM discord WHERE KEYWORD LIKE "  + ("'%"+key+"%'")
	conn.execute(query)
	row  = conn.fetchall()
	result=''
	for i in row:
		result= i[0] +' , '+ result
	return result

def call_search_api(key):
	from googleapiclient.discovery import build
	service = build(search, "v1",developerKey=developerKey)
	res = service.cse().list(q=key,cx=cx,).execute()
	result = ''
	for item in res['items']:
		data = item['formattedUrl']
		result= data + result
	return result
