"""
COMPOSITE PATTERN

What is Composite?
- Composite is a structural design pattern.
- It allows us to treat individual objects and groups of objects
  in the same way through a common interface.

Problem:
- Without a common interface, we may need to check the type
  of each object using isinstance().
- As we add new types, we may need more type checks and modify
  existing code, which can violate the Open/Closed Principle.

Solution:
- Create a common Component interface.
- Both individual objects and groups implement Component.
- The client works with Component without caring whether it is
  a single Shape or an entire Group.

In this example:
- Component = common interface
- Shape = Leaf
- Group = Composite
- Group contains a list of Components

Key idea:
    Treat a single object and a collection of objects uniformly.

Structure:

                Component
                render()
                   ↑
            ┌──────┴──────┐
            │             │
          Shape          Group
          (Leaf)       (Composite)
                          │
                          │ contains
                          ↓
                    List[Component]

Benefits:
- No isinstance() checks are needed.
- Shape and Group can be treated the same way.
- Groups can contain other Groups.
- New Component types can be added without changing Group.
- Supports the Open/Closed Principle.
"""


from abc import ABC, abstractmethod


# ==================================================
# COMPONENT INTERFACE
#
# Defines the common operation for both:
# - individual objects (Leaf)
# - groups of objects (Composite)
# ==================================================

class Component(ABC):

    @abstractmethod
    def render(self):
        pass


# ==================================================
# LEAF
#
# A Shape is an individual object.
# It does not contain other Components.
# ==================================================

class Shape(Component):

    def render(self):
        print("Render Shape")


# ==================================================
# COMPOSITE
#
# A Group is also a Component.
#
# However, unlike Shape, it can contain other Components.
# Those Components can be:
# - Shapes
# - Groups
# - any future class implementing Component
# ==================================================

class Group(Component):

    def __init__(self):
        self.__objects: list[Component] = []

    def add(self, component: Component):
        self.__objects.append(component)

    def render(self):

        # We don't care whether component is a
        # Shape or another Group.
        #
        # Polymorphism decides which render()
        # implementation gets executed.
        for component in self.__objects:
            component.render()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    # -----------------------------
    # First group
    # -----------------------------

    group1 = Group()

    group1.add(Shape())
    group1.add(Shape())

    # -----------------------------
    # Second group
    # -----------------------------

    group2 = Group()

    group2.add(Shape())
    group2.add(Shape())

    # -----------------------------
    # Parent group
    #
    # Notice that Group itself is a Component,
    # so a Group can contain other Groups.
    # -----------------------------

    group = Group()

    group.add(group1)
    group.add(group2)

    # -----------------------------
    # Render everything
    #
    # We only call render() once on the
    # outermost Group.
    # -----------------------------

    group.render()
