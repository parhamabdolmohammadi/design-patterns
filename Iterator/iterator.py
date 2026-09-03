from abc import ABC, abstractmethod


# ITERATOR INTERFACE
# Defines the operations that every iterator must provide.
class Iterator(ABC):

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass


# CONCRETE ITERATOR
# Knows how to iterate over a list.
class ListIterator(Iterator):

    def __init__(self, history):
        self.__history = history
        self.__index = 0

    def current(self):
        return self.__history[self.__index]

    def next(self):
        self.__index += 1

    def is_done(self):
        return self.__index >= len(self.__history)


# CONCRETE ITERATOR
# Another possible way of traversing the collection.
class ArrayIterator(Iterator):

    def __init__(self, history):
        self.__history = history
        self.__index = 0

    def current(self):
        return self.__history[self.__index]

    def next(self):
        self.__index += 1

    def is_done(self):
        return self.__index >= len(self.__history)


# COLLECTION
# Stores the data but doesn't expose it directly to the client.
class BrowseHistory:

    def __init__(self):
        self.__urls = []

    def push(self, url: str):
        self.__urls.append(url)

    def pop(self):
        return self.__urls.pop()

    def create_iterator(self) -> Iterator:
        return ListIterator(self.__urls)


if __name__ == "__main__":

    history = BrowseHistory()

    history.push("a")
    history.push("b")
    history.push("c")

    iterator = history.create_iterator()

    while not iterator.is_done():
        print(iterator.current())
        iterator.next()
