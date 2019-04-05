class BankAccount:

    total_money = 0

    def __init__(self, account_type, starting_balance = 0):
        print('Creating a new account of type', account_type, 'with a balance of', starting_balance)

        self.account_type = account_type
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
        print('New balance for this account is: $', self.balance, sep=)



fido = BankAccount('savings', 1000)
ruby = BankAccount('checking')
