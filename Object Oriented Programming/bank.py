
class Bank:
    bank_name = 'sbk'
    branch = 'kuttampuzha'
    def __init__(self, accno, person_name, balance):
        self.accno = accno
        self.person_name = person_name
        self.balance = balance
        print('Thank you from', Bank.bank_name)


    def deposit(self, ammount):
        self.balance+=ammount
        print('your account no:', self.accno,'credited with', ammount, 'your available balance', self.balance)


    def withdraw(self, ammount):

        if ammount > self.balance:
            print('in sufficiant balance')
        else:
            self.balance-= ammount
            print('your account no:', self.accno, 'debited with', ammount, 'your available balance', self.balance)



    def balance_enq(self):
        print('your current balance:', self.balance)

    @staticmethod
    def welcome():
        print('Welcome to sbk')

    @classmethod
    def branchname(cls):
        print('Branch:',Bank.branch)

Bank.welcome()
Bank.branchname()
accno = int(input('enter acc no'))
name = input('enter name')
balance = int(input('Enter your Ammount'))

ob = Bank(accno,name,balance)
option = input("press 'd' for Deposite or press 'w' for Widraw or press 'b' for balance enquiry")
if option == 'd':
    damount = int(input('enter amount to deposite'))
    ob.deposit(damount)
elif option == 'w':
    wamount = int(input('enter amount to widraw'))
    ob.withdraw(wamount)
elif option == 'b':
    ob.balance_enq()
else:
    print('you choose a wrong command')

