import random
import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='127.0.0.1',user='Anish',passwd='12345',database='airline')
cursor=con.cursor()
import payment as upi
c=0
urnme=""
#urnme=str(urnme)
tickets={}

def display_menu():
  """Prints the menu options for the airline reservation system."""
  print("1. Search available planes") #delete this later
  print("2. Check seat availability")
  print("3. Book ticket")
  print("4. Cancel ticket")
  print("5. Check PNR status")
  print("6. View tickets")
  print("7. Exit")
  print("\nPlease enter your choice (1-7): ")

def initial_display_menu():
  print("\nAirline Reservation System")
  print("-" * 30)
  print("1.Sign in ")
  print("2.Sign up ")
  print("3.Search planes ")
  print("\nPlease enter your choice (1-3): ")

def exitf():
  print("Exiting the system...")
  exit()

def planes_available():
  cursor2=con.cursor()
  '''prints available planes'''
  strt=input("Enter source ")
  end=input("Enter destination ")
  val=(strt,end)
  SQL="SELECT * FROM planes WHERE departure_place= %s and reaching_place= %s"
  cursor2.execute(SQL,val)
  dt=cursor2.fetchall()
  #cursor.close()
  if len(dt)!=0:
    print("Found the following flights ")
    print(pd.DataFrame.from_records(dt,columns=["Plane number","Destination","Source","Departure Time","Arrival Time","Airline Company","Economy Class Fare", "Business Class Fare"]).reset_index(drop=True))
  else:
    print("NO planes found")    
  cursor2.close()

def ticketbooking():
  '''books the ticket'''
  cursor3=con.cursor()
  planes_available()
  pno=input("Enter plane number of your desired plane from the list: ")
  pn=list(pno)
  f1,f2='',''
  #values=(fare,)
  cl=input("Enter class:\n Economy \n Business ")
  cursor.execute("SELECT plane_number,fare1,fare2 FROM planes")
  combfare=cursor.fetchall()
  flg=False
  for i in combfare:
    if(i[0])==pno.upper():
      f1=str(i[1])
      f2=str(i[2])
      flg=True
  if(flg==False):
    print("No planes found with the entered plane number")
   
  fare="0"
  if(cl.lower()=='economy'):
    fare=f1
  elif(cl.lower()=='business'):
    fare=f2
  else:
    print("error")    
     
  num_of_tic=int(input("Enter number of tickets to book: "))
  for i in range(0,num_of_tic):
    nameofpass=input("Enter name of passenger: ")
    bknum=random.randint(10000,99999)
    bknum=str(bknum)
    values=(urnme,pno,bknum,nameofpass,cl,fare)
    sql="INSERT INTO tickets(username,plane_number,booking_no,Passenger_Name,classs,fare) VALUES (%s,%s,%s,%s,%s,%s) "
    try:
      cursor3.execute(sql,values)
      con.commit()
      print("Ticket booked successfully")
    except:
      print("Error")  



def cancel_ticket():
    '''cancels the ticket'''
    a=int(input("Enter pnr number of the ticket to cancel"))
    if a in tickets:
        del tickets[a]
        print("Your ticket has been deleted")

    else:
        print("PNR not found")

def pnr_status():
    '''does the pnr status check'''
    a=int(input("Enter pnr number of the ticket "))
    if a in tickets:
        print("Booking is confirmed")
    else:
        print("PNR not found") 

def display_booked_tickets():
    '''displays booksed tickets'''
    print(print(pd.DataFrame.from_dict(tickets, orient='index').reset_index(drop=True)) )           

def sign_up():
  uid=input("Enter username ")
  name=input("Enter your name ")
  email=input("Enter email address ")
  ph=input("Enter phone number ")
  passw=input("Create password")
  values=(uid,name,email,ph,passw)
  sql="INSERT INTO users(username,Full_Name,email,phone,passw) VALUES(%s,%s,%s,%s,%s)"
  cursor.execute(sql,values)
  con.commit()
  #cursor.close()

  print("Now login using your details: ")
  sign_in()

def sign_in():
  global urnme
  cursor=con.cursor()
  uid=input("Enter username: ")
  urnme=uid
  passw=input("Enter password: ")
  data=(uid,passw)
  flag=True
  global c
  c=0
  while flag:
    cursor.execute("SELECT username,passw from users")
    database_data=cursor.fetchone()
    print(database_data)
    if(database_data==data):
      flag=False
      print('Welcome: ')
      c=1
      display_menu()
    else:
      print("Wrong details ")
      print("Do you want to retry, enter yes or no")
      ret=input()
      if ret.lower=='no' :
        flag=False 
  cursor.close()      

def execution():
  initial_display_menu()
  choice=int(input())
  if(choice==1):
    sign_in()
  elif choice==2:
    sign_up()
  elif choice==3: 
    planes_available()         

def main():
  execution()
  if c==1:
    while True:
      display_menu()
      choice = int(input())
      if choice == 1:
        # Implement Plane search functionality
        planes_available()
        pass
      #elif choice == 2:
        #seat_availability()
        # Implement seat availability check functionality
        pass
      elif choice == 3:
          ticketbooking() # Implement ticket booking functionality
      elif choice == 4:
        cancel_ticket()# Implement ticket cancellation functionality
        pass
      elif choice == 5:
        pnr_status()# Implement PNR status check functionality
        pass
      elif choice == 6:
        display_booked_tickets()# Implement view Fare= tickets functionality
        pass
      elif choice == 7:
        exitf()
        break
      else:
        print("Invalid choice. Please try again.")
  else:
    print("please sign_in ")
    sign_in()  

#main()        
#planes_available()
ticketbooking()