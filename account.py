class Account:
    def __init__(self, name: str):
        """
        Creates a new instance of the Account class
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: int) -> bool:
        """
        Deposits the amount given into the account
        :param amount: The amount of money to deposit.
        :return: True if the deposit was successful, else False.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        """
        Takes out however much money is given in the amount into the account
        :param amount: The amount of money to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if (amount > 0) and (amount <= self.account_balance):
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> int:
        """
        Returns the current balance
        :return: The current balance of the account.
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        Returns the name of the account owner
        :return: The name of the account owner.
        """
        return self.account_name
