"""
OBSERVER PATTERN - PULL MODEL

What is Observer?
- Observer is a behavioral design pattern.
- It defines a one-to-many relationship between objects.
- When the Subject changes, all subscribed Observers are notified.

This implementation uses the PULL MODEL:
- Subject does NOT send the changed data to observers.
- Subject simply tells observers that something changed:
      observer.update()
- Each observer then PULLS whatever information it needs
  from the Concrete Subject.

Example:
- SpreadSheet only needs value.
- Chart needs value and timestamp.
- Each observer decides what data it needs.


Why Pull instead of Push?
-------------------------
PUSH:
    observer.update(value)

The Subject decides what information every observer receives.

Problem:
If a new observer needs:
    value + timestamp + something_else

we may have to modify update() and notify().


PULL:
    observer.update()

The Subject only says:
    "Something changed."

Then:
    SpreadSheet -> get_value()
    Chart       -> get_value() + get_timestamp()

This makes observers more flexible because each observer
can retrieve a different set of information.


PATTERN PARTICIPANTS:
---------------------

Subject:
- Maintains the list of observers.
- attach() subscribes an observer.
- detach() unsubscribes an observer.
- notify() tells all observers something changed.

Observer:
- Defines the update() contract.

DataSource:
- Concrete Subject.
- Contains the actual state/data.
- Notifies observers when its state changes.

SpreadSheet / Chart:
- Concrete Observers.
- React to changes by pulling the data they need.


DESIGN PRINCIPLES:
------------------

Open/Closed Principle:
- New Observer types can be added without modifying Subject.
- Example: Logger, EmailService, Dashboard, etc.

Polymorphism:
- Subject can loop through different Observer implementations
  and call update() on all of them.

Abstraction:
- Subject depends on the Observer abstraction.
- It does not depend on SpreadSheet, Chart, or other concrete observers.

Encapsulation:
- Each observer contains its own update behavior.
- DataSource manages its own state.

Decoupling:
- Subject does not know what data each observer needs.
- It only knows that every Observer has update().
"""


from abc import ABC, abstractmethod


# ==================================================
# OBSERVER INTERFACE
#
# Every concrete observer must implement update().
# ==================================================

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


# ==================================================
# SUBJECT / OBSERVABLE
#
# Contains the common observer-management functionality.
# It does not know the concrete types of its observers.
# ==================================================

class Subject:

    def __init__(self):
        self.__observers = []

    # Subscribe an observer.
    def attach(self, observer: Observer):
        self.__observers.append(observer)

    # Unsubscribe an observer.
    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    # Notify all subscribed observers.
    #
    # PULL MODEL:
    # No data is passed to update().
    # Observers decide what data they want to retrieve.
    def notify(self):
        for observer in self.__observers:
            observer.update()


# ==================================================
# CONCRETE SUBJECT
#
# Stores the actual state.
# When its state changes, it notifies its observers.
# ==================================================

class DataSource(Subject):

    def __init__(self):
        # Initialize Subject's observer list.
        super().__init__()

        self.__value = None
        self.__timestamp = None

    def get_value(self):
        return self.__value

    def get_timestamp(self):
        return self.__timestamp

    def set_value(self, value):
        self.__value = value

        # Don't tell observers WHAT changed.
        # Simply tell them that something changed.
        self.notify()


# ==================================================
# CONCRETE OBSERVER
#
# Spreadsheet only cares about value.
# It pulls only value from DataSource.
# ==================================================

class SpreadSheet(Observer):

    def __init__(self, data_source):
        self.__data_source = data_source

    def update(self):
        value = self.__data_source.get_value()

        print(f"Spreadsheet Updated {value}")


# ==================================================
# CONCRETE OBSERVER
#
# Chart needs more information than SpreadSheet.
# It independently decides to pull both value and timestamp.
# ==================================================

class Chart(Observer):

    def __init__(self, data_source):
        self.__data_source = data_source

    def update(self):
        value = self.__data_source.get_value()
        timestamp = self.__data_source.get_timestamp()

        print(f"Chart Updated: value={value}, timestamp={timestamp}")


# ==================================================
# CLIENT / MAIN
# ==================================================

if __name__ == "__main__":

    # Create the Concrete Subject.
    data_source = DataSource()

    # Create observers and give them access to the DataSource
    # so they can pull data from it when update() is called.
    spreadsheet = SpreadSheet(data_source)
    chart = Chart(data_source)

    # Subscribe both observers.
    data_source.attach(spreadsheet)
    data_source.attach(chart)

    # Change DataSource state.
    #
    # set_value()
    #      ↓
    # notify()
    #      ↓
    # observer.update()
    #      ↓
    # each observer pulls what it needs
    data_source.set_value(10)
