class Bank:
    '''This is a bank class'''
    
    ifsc = 4555269
    branch = 'Rajouri'

    #constructor
    def __init__(self): #init means initialize
        self.name = None
        self.acc_no = None
        self.bal = 0.0
        self.pin = None
        self.details = []
        
    
    #normal func
    def showDetails(self):
        #self = this refers to the current object
        print('Details')
        self.details.append([self.name,self.acc_no,self.bal,self.pin,self.ifsc,self.branch])
        #print(self.details)



    #destructor function
    def __del__(self):
        print('Object of {} is destroyed'.format(self.name))

cust_1 = Bank()  #object1

cust_1.acc_no = 4545457899
cust_1.bal += 50000.0
cust_1.pin = 1234
cust_1.name = 'John'
cust_1.showDetails()
print(cust_1.details)

#it will __del__ for object 1
del cust_1

print()

cust_2 = Bank()  #object2
cust_2.acc_no = 7878780123
cust_2.bal += 100000.0
cust_2.pin = 8794
cust_2.branch = 'Paschim Vihar'
cust_2.name = 'James'
cust_2.showDetails()
print(cust_2.details)
print()
print(cust_1.details)
