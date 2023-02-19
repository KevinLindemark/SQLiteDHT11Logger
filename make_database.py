import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('sensor.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the DHT11TABLE table if already exists.
#cursor_obj.execute("DROP TABLE IF EXISTS DHT11TABLE")
 
# Creating table
table = """ CREATE TABLE IF NOT EXISTS "DHT11TABLE"(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    DATETIME TEXT,
    TEMPERATURE REAL,
    HUMIDITY REAL);
 """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()