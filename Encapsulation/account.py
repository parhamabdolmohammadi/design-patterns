class Account:
    # Encapsulation means keeping an object's data and the methods
    # that operate on that data together inside a class.

    def __init__(self, balance):
        # __balance is private.
        # The double underscore prevents users of Account from
        # directly accessing the balance in the normal way.
        # This hides the internal state of the Account.
        self.__balance = balance

    def deposit(self, amount):
        # Instead of directly changing the balance from outside,
        # we provide a method that controls how money is deposited.
        self.set_balance(self.__balance + amount)

    def withdraw(self, amount):
        # The balance is modified through the Account's methods,
        # giving the class control over its internal state.
        self.set_balance(self.__balance - amount)

    def set_balance(self, amount):
        # Provides controlled access for modifying the private balance.
        # Validation could also be added here.
        self.__balance = amount

    def get_balance(self):
        # Provides controlled read access to the private balance.
        return self.__balance
