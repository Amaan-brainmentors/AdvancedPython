import random

class Bank:
    '''This is a bank class'''
    #constructor
    def __init__(self): #init means initialize
        self.bank = 'HDFC'
        self.branch = 'Rohini'
        self.acc_no = random.randint(100000,999999)
        self.ifsc = '1014880'
        self.customer = []
        
    def storeCustomer(self):
        self.customer.append([self.acc_no,self.branch,self.ifsc])
       
    
#single level inheritance
class Customer(Bank):

    def __init__(self,name,age,occ):
        self.cust_name = name
        self.cust_age = age
        self.cust_occ = occ
        super().__init__()   #calling the parent class constructor

    def show(self):
        print('Welcome to {} bank.'.format(self.bank))
        print('Branch is',self.branch)
        print('Details of Customer : ')
        self.customer.append([self.cust_name,self.cust_age,self.cust_occ])
        print(self.customer)
        print('-'*60)

obj = Customer('Ram',40,'Manager')
obj.storeCustomer()
obj.show()




    

