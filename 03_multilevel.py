import random

class Bank:
    '''This is a bank class'''
    customers = []
    
    #constructor
    def __init__(self): #init means initialize
        self.bank = 'HDFC'
        self.branch = 'Rohini'
        self.acc_no = random.randint(100000,999999)
        self.ifsc = '1014880'
        self.currentUser = {}
        
    def storeDefault(self):
        self.currentUser['Bank'] = self.bank
        self.currentUser['Account'] = self.acc_no
        self.currentUser['Branch'] = self.branch
        self.currentUser['IFSC'] = self.ifsc
        
        self.customers.append(self.currentUser)

    def showAll(self):
        print(self.customers)
       
#inheritance
class Customer(Bank):
    
    def __init__(self,name,age,occ):
        self.cust_name = name
        self.cust_age = age
        self.cust_occ = occ
        super().__init__()   #calling the parent class constructor


    def storeCustomer(self):
        self.currentUser['Name'] = self.cust_name
        self.currentUser['Age'] = self.cust_age
        self.currentUser['Occupation'] = self.cust_occ
        
        
    def showCurrentCustomer(self):
        print('Welcome to {} bank.'.format(self.bank))
        print('Branch is',self.branch)
        print('Details of Customer : ')
        print(self.currentUser)
        print('-'*60)

class Employee(Customer):
    
    def __init__(self,name,age,acc_type,sal):
        self.name = name
        self.age = age
        self.occ = 'Employee'
        self.acc_type = acc_type
        self.sal = sal
        super().__init__(self.name,self.age,self.occ)  #init func has parameters or not

    def storeEmp(self):
        self.currentUser['Employee'] = self.name
        self.currentUser['Salary'] = self.sal
        self.currentUser['Account_Type'] = self.acc_type
        self.currentUser['Emp_Age'] = self.age

    #overriding
    def showCurrentCustomer(self):
        print('Welcome to {} bank.'.format(self.bank))
        print('Branch is',self.branch)
        print('Details of Customer : ')
        print(self.currentUser)
        print('-'*60)
        self.checkLoan()

    def checkLoan(self):
        print('Loan option Available for employees...')
        if self.sal >=50000:
            print('Loan available upto 10 Lakhs.')
        elif self.sal >= 30000 and self.sal < 50000:
            print('Loan available upto 5 Lakhs.')
        else:
            print('Loan not available.')



obj = Employee('Ram',40,'Savings',70000)
obj.storeDefault()
obj.storeCustomer()
obj.storeEmp()
obj.showCurrentCustomer()
