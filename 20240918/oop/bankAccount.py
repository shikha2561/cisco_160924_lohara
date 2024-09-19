class Account:
    def __init__(self, number, name, initial_amount=1000):
        self._number = number
        self._name = name
        self._balance = initial_amount
    def __repr__(self):
        return f'[number={self.__number}, name={self.__name}, balance={self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
         self.__balance -= amount


rohit_ac = Account(name='Rohit' , number= ' 1345567', initial_amount=3000)
print(rohit_ac)

rohit_ac.deposit(10000)
print(rohit_ac)

rohit_ac.withdraw(10000)
print(rohit_ac)

rohit_ac.deposit(10000)
print(rohit_ac)


        

        
        



    