class Account:

    account="Bank Account"

    def __init__(self,account_number,balance,account_name):
       
       self.account_name=account_name
       self.account_number=account_number
       self.balance=balance

    def get_withdrawal(self):
        return f"I withdrew  {20000-self.balance} kshs from my {self.account}"
    
    def get_account_name(self):
        return f" {self.account} was lock due to the errors in the {self.account_name}"
    
    def check_account_number(self):
        return {self.account_number}


    