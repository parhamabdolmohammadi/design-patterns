"""
ADAPTER PATTERN

What is Adapter?
- Adapter is a structural design pattern.
- It converts the interface of an existing/foreign class
  into the interface that our application expects.

Problem:
- ImageView expects an object that follows the Filter interface:

      filter.apply(image)

- VividFilter already follows that interface.

- Caramel is from an imaginary third-party library and has a
  different interface:

      caramel.init()
      caramel.render(image)

- Because Caramel does not implement Filter, ImageView cannot
  use it directly.

Solution:
- Create CaramelFilter as an Adapter.
- CaramelFilter implements our Filter interface.
- Internally, it translates:

      apply(image)

  into:

      caramel.init()
      caramel.render(image)

In this example:

ImageView      = Client
Filter         = Target interface
VividFilter    = Normal implementation of Target
Caramel        = Adaptee / foreign class
CaramelFilter  = Adapter

Key idea:

    Our system expects:        Filter.apply(image)

    Foreign class provides:    Caramel.render(image)

    Adapter connects them.
"""


from abc import ABC, abstractmethod


# ==================================================
# IMAGE
# ==================================================

class Image:
    pass


# ==================================================
# TARGET INTERFACE
#
# This is the interface ImageView expects.
# ==================================================

class Filter(ABC):

    @abstractmethod
    def apply(self, image: Image):
        pass


# ==================================================
# NORMAL FILTER
#
# Already follows the Filter interface,
# so no adapter is needed.
# ==================================================

class VividFilter(Filter):

    def apply(self, image: Image):
        print("Applying Vivid Filter")


# ==================================================
# CLIENT
#
# ImageView only knows about the Filter abstraction.
# It does not care which concrete filter is used.
# ==================================================

class ImageView:

    def __init__(self, image: Image):
        self.__image = image

    def apply(self, filter: Filter):
        filter.apply(self.__image)


# ==================================================
# FOREIGN / THIRD-PARTY CLASS
#
# Imagine this comes from an external package.
#
# We should not modify it.
#
# Notice that it does NOT have:
#     apply(image)
#
# Instead, it uses:
#     init()
#     render(image)
# ==================================================

class Caramel:

    def init(self):
        print("Initializing Caramel")

    def render(self, image: Image):
        print("Applying Caramel Filter")


# ==================================================
# ADAPTER
#
# Converts the Caramel interface into our Filter interface.
#
# ImageView calls:
#     apply(image)
#
# Adapter translates that into:
#     caramel.init()
#     caramel.render(image)
# ==================================================

class CaramelFilter(Filter):

    def __init__(self, caramel: Caramel):
        self.__caramel = caramel

    def apply(self, image: Image):
        self.__caramel.init()
        self.__caramel.render(image)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    image = Image()

    image_view = ImageView(image)

    # Normal filter already implements Filter.
    image_view.apply(VividFilter())

    print("-----")

    # Caramel cannot be passed directly:
    #
    # image_view.apply(Caramel())   # ❌
    #
    # because Caramel does not implement apply().

    caramel = Caramel()

    # Wrap the incompatible object inside the Adapter.
    caramel_filter = CaramelFilter(caramel)

    # Now ImageView can use it like any other Filter.
    image_view.apply(caramel_filter)
