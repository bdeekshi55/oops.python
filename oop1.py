class HDFCBankAccount:
    def __init__(self, user_name, main_bal, pin=1234):
        self.name = user_name
        self.__MainBal = main_bal
        self.__pin = pin
        self.__account_Active_Status = True
        self.__isAtmCardHolder = False
        self.__isCheckBookHolder = False
        self.__isAtmCardGotFreezed = False

    def __verifyPin(self, pin):
        return self.__pin == pin

    def __updateMainBalByWithDraw(self, amount):
        self.__MainBal -= amount
        print(f"You have withdrawn {amount}. Available Balance: {self.__MainBal}")

    def __updateMainBalByDeposit(self, amount):
        self.__MainBal += amount
        print(f" You have deposited {amount}. Available Balance: {self.__MainBal}")

    def __show_MainBal(self):
        print(f" Available Balance: {self.__MainBal}")

    def withdraw(self, amount, pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                if amount > self.__MainBal:
                    print("Insufficient Balance")
                else:
                    self.__updateMainBalByWithDraw(amount)
            else:
                print("Incorrect PIN")
        else:
            print("Account not active")

    def deposit(self, amount, pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                self.__updateMainBalByDeposit(amount)
            else:
                print(" Incorrect PIN")
        else:
            print("Account not active")

    def check_Bal(self, pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                self.__show_MainBal()
            else:
                print("Incorrect PIN")


class SavingAccount(HDFCBankAccount):
    def __init__(self, name, bal):
        self.loanLimit = 300000
        super().__init__(name, bal)

    def personalLoanRaise(self, amount):
        if amount > self.loanLimit:
            print(" Loan request exceeds limit")
        else:
            print("Loan request approved within limit")


class BusinessAccount(HDFCBankAccount):
    def __init__(self, name, bal):
        self.loanLimit = 2000000
        super().__init__(name, bal)

    def businessLoanRaise(self, amount):
        if amount > self.loanLimit:
            print(" Loan request exceeds limit")
        else:
            print("Loan request approved within limit")

# Creating accounts
sAccount = SavingAccount("Vamsi", 50000)
bAccount = BusinessAccount("Rakesh", 1000000)

print("\n--- Saving Account Transactions ---")
sAccount.check_Bal(1234)      # Check balance
sAccount.deposit(10000, 1234) # Deposit
sAccount.withdraw(2000, 1234) # Withdraw
sAccount.check_Bal(1234)      # Final balance

print("\n--- Business Account Transactions ---")
bAccount.check_Bal(1234)
bAccount.businessLoanRaise(500000)  # Loan request within limit
bAccount.deposit(20000, 1234)
bAccount.withdraw(50000, 1234)
bAccount.check_Bal(1234)
