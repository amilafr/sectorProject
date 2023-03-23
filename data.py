# import mysql.connector
# from array import *

## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
# import numpy as np

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "sector_damage"
)

cursor = db.cursor()

## defining the Query
## getting records from the table
## fetching all records from the 'cursor' object

# ambil id case
query2 = "SELECT id_case FROM cases"
cursor.execute(query2)
records2 = cursor.fetchall()

indexes = []
i = 0
for r in records2:
    indexes.append(r[0])
# print(indexes)

# ambil data matrix
query = "SELECT * FROM matrix_keputusan"
cursor.execute(query)
records = cursor.fetchall()
# data = {}   #dictionary
data = []  #array

for index in indexes:
    arr = []
    for record in records:
        if record[1] == index:
            # arr.append(record[2])
            for x in range(1, 6):
                if record[2] == 1 and record[3] == x and record[4] > 1:
                    arr.append(record[2])
                elif record[2] == 2 and record[3] == x and record[4] > 1:
                    arr.append(record[2])
                elif record[2] == 3 and record[3] == x and record[4] > 1:
                    arr.append(record[2])
    data.insert(index, arr)

# ambil result
query3 = "SELECT result FROM v_result"
cursor.execute(query3)
records3 = cursor.fetchall()

results = []
for r in records3:
    results.append(r[0])
# print(results)

for i in range(0,len(records3)):
    data[i].append(results[i])

actual_data = data

# print(actual_data)