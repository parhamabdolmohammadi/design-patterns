"""
PROXY PATTERN

What is Proxy?
- Proxy is a structural design pattern.
- It provides a substitute/placeholder for another object.
- The Proxy implements the same interface as the real object,
  so the client can use either one without knowing the difference.

Problem:
- Creating an Ebook immediately loads the ebook into memory.
- If the library contains thousands of ebooks, they are ALL loaded
  even if the user only opens one of them.

Example:

    filenames = ["a", "b", "c"]

Without Proxy:

    Ebook("a") → loads a
    Ebook("b") → loads b
    Ebook("c") → loads c

Even if we only:

    library.open("a")

we unnecessarily loaded b and c.


Solution:
- Create a common Ebook interface.
- RealEbook performs the expensive loading.
- EbookProxy represents an Ebook without loading it immediately.
- The real Ebook is created only when show() is called.

This is called:
    LAZY LOADING

In this example:

Ebook       = Subject interface
RealEbook   = Real Subject
EbookProxy  = Proxy
Library     = Client


OPEN/CLOSED PRINCIPLE:
- Library depends on the Ebook abstraction instead of RealEbook.
- We can introduce other Ebook implementations/proxies without
  changing Library.
- For example:
      LoggingEbook
      CachedEbook
      ProtectedEbook
- Library remains closed for modification but open for extension.


Key idea:

    Client → Proxy → Real Object

The client thinks it is working with a normal Ebook.

The Proxy decides when the expensive RealEbook should actually
be created and loaded.
"""


from abc import ABC, abstractmethod


# ==================================================
# SUBJECT INTERFACE
#
# Both RealEbook and EbookProxy follow this interface.
# This allows Library to treat them the same way.
# ==================================================

class Ebook(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def get_file_name(self):
        pass


# ==================================================
# REAL SUBJECT
#
# This is the expensive object.
# Creating it causes the ebook to be loaded into memory.
# ==================================================

class RealEbook(Ebook):

    def __init__(self, filename: str):
        self.__file_name = filename

        # Expensive operation
        self.__load()

    def __load(self):
        print("Loading the ebook " + self.__file_name)

    def show(self):
        print("Showing the ebook " + self.__file_name)

    def get_file_name(self):
        return self.__file_name


# ==================================================
# PROXY
#
# Looks like an Ebook because it implements Ebook.
#
# But it does NOT create RealEbook immediately.
# It waits until show() is actually requested.
# ==================================================

class EbookProxy(Ebook):

    def __init__(self, filename: str):
        self.__file_name = filename

        # Real object does not exist yet.
        self.__ebook: RealEbook | None = None

    def show(self):

        # LAZY LOADING:
        # Create the expensive RealEbook only when needed.
        if self.__ebook is None:
            self.__ebook = RealEbook(self.__file_name)

        # Delegate the real work to RealEbook.
        self.__ebook.show()

    def get_file_name(self):
        return self.__file_name


# ==================================================
# LIBRARY / CLIENT
#
# Library depends on Ebook, NOT RealEbook.
#
# Because both RealEbook and EbookProxy implement Ebook,
# Library doesn't care which implementation it receives.
#
# This also supports the Open/Closed Principle.
# ==================================================

class Library:

    def __init__(self):
        self.__ebooks: dict[str, Ebook] = {}

    def add(self, ebook: Ebook):
        self.__ebooks[ebook.get_file_name()] = ebook

    def open(self, filename: str):
        ebook = self.__ebooks.get(filename)

        if ebook is not None:
            ebook.show()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    library = Library()

    filenames = ["a", "b", "c"]

    # We create lightweight proxies.
    #
    # The actual ebooks are NOT loaded here.
    for filename in filenames:
        library.add(
            EbookProxy(filename)
        )

        """
        Super IMPORTANT
    With the proxy, you can register all three filenames cheaply:

    library.add(EbookProxy("a"))
    library.add(EbookProxy("b"))
    library.add(EbookProxy("c"))
    """
    print("Library created")
    print("-----")

    # Only ebook "a" is loaded because it is the only
    # ebook that we actually open.
    library.open("a")
