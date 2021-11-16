class Bank:
    '''This is a bank class'''
    #default values
    acc_no = None
    bal = 0.0
    pin = None
    ifsc = 4555269
    branch = 'Rajouri'

    def showDetails(self):
        #self = this refers to the current object
        print('Details')
        print('Account No. :',self.acc_no)
        print('Balance :',self.bal)
        print('Branch :',self.branch)



cust_1 = Bank()  #object1

cust_1.acc_no = 4545457899
cust_1.bal += 50000.0
cust_1.pin = 1234
cust_1.showDetails()


print()

cust_2 = Bank()  #object2
cust_2.acc_no = 7878780123
cust_2.bal += 100000.0
cust_2.pin = 8794
cust_2.branch = 'Paschim Vihar'
cust_2.showDetails()

