from abc import ABC, abstractmethod


# COMMAND INTERFACE
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# CONCRETE COMMAND
class ResizeCommand(Command):

    def execute(self):
        print("Resize")


# CONCRETE COMMAND
class BlackAndWhiteCommand(Command):

    def execute(self):
        print("Black and White")


# COMPOSITE COMMAND
# A command that contains multiple commands.
class CompositeCommand(Command):

    def __init__(self):
        self.__commands = []

    def add(self, command: Command):
        self.__commands.append(command)

    def execute(self):
        for command in self.__commands:
            command.execute()


if __name__ == "__main__":

    composite = CompositeCommand()

    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())

    composite.execute()
