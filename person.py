from bank_account import BankAccount

class Person:
    def __init__(self, first_name, last_name):
        self.__bank_account = None
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def set_bank_account(self, account):
        self.__bank_account = account

    def get_bank_account(self):
        return self.__bank_account

    def open_account(self, account_name, account_number, balance):
        self.set_bank_account(account = BankAccount(account_name = account_name, account_number = account_number, balance = balance))

    #properties
    #person_first_name = property(get_first_name())
    #person_last_name = property(get_last_name())
    #person_bank_account = property(get_bank_account(), set_bank_account())

    def __str__(self):
        if isinstance(self.get_bank_account(), BankAccount):
            return f"{self.get_first_name()} {self.get_last_name()} has a balance of {self.get_bank_account().balance}"
        else:
            return f"{self.get_first_name()} {self.get_last_name()} has no account"

person = Person("Lucy", "Edwards")
person.open_account("123456", "123456", 100)
print(person)

person = Person("William", "Chen")
print(person)

person = Person("Alexander", "Cooke")
print(person.get_first_name())
print(person.get_last_name())