#-*- coding: utf-8 -*-
from win10toast import ToastNotifier
import sqlite3
import random
from time import sleep

DB_PATH = 'persistence/recordatorios.db'
ICON = ''
NOTIFICATION_DURATION = 5*60 # 5 minutes
NOTIFICATION_INTERVAL = 20*60 # 20 minutes
PROCESS_LIST = [
	"League of Legends.exe",
	"csgo.exe"
]


def main():
	#Create the connection object
	con = sqlite3.connect(DB_PATH)
	cursor = con.cursor()
	while True:
		#Get the max number of memories
		memories_count = getMemoriesCount(con,cursor)
		# Creating an array with all the ids of the memories 
		items = [x for x in range(1,memories_count+1)]
		while len(items)>0:
			# Check if another memory was added
			if(getMemoriesCount(con,cursor)!=memories_count):
				break
			random.shuffle(items)
			cat, title, desc = getInfo(con,cursor,items[0])
			items = items[1:]
			showNotification(cat,title,desc)
			sleep(NOTIFICATION_INTERVAL)
	con.close()

def getMemoriesCount(con, cursor):
	sql = "SELECT COUNT(*) FROM memories"
	cursor.execute(sql)
	con.commit()
	for i in cursor:
		cnt = i[0]
	return cnt

def getInfo(con, cursor, id):
	sql = """SELECT categories.name, memories.title, memories.desc 
			FROM memories, categories 
			WHERE memories.id = ? and memories.category = categories.id"""
	cursor.execute(sql,[id])
	con.commit()
	return cursor.fetchone()

def showNotification(category, title, desc):
	toaster = ToastNotifier()
	toaster.show_toast(
		category,
		title+": "+desc,
		duration=NOTIFICATION_DURATION
	)


if __name__ == '__main__':
	#args = sys.argv[1]
	main()
