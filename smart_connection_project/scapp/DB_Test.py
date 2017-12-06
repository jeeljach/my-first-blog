import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='minepro02', db='smart_connection')

cur = conn.cursor()

cur.execute("SELECT * FROM sc_table")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()