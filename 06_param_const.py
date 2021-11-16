class Bank:
    '''This is a bank class'''
    
    ifsc = 4555269
    branch = 'Rajouri'

    #paramterized constructor
    def __init__(self,name,acc_no,bal,pin): #init means initialize
        self.name = name
        self.acc_no = acc_no
        self.bal = bal
        self.pin = pin
        self.details = []
        
    
    #normal func
    def showDetails(self):
        #self = this refers to the current object
        print('Details')
        self.details.append([self.name,self.acc_no,self.bal,self.pin,self.ifsc,self.branch])
        print(self.details)


    #destructor function
    def __del__(self):
        print('Object of {} is destroyed.'.format(self.name))

cust_1 = Bank('Ram',4587854574,10000.0,8798)  #object1
cust_1.showDetails()

copy_1 = cust_1
#it will __del__ for object 1
del cust_1

print()

cust_2 = Bank('John',9275472554,9000.0,4567)  #object2

cust_2.showDetails()


print("Copy of object 1 details")
copy_1.showDetails()

