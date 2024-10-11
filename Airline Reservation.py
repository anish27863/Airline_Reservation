import random
import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='127.0.0.1',user='Anish',passwd='12345',database='airline')
cursor=con.cursor()
c=0
urnme=""

def display_menu():
  """Prints the menu options for the airline reservation system."""
  print("1. Search available planes")
  print("2. Book ticket")
  print("3. Cancel ticket")
  print("4. View tickets")
  print("5. Exit")
  print("\nPlease enter your choice (1-5): ")
  print("-"*120,"\n")

def initial_display_menu():
  print("\nAirline Reservation System")
  print("-" * 30)
  print("1.Sign in ")
  print("2.Sign up ")
  print("3.Search planes ")
  print("\nPlease enter your choice (1-3): ")
  print("-"*120,"\n")

def exitf():
  print("Exiting the system...")
  exit()

def spacer():
  print("-"*120)
  print("\n\n\n")  

def planes_available():
  cursor2=con.cursor()
  '''prints available planes'''
  strt=input("Enter source ")
  end=input("Enter destination ")
  val=(strt,end)
  SQL="SELECT * FROM planes WHERE departure_place= %s and reaching_place= %s"
  cursor2.execute(SQL,val)
  dt=cursor2.fetchall()

  if len(dt)!=0:
    print("Found the following flights ")
    print(pd.DataFrame.from_records(dt,columns=["Plane number","Destination","Source","Departure Time","Arrival Time","Airline Company","Economy Class Fare", "Business Class Fare"]).reset_index(drop=True))
  else:
    print("NO planes found")    
  cursor2.close()
  spacer()

def ticketbooking():
  '''books the ticket'''
  cursor3=con.cursor()
  planes_available()
  pno=input("Enter plane number of your desired plane from the list: ")
  pn=list(pno)
  f1,f2='',''
  cl=input("Enter class:\n Economy \n Business \n ")
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
      print(f"please note the booking number {bknum} for future refference")
    except:
      print("Error")

  spacer()      

def display_booked_tickets():
  '''displays booksed tickets'''
  cursor4=con.cursor()
  bno=input("Enter booking number: ")
  cursor4.execute("SELECT * FROM tickets WHERE booking_no= %s and username= %s",(bno,urnme))
  tickets=cursor4.fetchall()
  if(len(tickets)!=0):
    print(pd.DataFrame.from_records(tickets, columns=["Username","Plane Number","Booking Number","Passenger Name", "Class", "Fare"]).reset_index(drop=True))
    cursor4.close()
    return bno    
  else:
    print("Ticket not found ")
  spacer()  
  
def cancel_ticket():
  '''cancels the ticket'''
  bno=display_booked_tickets()
  cursor5=con.cursor()
  if(bno!=None):
    confirmation=int(input("Are you sure you want to delete the above ticket ??\n 1. yes\n 2. No\n"))
    if(confirmation==1):
      print(urnme)
      cursor5.execute("DELETE FROM tickets WHERE booking_no=%s and username=%s ",(bno,urnme))
      con.commit()
      print("data deleted")
  cursor5.close()
  spacer()  

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
  spacer()

  print("Now login using your details: ")
  sign_in()

def sign_in():
  global urnme
  cursor1=con.cursor()
  flag=True
  global c
  c=0
  while flag:
    uid=input("Enter username: ")
    urnme=uid
    passw=input("Enter password: ")
    data=(uid,passw)
    cursor1.execute("select username,passw from users where username=%s and passw=%s",data)
    database_data=cursor1.fetchall()
     
    if(data in database_data):
      flag=False
      print('Welcome: ')
      spacer()
      c=1
    else:
      print("Wrong details ")
      ret=input("Do you want to retry, enter yes or no: \n\t")
      if ret.lower()=='no' :
        cursor1.close()
        exitf()
       
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
        planes_available() # Implement Plane search functionality
        pass
      elif choice == 2:
          ticketbooking() # Implement ticket booking functionality
          pass
      elif choice == 3:
        cancel_ticket()# Implement ticket cancellation functionality
        pass
      elif choice == 4:
        display_booked_tickets()# Implement view Fare= tickets functionality
        pass
      elif choice == 5:
        exitf()
        break
      else:
        print("Invalid choice. Please try again.")
  else:
    print("please sign_in ")
    sign_in()  

main()        