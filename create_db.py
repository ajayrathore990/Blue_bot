import sqlite3

conn = sqlite3.connect('discord.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE discord
         (ID INTEGER PRIMARY KEY,
         NAME           TEXT    NOT NULL,
         KEYWORD        TEXT     NOT NULL,
         Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
         );''')
print("Table created successfully")

conn.close()