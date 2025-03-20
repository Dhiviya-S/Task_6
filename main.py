##BANK ACCOUNT USING INHERITANCE ###
class BankAccount: #class creation [class ClassName:]
    def __init__(self): #init method is called when object is created
        self.account_number = "0112345678"
        self._balance = 5000 #Balance attribute is protected self._(Accessible within subclasses)
    def deposit(self):#Instance method to deposit
        amount = float(input("Enter the amount to deposit: "))
        self._balance += amount #Adds deposited amount to balance
        print(f"Deposited amount:{amount}.New balance:{self._balance}")
    def withdraw(self): #Instance method to withdraw
        amount = float(input("Enter withdrawal amount: "))
        if amount>=self._balance: #Checks if withdrawal exceeds available balance
            print("\n Withdrawal exceeds your balance ")
        elif self._balance - amount < 1500: #Checks if withdrawal violates minimum balance requirement of "Rs.1500"
           print ("Withdrawal would violate minimum balance requirement.")
        elif self._balance >= amount and self._balance>1500 : #Withdraws only if "amount" is less than available balance
            self._balance -= amount #Subtracts from available balance
            print(f"Withdrawal amount:{amount}.New balance:{self._balance}")

class SavingsAccount(BankAccount): #Inherited BankAccount class(SavingsAccount is a Subclass)
    def __init__(self):
        super().__init__() #super() is used to access the base class attributes account number and balance
        self.interest_rate = 0.05 #New attribute
        print(f"Your Account number:{self.account_number}, Available Balance:{self._balance}, Interest rate:{self.interest_rate * 100}%")
    def set_interest(self, new_rate): #this method prints the updated interest rate
        self.interest_rate = new_rate
        return f"Updated interest rate is {self.interest_rate * 100}%"

class CurrentAccount(BankAccount):#Inherited BankAccount class
    def __init__(self):
        super().__init__() #super() is used to access the BankAccount Attributes
    def min_balance(self): #Check if the balance meets the minimum balance requirement
        if self._balance < 1500:
            print(f"Your balance:{self._balance} is below the minimum balance")

s = SavingsAccount() #s is object created to access SavingsAccount() [objectname=method()]
print(s.set_interest(0.07)) #Passing new interest rate to set_interest() method
c = CurrentAccount() #c is an object to access CurrentAccount() class [objectname=method()]
c.deposit() # deposit and withdrawal methods are accessed either by object 'c' or 's'
c.withdraw()
c.min_balance() #calls min_balance method in CurrentAccount
print()

##EMPLOYEE MANAGEMENT USING INHERITANCE AND POLYMORPHISM##
class Employee: #Baseclass
    def __init__(self,name,salary): #name and salary attributes
        self.name=name
        self.salary=salary
    def calculate_salary(self): #instance method to calculate salary; Polymorphism is implemented in each subclass;only input varies
        print("Calculating wages")

class RegularEmployee(Employee):#Inherited Employee class
    def __init__(self,name,incentives,salary):
        super().__init__(name,salary) #Access base class attributes
        self.incentives=incentives #New attribute in RegularEmployee class which is not in base class
    def calculate_salary(self): #NetSalary includes sum of both Basic salary and incentives
        print(f"REGULAR EMPLOYEE: Name:{self.name}, Incentives:{self.incentives}, BasicSalary:{round(self.salary/12)}, NetSalary:{round(self.salary/12)+self.incentives}")

class ContractEmployee(Employee):#Inherited Employee class
    def __init__(self, name,hours_worked,hours_wage,salary):
        super().__init__(name,salary)
        self.hours_worked=hours_worked #New attributes other than base class
        self.hours_wage=hours_wage #New attributes
    def calculate_salary(self):
        self.salary=self.hours_worked*self.hours_wage #Multiplication of hours_worked and wages
        print(f"CONTRACT EMPLOYEE: Name:{self.name}, Worked_hours:{self.hours_worked}, WagesPerHour:{self.hours_wage}, NetSalary:{self.salary}")

class Manager(Employee):#Inherited Employee class
    def __init__(self, name,pf,salary):
        super().__init__(name,salary)
        self.pf=pf #New attribute in Manager class
    def calculate_salary(self): #PF is deducted from salary
        print(f"MANAGER: Name:{self.name}, PF_Deduction:{self.pf}, BasicSalary:{round(self.salary/12)}, NetSalary:{round(self.salary/12)-self.pf}")

print("Salary of Employees ")
r=RegularEmployee("Bob",1000,500000) #r is an object and here incentives and annual salary is passed
r.calculate_salary()
c=ContractEmployee("Alice",10,1500,200000) #Total hours worked and wages/hour is passed
c.calculate_salary()
m=Manager("John",2500,850000) #PF amount to be deducted and annual salary is passed
m.calculate_salary() #calls calculate_salary inside Manager class
print()

##VEHICLE RENTAL USING INHERITANCE AND POLYMORPHISM##
class Vehicle: #Baseclass
    def __init__(self,model,rental_rate): #Model and rental rate are attributes
        self.model=model
        self.rental_rate=rental_rate
    def calculate_rental(self): #Instance method to calculate rent.Polymorphism is implemented in Car,Bike,Truck to calculate cost
        print("Calculating rents")

class Car(Vehicle): #Subclass
    def __init__(self,model,make,engine,rental_rate):
        super().__init__(model,rental_rate) #Access base class attributes
        self.make = make #New Attributes in Car class
        self.engine = engine
    def calculate_rental(self): #To calculate the rental cost
        rental_duration = int(input("Enter the rental duration for Car(in hours):")) #Input from user for rental duration
        self.rental_rate= rental_duration*self.rental_rate #multiplication of duration and rate
        return f"Vehicle type:{self.model},Make:{self.make},Engine:{self.engine},Rental_Cost:{self.rental_rate}"

class Bike(Vehicle):#Subclass
    def __init__(self,model,brand,gear,rental_rate):
        super().__init__(model,rental_rate)
        self.brand=brand #New Attributes in Bike class
        self.gear=gear
    def calculate_rental(self): #polymorphism is implemented here, different inputs are brand and gear
        rental_duration = int(input("Enter the rental duration for Bike(in hours):"))
        self.rental_rate= rental_duration*self.rental_rate
        return f"Vehicle type:{self.model},Brand:{self.brand},Gear:{self.gear},Rental_Cost:{self.rental_rate}"

class Truck(Vehicle):#Subclass
    def __init__(self,model,capacity,fuel_type,rental_rate):
        super().__init__(model,rental_rate)
        self.capacity=capacity #New Attributes in Truck class
        self.fuel_type=fuel_type
    def calculate_rental(self): #polymorphism is implemented here, different inputs are capacity and fuel type
        rental_duration = int(input("Enter the rental duration for Truck(in hours):"))
        self.rental_rate= rental_duration*self.rental_rate
        return f"Vehicle type:{self.model},Load:{self.capacity} tons,Fuel:{self.fuel_type},Rental_Cost:{self.rental_rate}"

print("Calculating rents for different types of Vehicles")
c=Car("Car","Swift","Diesel",600) #c is an object to access Car class
print(c.calculate_rental()) #Calls calculate_rental method inside Car class
b=Bike("Bike","R15",3,300)
print(b.calculate_rental())
t=Truck("Truck",25,"Gasoline",2000)
print(t.calculate_rental())




