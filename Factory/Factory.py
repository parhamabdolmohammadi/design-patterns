"""
FACTORY METHOD PATTERN

What is Factory Method?
- Factory Method is a creational design pattern.
- It defines a method for creating an object,
  but lets subclasses decide WHICH concrete object
  should actually be created.

Problem:
- Suppose Controller needs a ViewEngine in order
  to render a page.

- If Controller directly creates MatchaViewEngine:

      engine = MatchaViewEngine()

  then Controller becomes tightly coupled to
  MatchaViewEngine.

- If tomorrow we want another engine such as:

      ReactViewEngine
      BladeViewEngine
      DjangoViewEngine

  we would have to modify Controller.

- That violates the Open/Closed Principle because
  Controller should ideally be open for extension
  but closed for modification.

Solution:
- Controller defines a factory method:

      create_view_engine()

- Controller uses that method instead of directly
  creating a concrete ViewEngine.

- Subclasses override the factory method and decide
  which ViewEngine should be created.

Participants:

1. Product
   - ViewEngine
   - Defines the interface for objects created
     by the factory method.

2. Concrete Product
   - MatchaViewEngine
   - Actual object that gets created.

3. Creator
   - Controller
   - Contains the main operation:
         render()
   - Calls the factory method:
         create_view_engine()

4. Concrete Creator
   - ProductsController
   - Overrides create_view_engine()
   - Returns a MatchaViewEngine.

Flow:

    ProductsController.list_products()
                |
                v
         Controller.render()
                |
                v
     self.create_view_engine()
                |
                v
    ProductsController.create_view_engine()
                |
                v
        MatchaViewEngine()
                |
                v
         engine.render()

Key idea:

    Creator does NOT directly create
    the concrete product.

Instead of:

    engine = MatchaViewEngine()

we do:

    engine = self.create_view_engine()

Then subclasses decide what object gets created.

Benefits:
- Reduces coupling between Creator and Concrete Product.
- Supports Open/Closed Principle.
- Makes it easier to introduce new product types.
- Object creation is delegated to subclasses.

Important:
- Factory Method is about deciding WHICH object
  should be created.
"""


from abc import ABC, abstractmethod


# ==================================================
# PRODUCT
# ==================================================

class ViewEngine(ABC):

    @abstractmethod
    def render(
        self,
        view_name: str,
        context: dict[str, object]
    ) -> str:
        pass


# ==================================================
# CONCRETE PRODUCT
# ==================================================

class MatchaViewEngine(ViewEngine):

    def render(
        self,
        view_name: str,
        context: dict[str, object]
    ) -> str:

        return "View Rendered By Matcha"


# ==================================================
# CREATOR
# ==================================================

class Controller(ABC):

    def render(
        self,
        view_name: str,
        context: dict[str, object]
    ) -> None:

        # We do NOT create MatchaViewEngine directly.
        #
        # Instead, we ask the factory method
        # to create the appropriate ViewEngine.
        engine = self.create_view_engine()

        html = engine.render(view_name, context)

        print(html)

    @abstractmethod
    def create_view_engine(self) -> ViewEngine:
        """
        Factory Method

        Subclasses decide which concrete
        ViewEngine should be created.
        """
        pass


# ==================================================
# CONCRETE CREATOR
# ==================================================

class ProductsController(Controller):

    def create_view_engine(self) -> ViewEngine:

        # Factory Method implementation.
        #
        # ProductsController decides that
        # MatchaViewEngine should be created.
        return MatchaViewEngine()

    def list_products(self) -> None:

        print("Get Products from database")

        context: dict[str, object] = {}

        # render() belongs to Controller.
        self.render("products.html", context)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    controller = ProductsController()

    controller.list_products()
