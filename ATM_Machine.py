class ATM:
    def __init__(self):
        self.__PIN = 0
        self.__Balance = 0
        self.__menu()

    def __menu(self):
        User_Input = input('''
        1 - Set Your PIN.
        2 - Check Your Balance.
        3 - Withdraw.
        4 - Deposit.
        5 - To Exit
        Enter your Choice: ''')
        
        if User_Input == '1':
            self.set_pin()
        elif User_Input == '2':
            self.check_balance()
        elif User_Input == '3':
            self.withdraw()
        elif User_Input == '4':
            self.deposit()
        elif User_Input == '5':
            print("Thank You For Visiting...")
        else:
            print("Choose a appropriate choice")


    def set_pin(self):
        self.__PIN = int(input("Enter Yor PIN: "))
        print("PIN set successfully")
        self.__menu()

    def check_balance(self):
        pin = int(input("Enter Your PIN: "))
        if pin == self.__PIN:
            print("Your current balance is: ", self.Balance)
            self.__menu()
        else:
            print("Invalid PIN. Try again...")
            self.__menu()

    def withdraw(self):
        pin = int(input("Enter Your PIN: "))
        if pin == self.__PIN:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.__Balance:
                self.__Balance = self.__Balance - amount
                print("Collect Your Cash.")
                self.__menu()
            else:
                print("The withdrawl amount is more then your balance")
        else:
            print("Invalid PIN. Try again...")
            self.__menu()

    def deposit(self):
        pin = int(input("Enter Your PIN: "))
        if pin == self.__PIN:
            amount = int(input("Enter the amount to deposit: "))
            self.__Balance = self.__Balance + amount
            print("Your cash has been Deposited.")
            self.__menu()
        else:
            print("Invalid PIN. Try again...")
            self.__menu()
