
# open closed: extendable without making any change
# polymorphysm: looping over different classes and use update function
from abc import ABC, abstractmethod

"""
OBSERVER PATTERN

What is Observer?
- Observer is a behavioral design pattern.
- It creates a one-to-many relationship between objects.
- When one object (Subject) changes, all subscribed objects
  (Observers) are automatically notified.

In this example:

DataSource   = Subject / Observable
Observer     = Observer interface
SpreadSheet  = Concrete Observer
Chart        = Concrete Observer


Flow:

DataSource changes
       ↓
notify_observers()
       ↓
loops through observers
       ↓
obs.update()
       ↓
 ┌─────────────┬───────────┐
 ↓             ↓
SpreadSheet   Chart
 update()     update()


Open/Closed Principle:
- We can add new Observer classes without modifying DataSource.

Polymorphism:
- DataSource stores different types of observers as Observer objects.
- It can call update() on each without knowing whether it is
  a SpreadSheet, Chart, etc.

Abstraction:
- DataSource depends on the Observer abstraction rather than
  concrete classes such as SpreadSheet or Chart.

Decoupling:
- DataSource does not need to know what each observer does.
- It only knows that observers have an update() method.
"""


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class DataSource:

    def __init__(self):
        self.__data_source = None
        self.__observers = list()

    def get_data_source(self):
        return self.__data_source

    def set_data_source(self, ds):
        self.__data_source = ds

        self.notify_observers()

    def add_observer(self, obs: Observer):
        self.__observers.append(obs)

    def notify_observers(self):
        for obs in self.__observers:
            obs.update()


class SpreadSheet(Observer):

    def update(self):
        print("Spreadsheet Updated")


class Chart(Observer):

    def update(self):
        print("Chart Updated")


if __name__ == "__main__":
    data_source = DataSource()

    spreadsheet = SpreadSheet()
    chart = Chart()

    data_source.add_observer(spreadsheet)
    data_source.add_observer(chart)

    data_source.set_data_source(10)
