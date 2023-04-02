from myprint import print_center,input_center
#import os
import datetime
#import string
#from datetime import date
#import platform
import pandas as pd
import mysql.connector

#stablishing connection with mysql
conn=mysql.connector.connect(host="localhost",
                             user="prince",
                             password="password@2!1",
                             database="hotel")

cursor=conn.cursor()  #It allow Python code to execute

Cdate=datetime.datetime.now()  

def Set_date_format(d1,m1,y1):
    fdt=""
    d11=str(d1)
    m11=str(m1)
    y11=str(y1)
    if (len(d11)==1):
        d11='0'+d11
    if (len(m11)==1):
        m11='0'+m11
    fdt=d11+'-'+m11+'-'+y11
    return fdt





#This function is made to add a new record in room table
def new_room():
    rid=int(input("Enter Room id:"))                
    room_no=int(input("Enter Room number:"))
    floor=int(input("Enter Floor number:"))
    beds=int(input("Enter beds required:"))
    availabale=input("Available(Y/N):")

    try:
            sql="insert into rooms values(%i,%i,%i,%i,'%s')"  #  this is a syntax of mysql used to insert values into table
            cursor.execute(sql %(rid,room_no,floor,beds,availabale))
            print("record inserted successfully")
            conn.commit() #It will make the change permanante
    except:
        print("EXCEPTION RAISED")


#This function  retrive data from room table as per choice
def view_rooms():
    print("☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺")
    print("===SEARCH  CRITERIA===")
    print("1.Room id:")
    print("2.Room No:")
    print("3.Floor:")
    print("4.Available:")
    print("5.Beds")
    print("6.View all")
    print("0.Go Back")
    print("☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺")
    print()
    ch=int(input("Enter Your Choice:"))  # It will ask for the choices
    if ch==1:
        i=int(input("Enter Room id:"))
        rl=(i,)
        sql="select*from rooms where id='%s'"
        cursor.execute(sql %(rl))
    elif ch==2:
        i=int(input("Enter Room no:"))
        rl=(i,)
        sql="select*from rooms where room_no='%s'"
        cursor.execute(sql %(rl))
    elif ch==3:
        i=int(input("Enter Floor:"))
        rl=(i,)
        sql="select*from rooms where floor=%d"
        cursor.execute(sql %(rl))
    elif ch==4:
        i=input("Enter Availabale:")
        rl=(i,)
        sql="select*from rooms where availabale='%s'"
        cursor.execute(sql %(rl))
    elif ch==5:
        i=int(input("Enter Number Of Beds:"))
        rl=(i,)
        sql="select*from rooms where beds=%d"
        cursor.execute(sql %(rl))
    elif ch==6:
        sql="select*from rooms"
        cursor.execute(sql)
    elif ch==0:
        room_menu()
    else:
        print("WORNG OPERATION")
        view_rooms()
    res=cursor.fetchall()
    print()
    print("♦♦♦♦THE ROOM DETAILS ARE AS FOLLOWS♦♦♦♦")
    df=pd.DataFrame(res,columns=['id', 'room_no','floor','beds','available'])
    print(df)
    
    
# This function perform the function of modifying the record as per choices
def modify_room_by_id():
    rid= int(input("Enter Room id-->"))
    print("♦♦SELECT OPTION TO UPDATE♦♦")
    print("1.Room No.")
    print("2.Floor")
    print("3.Beds")
    print("4.Available")
    print("0.Go Back")
    ch=int(input("Enter your choice-->"))
    if ch==1:
        N_room_no=int(input("Enter New Room No:"))
        sql="update rooms set room_no= %d where id =%d" 
        print("Updated successfully")
        cursor=conn.cursor()
        cursor.execute(sql %(N_room_no,rid))
        conn.commit()
    elif ch==2:
        N_floor=int(input("Enter new floor:"))
        sql="update rooms set floor= %d where id =%d"
        print("Update successfully")
        cursor=conn.cursor()
        cursor.execute(sql %(N_floor,rid))
        conn.commit()
    elif ch==3:
        N_beds=int(input("Enter number of beds:"))
        sql="update rooms set beds= %d where id =%d"
        print("Update successfully")
        cursor=conn.cursor()
        cursor.execute(sql %(N_beds,rid))
        conn.commit()
    elif ch==4:
        N_available=input("Enter Availability(Y/N):")
        sql="update rooms set availabale= %d where id =%d"
        print("Updated successfully")
        cursor=conn.cursor()
        cursor.execute(sql %(N_availabale,rid))
    elif ch==0:
        room_menu()
    else:
        print("☺☺☺ WRONG OPERATION ☺☺☺")
        modify_room_by_id()

