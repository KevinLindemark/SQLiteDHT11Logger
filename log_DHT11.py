import sqlite3
import datetime
import ada_dht
from time import sleep

def insertDHTDATA():
    try:
        conn = sqlite3.connect('sensor.db')
        query ='INSERT INTO DHT11TABLE (DATETIME, TEMPERATURE, HUMIDITY)VALUES(?,?,?)'
        temp, hum = ada_dht.read_sensor()
        if temp != None and hum != None:
            data = (datetime.datetime.now(), temp, hum)
            print(f"Inserting data: {data}")
            cur = conn.cursor()
            cur.execute(query, data)
            rowid = cur.lastrowid
            # Auto incremented/assigned id
            print(f'id of last row insert = {rowid}')
            conn.commit()
        else:
            print("Senosor reading failed")
    except sqlite3.Error as e:
        conn.rollback()
        print(f'Could not insert ! {e}')
    finally:
        conn.close()

while True: 
    insertDHTDATA()
    sleep(10)
