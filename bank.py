class Account:

    account="Bank Account"

    def __init__(self,account_number,account_name,withdrawals, deposits , loan_balance):
       
       self.account_name=account_name
       self.account_number=account_number
       self.withdrawals=[]
       self.deposits=[]
       self.loan_balance=0

    
    def get_account_name(self):
        return f" {self.account} was lock due to the missing character in the {self.account_name}"
    
    def check_account_number(self):
        return {self.account_number}
    _balance = 0.0

    def check_balance(self):
        balance = sum(transaction["amount"] for transaction in self.deposits) - sum(transaction["amount"] for transaction in self.withdrawals) - self.loan_balance
        return balance

    def deposit(self, amount):
        transaction = {
            "amount": amount,
            "narration":"deposit",
            
        }
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = {
            "amount": amount,
            "narration": "withdrawal",

           
        }
        self.withdrawals.append(transaction)

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction} - {transaction}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= sum(transaction["amount"] for transaction in self.deposits) / 3:
            self.loan_balance += amount
            print("Loan approved")
        else:
            print("Loan not approved")

    def repay_loan(self, amount):
        if amount >= self.loan_balance:
            self.loan_balance = 0
            self.deposit(amount - self.loan_balance)
        else:
            self.loan_balance -= amount
            self.deposit(amount)

    def transfer(self, amount, recipient_account):
        if amount <= self.check_balance():
            self.withdrawal(amount)
            recipient_account.deposit(amount)
            print("Transfer  was successful")
        else:
            print("Insufficient balance for transfer")
    


    