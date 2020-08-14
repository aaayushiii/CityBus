import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="new",
    passwd="newuser@123"
)
c=mydb.cursor()
c.execute("create database City_Bus_Management2")
c.execute("use City_Bus_Management2")
c.execute("create table `bus3`(""`busid` int," "`busno` int," "`busname` varchar(30)," "`busroute` varchar(50)," "`bustiming` float," "`fare` int"")")
c.execute("create table `passenger4`(""`passengername` varchar(40)," "`pid` int," "`startingpoint` varchar(50)," "`destination` varchar(30)," "`journeydate` DATE," "`fare` int"")")
print("Bus table is created......")
print("table is created")
mydb.commit()



class Bus:
    def admin(self):
        print("\n -- Welcome ADMIN -- \n")

        while True:

            v=int(input("1.View Passenger-table\n2.Fill Details\n3.Bus update\n4.busdelete\n5.viewbusdetails\n6.Delete Passenger-details\n7.exit\n enter your choice:"))

            if(v==1):
                print("\n -- Passenger Details : -- \n")
                c.execute("select * from passenger4")
                res=c.fetchall()
                print(res)
                #for i in res:
                    #print(i)

            elif(v==2):
                print("\n -- Bus : -- \n")
                busid=int(input("enter bus id"))
                busno=int(input("Enter Busno :"))
                busname=input("Enter BusName :")
                busroute=input("Enter  Busroute")
                bustiming=float(input("enter bustiming"))
                fare=int(input("enter the fare"))
                c.execute("insert into bus3 values (%d,%d,'%s','%s',%f,%d)"%(busid,busno,busname,busroute,bustiming,fare))
                c.execute("update passenger4 set fare=%s"%(fare,))
                mydb.commit()

            elif(v==3):
                print("\n -- Bus update : -- \n")
                busid=int(input("enter bus id"))
                bustiming=float(input("Enter Bustiming :"))
                busroute=input("Enter  Busroute")
                c.execute("update bus3 set `busroute`='%s',`bustiming`=%f where busid=%s"%(busroute,bustiming,busid))
                mydb.commit()
            elif(v==4):
                busid=int(input("enter bus id"))
                print("\n --Details Deletion : -- \n")
                c.execute("delete from bus3 where busid=%s"%(busid,))
                mydb.commit()
            elif(v==5):
                print("\n -- Bus details:-- \n")
                c.execute("select * from bus3")
                res=c.fetchall()
                print(res)
                #for i in res:
                    #print(i)
            elif(v==6):
                print("\n--Passenger Deletion--\n")
                pid=int(input("Enter pid :"))
                c.execute("delete from passenger4 where pid=%s"%(pid,))
                mydb.commit()
            elif(v==7):
                break
    def passenger(self):
        print("\n-- Welcome Passenger--")

        while True:

            n=int(input("1.View Bus Availability\n2.Fill Details\n3.View Details\n4.Update Details\n5.Exit\nenter your choice:"))
            if(n==1):
                print("-- View Bus Details :--")
                c.execute("select * from bus3")
                res=c.fetchall()
                print(res)
                #for i in res:
                    #print(i)
                mydb.commit()
            elif(n==2):
                print("--Fill Details :--")
                passengername=input("enter your name :")
                pid=int(input("Enter pid :"))
                startingpoint=input("Enter starting point :")
                destination=input("Enter  your destination :")
                journeydate=input("enter journey date:")
                fare=int(input("enter default value for fare:"))
                c.execute("insert into passenger4 values('%s',%d,'%s','%s','%s',%d)"%(passengername,pid,startingpoint,destination,journeydate,fare))
                mydb.commit()

            elif(n==3):
                print("--View Details :--")
                pid=(input("Enter pid :"))
                c.execute("select * from passenger4 where pid=%s"%(pid,))
                res=c.fetchall()
                print(res)
                mydb.commit()
            elif(n==4):
                print("--Details updation")
                pid=int(input("Enter Pid :"))
                passengername=input("enter name:")
                startingpoint=input("Enter starting point :")
                destination=input("Enter  your destination :")
                c.execute("update passenger4 set `passengername`='%s',`startingpoint`='%s',`destination`='%s' where pid=%d"%(passengername,startingpoint,destination,pid,))
                mydb.commit()

            elif(n==5):
                break




print("----- CITY BUS MANAGEMENT SYSTEM -----")
obj=Bus()
while True:
    ch=int(input("1.Admin\n2.Passenger\n3.exit\nEnter your Choice :"))
    if(ch==1):
        obj.admin()
    elif(ch==2):
        obj.passenger()
    elif(ch==3):
        break
