import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal

config = {
  'host':'db-owc-01.mysql.database.azure.com',
  'user':'OWC_Agent',
  'password':'^U?D#atNbmK6)k2',
  'database':'test_mysql',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': '<path-to-SSL-cert>/DigiCertGlobalRootG2.crt.pem'
}

# Construct connection string
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

  # Read data
  cursor.execute("SELECT * FROM inventory;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
    print("Data row = (%s, %s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")