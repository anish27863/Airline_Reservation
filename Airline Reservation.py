import random
import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='127.0.0.1',user='Anish',passwd='12345',database='airline')
cursor=con.cursor()
import payment as upi
tickets={}

def display_menu():
  """Prints the menu options for the airline reservation system."""
  print("\nAirline Reservation System")
  print("-" * 30)
  print("1. Search available planes")
  print("2. Check seat availability")
  print("3. Book ticket")
  print("4. Cancel ticket")
  print("5. Check PNR status")
  print("6. View tickets")
  print("7. Exit")
  print("\nPlease enter your choice (1-7): ")


def exitf():
  print("Exiting the system...")
  exit()


def planes_available():
  '''prints available planes'''
  global planes
  cursor.execute('SELECT * FROM planes')
  planes=cursor.fetchall()
  print(pd.DataFrame.from_records(planes).reset_index(drop=True))


def seat_availability():
  '''checks seat availablilty in the selected Plane'''
  tno=input("Enter Plane number")
  global boardingstaion,unboardingstation,date,ac1,ac2,ac3,sl,st,seats
  if(tno in planes):
    boardingstaion=input("Enter boarding station: ")
    unboardingstation=input("Enter unboarding station: ")
    date=input("Enter date of travel in the format dd.mm.yyyy: ")
    # Define a dictionary to represent the available seats in each class
    ac1=random.randint(0,20)
    ac2=random.randint(0,50)
    ac3=random.randint(0,80)
    sl=random.randint(0,150)
    st=random.randint(0,300)
    seats = {
    "First AC": {
        "Available": ac1
        
    },
    "Second AC": {
        "Available": ac2
        
    },
    "Third AC": {
        "Available": ac3
        
    },
    "Sleeper": {
        "Available": sl
        
    },
    "Sitting": {
        "Available": st
       
    }
  }

# Print the available seats for each class
  print("Available Seats:")
  for class_name, seat_info in seats.items():
    available_seats = seat_info["Available"]
    print(f"{class_name}: {available_seats}")


def ticketbooking():
  '''books the ticket'''
  fare=0
  berth=["upper",'middle',"lower","Side upper","side lower"]
  n=int(input("Enter number of tickets you wish to book: "))
  for i in range(1,n+1):
   pnr=random.randint(100,999)
   nm=input(f"Enter name of passenger {i} ")
   ag=int(input(f"Enter age of passenger {i} "))
   cl=int(input("choose preffered seating class:\n 1.First Ac \n 2.Second Ac \n 3.Third Ac \n 4.Sleeper \n 5.Seating \n "))
   if(cl==1):
    cla='First Ac'
    fare+=2000
    
   elif(cl==2):
    fare+=1500
    cla="Second Ac"
    
   elif(cl==3):
    fare+=1000
    cla="Third Ac"
     
   elif(cl==4):
    fare+=700
    cla="Sleeper"
    
   elif(cl==5):
    fare+=300
    cla="Sitting"
    
   else:
    print("Error, select a number between 1,5")      

   if(ag>55):
    berth=["Side lower","Lower"]

    

   tickets.update({pnr:{"          Name : ":nm,"         Age : ":ag," Class: ":cla," Berth : ":random.choice(berth),"PNR: ":pnr,"       Boarding Station: ":boardingstaion,"Unboarding Station: ":unboardingstation,"Date: ":date}})
  print(pd.DataFrame.from_dict(tickets, orient='index').reset_index(drop=True))
  print(f"Payment Due= {fare}")
  num=int(input("Enter UPI id: "))
  upi_ps=int(input("Enter UPI password: "))
  if(num==upi.upi_id and upi_ps==upi.upi_pin):
    print("Ticket Booked succesfully")
  else:
    print("Wrong id or password, ticket not booked")
    tickets.clear()   
  

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


def main():
  while True:
    display_menu()
    choice = int(input())
    if choice == 1:
      # Implement Plane search functionality
      planes_available()
      pass
    elif choice == 2:
      seat_availability()
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

if __name__ == "__main__":
  main()
