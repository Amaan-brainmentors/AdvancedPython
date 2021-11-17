class Bank:
    
    branch = 'Rohini'
    ifsc = 657586
    
    def __init__(self,name,acc_no,bal,pin):
        print('Constructor called...')
        self.name = name #public
        self._acc_no = acc_no  #protected
        self._bal = bal
        self.__pin = pin #private
        self.details = []

    def showDetails(self):
        print('Details')
        self.details.append([self._acc_no,self._bal,self.__pin,self.branch,self.ifsc])
        print(self.details)

    def __del__(self):
        print('Object of {} is destroyed.'.format(self.name))


cust_1 = Bank('John',87845458879,75000,1234)
cust_1.showDetails()

cust_1._acc_no = 9999999999
cust_1.showDetails()
        
