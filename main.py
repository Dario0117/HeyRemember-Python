#-*- coding: utf-8 -*-
from win10toast import ToastNotifier
import sqlite3
import random
from time import sleep

DB_PATH = 'persistence/recordatorios.db'
ICON = 'icon.ico'
NOTIFICATION_DURATION = 5*60 # 5 minutes
NOTIFICATION_INTERVAL = 30*60 # 20 minutes

def main():
	con = sqlite3.connect(DB_PATH)
	cursor = con.cursor()
	while True:
		memories_count = getMemoriesCount(con,cursor)
		items = [x for x in range(1,memories_count+1)]
		while len(items)>0:
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
		icon_path=ICON,
		duration=NOTIFICATION_DURATION
	)

if __name__ == '__main__':
	main()
