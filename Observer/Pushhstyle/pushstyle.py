
# problem if the new concrete observer needs different set of values
# we have to specify them and adjust the observer manual

"""
OBSERVER PATTERN - PUSH MODEL

What is Observer?
- Observer is a behavioral design pattern.
- It creates a one-to-many relationship between objects.
- When the Subject changes, all registered Observers are notified.

In this implementation:
- Subject stores the observers.
- DataSource is the Concrete Subject.
- Observer is the observer interface.
- SpreadSheet and Chart are Concrete Observers.

This version uses the PUSH model:
- The Subject pushes the changed value directly to observers.
- observer.update(value)

Advantage:
- Simple and easy when every observer needs the same data.

Problem:
- If different observers need different sets of data later,
  the Subject may need to change what it passes to update().
- That can increase coupling between Subject and Observers.

Example:
    SpreadSheet may need only value.
    Chart may need value + timestamp.
    Logger may need value + user_id.

Then update(value) may no longer be flexible enough.

A possible alternative is the PULL model:
- Subject only calls observer.update()
- Each observer retrieves whatever data it needs from the Subject.

Open/Closed:
New observers can be added without changing Subject/DataSource.

Polymorphism:
Subject loops through different observer types and calls update().

Abstraction:
Subject depends on Observer, not SpreadSheet or Chart.

Decoupling:
DataSource does not know exactly what each observer does.

Limitation of this version:
The Subject decides what data is pushed to all observers.
"""


# ==================================================
# OBSERVER INTERFACE
# ==================================================

from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, value: int):
        pass


# ==================================================
# SUBJECT / OBSERVABLE
# Contains the common observer-management behavior.
# ==================================================

class Subject:

    def __init__(self):
        self.__observers = []

    def attach(self, observer: Observer):
        self.__observers.append(observer)

    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self, value):
        for observer in self.__observers:
            observer.update(value)


# ==================================================
# CONCRETE SUBJECT
# Inherits observer management from Subject.
# Only worries about its own data.
# ==================================================

class DataSource(Subject):

    def __init__(self):
        super().__init__()
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
        self.notify(value)


# ==================================================
# CONCRETE OBSERVERS
# ==================================================

class SpreadSheet(Observer):

    def update(self, value: int):
        print(f"Spreadsheet Updated {value}")


class Chart(Observer):

    def update(self, value: int):
        print(f"Chart Updated {value}")


if __name__ == "__main__":

    data_source = DataSource()

    spreadsheet = SpreadSheet()
    chart = Chart()

    data_source.attach(spreadsheet)
    data_source.attach(chart)

    data_source.set_value(10)
