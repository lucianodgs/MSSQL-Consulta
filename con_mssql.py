import pymssql


con = pymssql.connect(host = 'xxx', user = 'xxx',  password = 'xxx', database = 'xxx')

cursor = con.cursor()

# print(query)
cursor.execute(query)
query = ("select  * from xxxxx" )
rows = cursor.fetchall()
count=1

for row in rows:
    print("COUNT:%s  HOST:%s" % (count,row[1]))
    count += 1