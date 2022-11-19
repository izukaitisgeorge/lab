class Account:
    """
    A class representing details for an account
    """

    def __int__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object

        :param name: The name on account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit in an account.
        :param amount: Amount being deposited
        :return: Whether deposit was successful or not
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw from an account
        :param amount: Amount being withdrawn
        :return: Whether withdrawal was successful.
        """

        if amount <= 0:
            return False
        elif self.__account_balance < amount:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access account balance
        :return: The account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access the name on the account
        :return: Name on the account
        """
        return self.__account_name
