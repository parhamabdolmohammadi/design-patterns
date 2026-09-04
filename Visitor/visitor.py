from abc import ABC, abstractmethod

"""
VISITOR PATTERN

What is Visitor?
- Visitor is a behavioral design pattern.
- It allows us to add new operations to a group of objects
  without changing the classes of those objects.
- Instead of putting every operation inside HtmlNode subclasses,
  we move those operations into separate Visitor classes.

Problem:
- Without Visitor, every new operation such as highlight(),
  plain_text(), export(), etc. would need to be added to HtmlNode
  and implemented by every concrete node.
- This means existing classes must keep changing when new
  operations are introduced, which can violate the Open/Closed Principle.

Solution:
- HtmlNode only defines accept(visitor).
- Each concrete node passes itself to the visitor.
- The Visitor contains the actual operation for each type of node.

In this example:
- HtmlNode = Element interface
- HeadingNode / AnchorNode = Concrete Elements
- Operation = Visitor interface
- HighlightOperation / PlainTextOperation = Concrete Visitors
- HtmlDocument = Object Structure containing the elements

Flow:

    HtmlDocument.execute(visitor)
              ↓
        node.accept(visitor)
              ↓
    visitor.visit_heading(self)
              OR
    visitor.visit_anchor(self)

Benefits:
- Easy to add new operations without modifying HtmlNode classes.
- Keeps operation-specific logic in separate classes.
- Uses polymorphism and follows the Open/Closed Principle
  when adding new operations.

Tradeoff:
- Adding a new Element type (for example ImageNode) requires
  updating the Visitor interface and all existing Visitors.

Easy way to remember:

    Visitor = operations change often, object types stay relatively stable.
"""

# ==================================================
# ELEMENT INTERFACE
# ==================================================


class HtmlNode(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# ==================================================
# CONCRETE ELEMENTS
# ==================================================

class HeadingNode(HtmlNode):
    def __init__(self):
        self.__name = "Heading"

    def get_name(self):
        return self.__name

    def accept(self, visitor):
        visitor.visit_heading(self)


class AnchorNode(HtmlNode):
    def __init__(self):
        self.__name = "Anchor"

    def get_name(self):
        return self.__name

    def accept(self, visitor):
        visitor.visit_anchor(self)


# ==================================================
# VISITOR INTERFACE
#
# Defines an operation for every concrete element type.
# ==================================================

class Operation(ABC):

    @abstractmethod
    def visit_heading(self, heading: HeadingNode):
        pass

    @abstractmethod
    def visit_anchor(self, anchor: AnchorNode):
        pass


# ==================================================
# CONCRETE VISITOR
# Represents one operation: Highlight
# ==================================================

class HighlightOperation(Operation):

    def visit_heading(self, heading: HeadingNode):
        print("Highlight " + heading.get_name())

    def visit_anchor(self, anchor: AnchorNode):
        print("Highlight " + anchor.get_name())


# ==================================================
# ANOTHER CONCRETE VISITOR
# Represents another operation.
# ==================================================

class PlainTextOperation(Operation):

    def visit_heading(self, heading: HeadingNode):
        print(f"Convert {heading.get_name()} to plain text")

    def visit_anchor(self, anchor: AnchorNode):
        print(f"Convert {anchor.get_name()} to plain text")


# ==================================================
# OBJECT STRUCTURE
# Stores the elements.
# ==================================================

class HtmlDocument:

    def __init__(self):
        self.__nodes: list[HtmlNode] = []

    def add(self, node: HtmlNode):
        self.__nodes.append(node)

    def execute(self, operation: Operation):
        for node in self.__nodes:
            node.accept(operation)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    document = HtmlDocument()

    document.add(HeadingNode())
    document.add(AnchorNode())

    # Apply highlight operation
    document.execute(HighlightOperation())

    print("-----")

    # Apply a completely different operation
    # without changing HeadingNode or AnchorNode.
    document.execute(PlainTextOperation())
