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
       
#single level inheritance
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

obj = Customer('Ram',40,'Manager')
obj.storeDefault()
obj.storeCustomer()
obj.showCurrentCustomer()

obj2 = Customer('John',20,'Intern')
obj2.storeDefault()
obj2.storeCustomer()
obj2.showCurrentCustomer()
    

