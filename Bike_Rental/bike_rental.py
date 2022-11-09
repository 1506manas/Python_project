import pymysql
import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database = 'bike_rental')
cur = connection.cursor()

class BikeRental:
    
    def __init__(self):
        
        self.__menu()

    def __menu(self):
        User_Input = input("""Select:
        1: Available Bikes
        2: Select a Bike for Rent
        3: Time Used
        4: Request for Bill
        5: Add a Bike
        Press any Button to Exit.
        Enter your Choice here:""")

        if User_Input == '1':
            self.available_bike()
        elif User_Input == '2':
            self.select_bike()
        elif User_Input == '3':
            self.time_used()
        elif User_Input == '4':
            self.bill()
        elif User_Input == '5':
            self.add_bike()
        else:
            print("Thank You Visiting")
        
    def available_bike(self):
        
        sql = "select * from Bikes where Availability = 'YES'"
        cur.execute(sql)
        records = cur.fetchall()
        print("Total number of Bikes available: ", cur.rowcount, "\n")

        for row in records:
            print("Name = ", row[0], )
            print("Bike Number = ", row[1])
            print("Rent_Per_Hour  = ", row[2])
            print("Rent_Per_Day  = ", row[3])
            print("Rent_Per_Month  = ", row[4], "\n")

        print("\n")
        self.__menu()
        
    def select_bike(self):
        sql = "select * from Bikes where Availability = 'YES'"
        cur.execute(sql)
        records = cur.fetchall()
        print("Total number of Bikes available: ", cur.rowcount, "\n")
        
        if cur.rowcount >= 1:
            select = input("Enter The Bike Number You Want:")

            start = datetime.datetime.now()
        
            sql = "UPDATE Bikes set Availability = 'NO', Timing = '{}' where Bike_Number = '{}'".format(start.strftime('%Y-%m-%d %H:%M:%S'), select)
            cur.execute(sql)
        
            connection.commit()

        else:
            print("No Bike is available at this time")

        print("\n")
        self.__menu()

    def time_used(self):
        
        select = input("Enter The Bike number: ")

        sql = "select Timing from Bikes where Bike_Number = '{}'".format(select)
        cur.execute(sql)

        record = cur.fetchone()
        
        if record[0] == None:
            print("This bike is not in use")

        else:
            start = datetime.datetime.now()
            #print(start)

        
            #print(start -record[0])
        
            current_time = start - record[0]
            print(current_time)

        print("\n")
        self.__menu()

    def bill(self):

        select = input("Enter The Bike number: ")
        
        start = datetime.datetime.now()

        sql = "select Timing from Bikes where Bike_Number = '{}'".format(select)
        cur.execute(sql)

        record = cur.fetchone()

        current_time = start - record[0]
        #print(current_time)

        days = current_time.days

        hours = current_time.seconds/(60*60)
        #print(hours)
        
        sql1 = "select * from Bikes where Bike_Number = '{}'".format(select)
        cur.execute(sql1)
        records = cur.fetchall()

        for row in records:
            Rent_Per_Hour  = row[2]
            Rent_Per_Day  = row[3]
            Rent_Per_Month  = row[4]

        if days < 1:
            minute = round((hours - int(hours))*60)
            total_rent = round(hours) * Rent_Per_Hour
            print("\nThe Total rent you have to pay is: Rs.", total_rent)
            print("\nThe total time you used this Bike is: ", int(hours), "Hours and", minute, "Minutes." )

        elif days > 1 and days < 30:
            hour = int((hours/24 - int(hours/24))*24)
            total_rent =(days * Rent_Per_Day) + (round(hour)*Rent_Per_Hour)
            
            print("\nThe Total rent you have to pay is: Rs.", total_rent)
            print("\nThe total time you used this Bike is: ", days, "Days and", hour, "Hours")

        elif days > 30:
            month = int(days/30)
            day = days - (month*30)

            total_rent = (month*Rent_Per_Month) + (day*Rent_Per_Day) + (hours*Rent_Per_Hour)
            print("\nThe Total rent you have to pay is: Rs.", total_rent)
            print("\nThe total time you used this Bike is: ", month, "months, ",day, "Days and ", round(hours), "Hours")

        sql = "UPDATE Bikes set Availability = 'YES', Timing = NULL where Bike_Number = '{}'".format(select)
        cur.execute(sql)
        
        connection.commit()

        print("\n")
        self.__menu()
        
        
    def add_bike(self):
        
        value = input("Enter the bike you want to add:")
        number = input("Enter the bike number")
        rent_per_hour = int(input("Enter the rent for an hour:"))
        rent_per_day = int(input("Enter the rent for a day:"))
        rent_per_month = int(input("Enter the rent for a Month:"))
                
        
        
        sql = "INSERT INTO Bikes(Name, Bike_Number, Rent_Per_Hour, Rent_Per_Day, Rent_Per_Month) VALUES ('{}','{}',{},{},{})".format(value.title(),number.title(),rent_per_hour,rent_per_day,rent_per_month)
        cur.execute(sql)

        connection.commit()

        print("\n")
        self.__menu()
                             

cust1 = BikeRental()
        
