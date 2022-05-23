import mysql.connector
from mysql.connector import errorcode
import time
from datetime import datetime
from collections import deque
from py4j.java_gateway import JavaGateway
import get_Analog_value_java as getAvalue
import random

gateway = JavaGateway()
gateway.connectModbus()

config = {
  'host':'db-owc-01.mysql.database.azure.com',
  'user':'OWC_Agent',
  'password':'^U?D#atNbmK6)k2',
  'database':'test_mysql',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': '<path-to-SSL-cert>/DigiCertGlobalRootG2.crt.pem'
}

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Drop previous table of same name if one exists
  #cursor.execute("DROP TABLE IF EXISTS inventory;")
  #print("Finished dropping table (if existed).")

  # Create table
  #cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, KST VARCHAR(50), name VARCHAR(50), value FLOAT(5, 2), avg FLOAT(5, 2));")
  #print("Finished creating table.")

  temp_queue = deque()
  humid_queue = deque()
  CO2_queue = deque()
  query = getAvalue.query
  # Insert some data into table
  i = 0
  while(1):
    if i == 57 and random.randint(1, 100) == 57:
      temp = random.randint(-30, 9)
      humid = random.randint(0,  29)
      CO2 = random.randint(650, 1000)

      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Temp", temp, temp_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Humid", humid, humid_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "CO2", CO2, CO2_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      conn.commit()

      temp = query.gettemp(gateway)
      humid = query.gethumid(gateway)
      CO2 = query.getco2(gateway)
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Temp", temp, temp_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Humid", humid, humid_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "CO2", CO2, CO2_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      conn.commit()
    elif i == 119 and random.randint(1, 100) == 11:
      temp = random.randint(33, 100)
      humid = random.randint(50,  100)
      CO2 = random.randint(650, 1000)

      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Temp", temp, temp_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Humid", humid, humid_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "CO2", CO2, CO2_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      conn.commit()

      temp = query.gettemp(gateway)
      humid = query.gethumid(gateway)
      CO2 = query.getco2(gateway)
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Temp", temp, temp_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Humid", humid, humid_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "CO2", CO2, CO2_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      conn.commit()
    else:
      temp = query.gettemp(gateway)
      humid = query.gethumid(gateway)
      CO2 = query.getco2(gateway)
    
    while temp == -1000000 or humid == -1000000 or CO2 == -1000000:
      gateway.closeModbus()
      gateway.connectModbus()
      temp = query.gettemp(gateway)
      humid = query.gethumid(gateway)
      CO2 = query.getco2(gateway)
    
    temp_queue.append(temp)
    humid_queue.append(humid)
    CO2_queue.append(CO2)
    if len(temp_queue) > 150:
      temp_queue.popleft()
    if len(humid_queue) > 150:
      humid_queue.popleft()
    if len(CO2_queue) > 150:
      CO2_queue.popleft()

    print(temp_queue)
    print(humid_queue)
    print(CO2_queue)

    temp_avg = round(sum(temp_queue) / 150, 2)
    humid_avg = round(sum(humid_queue) / 150, 2)
    CO2_avg = round(sum(CO2_queue) / 150, 2)

    KST = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    i += 1

    print(i)
    if i == 150:
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Temp", temp, temp_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "Humid", humid, humid_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      cursor.execute("INSERT INTO inventory (KST, name, value, avg) VALUES (%s, %s, %s, %s);", (KST, "CO2", CO2, CO2_avg))
      print("Inserted",cursor.rowcount,"row(s) of data.")
      conn.commit()
      i = 0
    time.sleep(2)

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")