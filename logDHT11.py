import sqlite3
import datetime
import dht11Sens
from time import sleep

def insertDHTDATA():
    try:
        conn = sqlite3.connect('sensor.db')
        query ='INSERT INTO DHT11TABLE (DATETIME, TEMPERATURE, HUMIDITY)VALUES(?,?,?)'
        temp, hum = dht11Sens.getDht11Data()
        sleep(1)
        data = (datetime.datetime.now(), temp, hum)
        print(f"Inserting data: {data}")
        cur = conn.cursor()
        cur.execute(query, data)
        rowid = cur.lastrowid
    # Auto incremented/assigned id
        print(f'id of last row insert = {rowid}')
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f'Could not insert ! {e}')
    finally:
        conn.close()

while True:
    try:
        insertDHTDATA()
        sleep(10)
    except:
        print("Error")
