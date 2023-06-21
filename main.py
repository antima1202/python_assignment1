import csv
from datetime import datetime
import re

#all users data read from orders.csv
class AcmeWines:

        def __init__(self):
            print("init")
        
        def read_orders(self):
                orders=[]
                with open("orders.csv","r") as file:
                        data = csv.DictReader(file)
                        orders.extend(iter(data))
                return orders

class Users:
      def __init__(self,data):
            self.id=data["ID"]
            self.name=data["Name"]
            self.email_address=data["Email"]
            self.zipcode=data["ZipCode"]
            self.state=data["State"]
            self.birth_date=datetime.strptime(data["Birthday"],"%m/%d/%Y")

      #check for prohibited states
      def check_state(self): 
             prohibited_states=  ["NJ", "CT", "PA", "MA", "IL", "ID" , "OR"]
             return self.state not in prohibited_states
             
      #check zipcode for consicutive numbers
      def check_zipcode(self): 
          n=len(self.zipcode)-1                       #zipcode length
          while n:
            if self.is_consecutive(self.zipcode[n],self.zipcode[n-1]):
                 return False
            n -=1
          return True
                    
      def is_consecutive(self, a, b):
             self.a= int(a)
             self.b= int(b)
             return self.a-1 == self.b or self.a == self.b-1

      #check for a valid email address
      def check_email(self): 
             return bool(re.match (r"[^@]+@[^@]+\.[^@]+",self.email_address))          
          
     
      #check if date is first monday of month
      def check_weekday(self): 
             return self.birth_date.weekday() if self.birth_date.day <= 7 else True
     
      #check age>= 21
      def check_age(self): 
              today=datetime.now()
              age=today.year-self.birth_date.year
              if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1
              return age >= 21
     
class Orders:
        
     def valid_orders(self,id):
          with open("valid.csv",'a',newline='') as file:
                writer=csv.writer(file)
                writer.writerow([id])
     
     def invalid_orders(self,id):
           with open("invalid.csv",'a',newline='') as file:
                writer=csv.writer(file)
                writer.writerow([id])

#------
customers =AcmeWines()
orderlist= customers.read_orders()
deliver= Orders()
for row in orderlist:
        user=Users(row)
        if user.check_email() and user.check_zipcode() and user.check_state() and user.check_weekday() and user.check_age():
              deliver.valid_orders(row["ID"])
        else:
              deliver.invalid_orders(row["ID"])
# ------