#This function perform the removal or data from table as per choices
def delete_room():
    print("♥♥♥SELECT OPTION BY WHICH YOU WANT TO DELETE♥♥♥")
    print("1.Id:")
    print("2.Room no:")
    print("3.Floor:")
    print("0.Go Back")
    print()
    ch=int(input("Enter Your Choices:"))
    if ch==1:
         id=int(input("Enter Room Id:"))
         sql="delete from rooms where id=id"
         cursor=conn.cursor()
         cursor.execute(sql)
         conn.commit()
    elif ch==2:
        Room_No=int(input("Enter Room Number:"))
        sql="delete from rooms where room_no=Room_No"
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
    elif ch==3:
        floor=int(input("Enter floor:"))
        sql="delete from rooms where floor=floor"
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
    elif ch==0:
        room_menu()
    else:
        print("↓↓↓WRONG OPERATION↓↓↓")
        delete_room()
        


#This is the main function.It provides option for performing various operation table Room.
def room_menu():
    while True:
        print()
        print("============================")
        print("==========Room Menu=========")
        print("============================")
        print()

        print("1. Add new room")
        print("2. Get room details")
        print("3. Edit Room details")
        print("4. Delete room")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_room()
        elif choice==2:
            view_rooms()
        elif choice==3:
            modify_room_by_id()
        elif choice==4:
            delete_room()
        else :
            print("☺☺☺ THANK YOU ☺☺☺")
            MenuSet()


#This function perform the task of adding new record in customer table
def add_customer():
    l=[]
    rid=int(input("Enter Customer Id:"))
    l.append(id)                
    name=input("Enter Customer Name:")
    l.append(name)
    address=input("Enter Customer Address:")
    l.append(address)
    phone_number=int(input("Enter Customer Phone Number:"))
    l.append(phone_number)
    room_no=int(input("Enter Room Number:"))
    l.append(room_no)
    curDt=str(Cdate)
    l.append(curDt)
    checkout=input("Enter Date:")
    l.append(checkout)
        
    try:
            sql="insert into customer values(%d,'%s','%s',%d,%d,'%s','%s')"
            cursor.execute(sql %(rid,name,address,phone_number,room_no,curDt,checkout))
            print("Added successfully")
            conn.commit()
    except:
            print("EXECPTION RAISED")


#This function perform the task of retrival or data from customer table
def view_customer():
    print("☺☺☺☺ SEARCH CRITERIA ☺☺☺☺")
    print("1.Id:")
    print("2.Room No:")
    print("3.Name:")
    print("4.Address:")
    print("5.Phone number")
    print("6.Entry_date")
    print("7.Check_out")
    print("8.view all")
    print("0.Go Back")
    ch=int(input("Enetr your choice-->"))
    if ch==1:
        i=int(input("Enter Customer Id:"))
        rl=(i,)
        sql="select*from customer where id=%s"
        cursor.execute(sql,rl)
    elif ch==2:
        i=int(input("Enter Room No:"))
        rl=(i,)
        sql="select*from customer where room_no=%s"
        cursor.execute(sql,rl)
    elif ch==3:
        i=input("Enter Customer Name:")
        rl=(i,)
        sql="select*from customer where Name=%s"
        cursor.execute(sql,rl)
    elif ch==4:
        i=input("Enter Address of the Customer:")
        rl=(i,)
        sql="select*from customer where Address=%s"
        cursor.execute(sql,rl)
    elif ch==5:
        i=int(input("Enter Customer Phone Number:"))
        rl=(i,)
        sql="select*from customer where phone=%s"
        cursor.execute(sql,rl)
    elif ch==6:
        i=input("Enter Entry date:")
        rl=(i,)
        sql="select*from customer where entry_date=%s"
        cursor.execute(sql,rl)
    elif ch==7:
        i=input("Enter Check out date:")
        rl=(i,)
        sql="select*from customer where check_out=%s"
        cursor.execute(sql,rl)
    elif ch==8:
        sql="select*from customer"
        cursor.execute(sql)
    elif ch==0:
        customer_menu()
    else:
        print("↓↓↓WRONG OPERATION↓↓↓")
        view_customer()
    res=cursor.fetchall()
    print()
    print("♦♦♦♦THE CUSTOMERS DETAILS ARE AS FOLLOWS♦♦♦♦")
    df=pd.DataFrame(res,columns=['id','Name','Address','phone','room_no','entry_date','check_out' ])
    print(df)

