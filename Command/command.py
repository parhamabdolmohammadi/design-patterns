

from abc import ABC, abstractmethod


class Button:

    def __init__(self, command):
        self.__label = None
        self.__command = command

    def click(self):
        self.__command.execute()

    def get_label(self):
        return self.__label

    def set_label(self, label):
        self.__label = label


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class CustomerService:

    def add_customer(self):
        print("Add customer")


class AddCustomerCommand(Command):

    def __init__(self, service):
        self.__service = service

    def execute(self):
        self.__service.add_customer()


if __name__ == "__main__":
    service = CustomerService()
    command = AddCustomerCommand(service)

    button = Button(command)
    button.click()
