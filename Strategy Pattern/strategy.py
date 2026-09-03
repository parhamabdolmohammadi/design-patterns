"""
STRATEGY PATTERN

What is the Strategy Pattern?
- Strategy is a behavioral design pattern.
- It defines a family of algorithms/behaviors, puts each one in a separate class,
  and makes them interchangeable.
- The client can choose which strategy (algorithm) to use at runtime.
- The class using the strategy does not need to know how the algorithm is implemented.

In this example:
- Compressor is one strategy interface.
    -> JpegCompressor and PngCompressor are different compression strategies.

- Filter is another strategy interface.
    -> BlackAndWhite and HighContrast are different filtering strategies.

- ImageStorage is the Context.
    -> It uses the strategies without knowing their implementation details.


Single Responsibility Principle:
- ImageStorage is responsible for storing the image.
- Compression logic is handled by Compressor classes.
- Filtering logic is handled by Filter classes.
- Each class has one clear responsibility.

Open/Closed Principle:
- We can add new compressors or filters by creating new classes.
- Existing code such as ImageStorage does not need to be modified.
- Open for extension, closed for modification.

Polymorphism:
- ImageStorage can work with different Compressor implementations
  without knowing their concrete types.
- The same applies to different Filter implementations.

Abstraction:
- ImageStorage depends on the Compressor and Filter abstractions.
- It does not need to know HOW compression or filtering is performed.

Encapsulation:
- Each algorithm is encapsulated inside its own class.
- For example, JPEG compression logic belongs to JpegCompressor.


Difference between Strategy and State:

STRATEGY:
- The client chooses which algorithm/behavior(strategy) to use.
- Used when there are different ways of performing an operation.

STATE:
- An object's behavior changes depending on its current state.
- Used when an object behaves differently as its state changes.

Simple way to remember:

Strategy = "HOW should I do this?"
State    = "HOW should I behave right now?"
"""

from abc import ABC, abstractmethod


# ---------------- COMPRESSOR STRATEGY ----------------

class Compressor(ABC):

    @abstractmethod
    def compress(self):
        pass


class JpegCompressor(Compressor):

    def compress(self):
        print("Compressing using JPEG")


class PngCompressor(Compressor):

    def compress(self):
        print("Compressing using PNG")


# ---------------- FILTER STRATEGY ----------------

class Filter(ABC):

    @abstractmethod
    def apply(self):
        pass


class BlackAndWhite(Filter):

    def apply(self):
        print("Applying Black and White filter")


class HighContrast(Filter):

    def apply(self):
        print("Applying High Contrast filter")


# ---------------- CONTEXT ----------------

class ImageStorage:

    def store(self, compressor: Compressor, filter: Filter):

        compressor.compress()
        filter.apply()

        print("Storing image")


if __name__ == "__main__":

    storage = ImageStorage()

    storage.store(
        JpegCompressor(),
        BlackAndWhite()
    )

    storage.store(
        PngCompressor(),
        HighContrast()
    )
