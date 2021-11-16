#Class
class Bank:
    '''This is a bank class'''
    acc_no = None
    bal = 0.0
    pin = None
    ifsc = 4555269
    branch = 'Rajouri'

cust_1 = Bank()  #object1

cust_1.acc_no = 454545789
cust_1.bal += 50000.0
cust_1.pin = 1234



cust_2 = Bank()  #object2
cust_2.acc_no = 7878780123
cust_2.bal += 100000.0
cust_2.pin = 8794

print(cust_1.__dict__)
print('-'*75)
print(cust_2.__dict__)

