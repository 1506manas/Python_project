import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             )
if connection== False:
    print("failed connecting")
else:
    print("success")



try:
    cur = connection.cursor()
    sql = "CREATE DATABASE Bike_Rental"
    cur.execute(sql)
    #sql = "CREATE TABLE Bikes(Name varchar(20), Rent_For_Hour int(10), Rent_For_Day int(10), Rent_For_Month int(10))"
    #cursorInsatnce.execute(sql)

except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    connection.close()