#This function perform the task of modification to be done in customer table
def modify_customer_by_id():
    rid= int(input("Enter Customer Id-->"))
    print("==SELECT OPTION TO UPDATE===")
    print("1.Room No.")
    print("2.Name")
    print("3.Address")
    print("4.Phone number")
    print("5.Entry date")
    print("6.Check out")
    print("0.Go Back")
    
    ch=int(input("Enter Your Choice-->"))
    if ch==1:
        N_room_no=int(input("Enter new Room No:"))
        sql="update customer set room_no=%d where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_room_no,rid))
        print("♥♥♥SUCCESSFULLY MODIFID♥♥♥")
        conn.commit()
        
    elif ch==2:
        N_customer=input("Enter New Customer Name:")
        sql="update customer set Name='%s' where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_customer,rid))
        conn.commit()
    elif ch==3:
        N_Address=input("Enter New Address:")
        sql="update customer set Address='%s' where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_Address,rid))
        print("♥♥♥SUCCESSFULLY MODIFID♥♥♥")               
        conn.commit()
    elif ch==4:
        N_phone_number=int(input("Enter New Phone Number:"))
        sql="update customer set phone=%d where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_phone_number,rid))
        print("♥♥♥SUCCESSFULLY MODIFID♥♥♥")
        conn.commit()
    elif ch==5:
        N_entry=input("Enter New Entry Date:")
        sql="update customer set entry_date='%s' where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_entry,rid))
        print("♥♥♥SUCCESSFULLY MODIFID♥♥♥")
        conn.commit()
    elif ch==6:
        N_entry=input("Enter Check Out Date:")
        sql="update customer set check_out='%s' where id=%d"
        cursor=conn.cursor()
        cursor.execute(sql %(N_entry,rid))
        print("♥♥♥SUCCESSFULLY MODIFID♥♥♥")
        conn.commit()
    elif ch==0:
        customer_menu()
    
    else:
        print("↓↓↓WRONG OPERATION↓↓↓")
        modify_customer_by_id()
        


#This function perform the task of removal of data from customer table
def delete_customer():
    print("☺☺☺SELECT OPTION BY WHICH YOU WANT TO DELETE☺☺☺")
    print("1.Id")
    print("2.Room No.")
    print("3.Name")
    print("4.Address")
    print("5.Phone number")
    print("6.Entry date")
    print("7.Check out")
    print("0.Go Back")
    
    ch=int(input("Enter Your Choice-->"))
    if ch==1:
         i=int(input("Enter Customer Id:"))
         sql="delete from customer where id=%d"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    if ch==2:
         i=int(input("Enter Room No:"))
         sql="delete from customer where room_no=%d"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==3:
         i=input("Enter Customer Name:")
         sql="delete from customer where Name='%s'"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==4:
         i=input("Enter Address:")
         sql="delete from customer where Address='%s'"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==5:
         i=int(input("Enter Phone Number:"))
         sql="delete from customer where phone=%d"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==6:
         i=input("Enter Entry Date:")
         sql="delete from customer where entry_date='%s'"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==7:
         i=input("Enter Check Out Date:")
         sql="delete from customer where check_out='%s'"
         cursor=conn.cursor()
         cursor.execute(sql %(i))
         print('♥♥♥SUCCESSFULLY REMOVED♥♥♥')
         conn.commit()
    elif ch==0:
        customer_menu()
    else:
        print("↓↓↓WRONG OPERATION↓↓↓")
        delete_customer()



#This is the main function which will provide the option to perform various task on customer table
def customer_menu():
    while True:
        print()
        print("================================")
        print("=========Customer Menu==========")
        print("================================")
        print()
        print("1. Add new customer")
        print("2. Get customer details")
        print("3. Edit customer details")
        print("4. Delete customer")
        print("0. Go Back")
        print()
        ch=int(input("Enter Your Option:"))
        if ch==1:
            add_customer()
        elif ch==2:
            view_customer()
        elif ch==3:
            modify_customer_by_id()
        elif ch==4:
            delete_customer()
        elif ch==0:
            MenuSet()
        else:
            print("↓↓↓WRONG OPERATION↓↓↓")
            customer_menu()




# This is the main set of whole programme
#It provides the option to choose the table on which you want to go through
def MenuSet():
 while True:
        opt=""
        print()
        print_center("==============================")
        print_center("=====REGAL HOTEL=====")
        print_center("==============================")
        print_center("1. Manage Rooms")
        print_center("2. Manage Customers")
        print_center("0. Exit")
        print()
        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            room_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 0:
            break
        else:
            print()
            print_center("Invalid choice (Press 0 to exit)")
            print()
            print_center("♥♥♥GoodBye♥♥♥")
            break
MenuSet()

