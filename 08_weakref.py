import weakref

class Bank:
    
    branch = 'Rohini'
    ifsc = 657586
    
    def __init__(self,name,acc_no,bal,pin):
        print('Constructor called...')
        self.name = name 
        self.acc_no = acc_no  
        self.bal = bal
        self.pin = pin 
        self.details = []

    def showDetails(self):
        print('Details')
        self.details.append([self.acc_no,self.bal,self.pin,self.branch,self.ifsc])
        print(self.details)

    def __del__(self):
        print('Object of {} is destroyed.'.format(self.name))


cust_1 = Bank('John',87845458879,75000,1234)
#making a copy of object 1
#obj_copy = cust_1

#storage was saved bcz we didnt copy the whole object
ref = weakref.ref(cust_1)
print('Object :',cust_1)
print('Ref :',ref)
print('Calling Ref : ',ref())


print('Deleting Reference now...')
del cust_1
#del obj_copy

print()
print('Calling reference again..',ref())

        
