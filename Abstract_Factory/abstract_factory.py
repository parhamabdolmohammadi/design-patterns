"""
ABSTRACT FACTORY PATTERN

What is Abstract Factory?
- Abstract Factory is a creational design pattern.
- It provides an interface for creating FAMILIES
  of related objects.

Problem:
- ContactForm directly creates concrete widgets:

      AntTextBox()
      AntButton()

      MaterialTextBox()
      MaterialButton()

- This means ContactForm knows about every theme.

- If we add another theme, such as:

      BootstrapButton
      BootstrapTextBox

  we would have to modify ContactForm.

- This violates the Open/Closed Principle.

- There is also another problem:
  related widgets must match.

  For example:

      MaterialButton + MaterialTextBox

  should be created together.

  We don't want to accidentally create:

      MaterialButton + AntTextBox


Solution:
- Create an abstract factory:

      WidgetFactory

- The factory defines methods for creating
  related widgets:

      create_button()
      create_textbox()

- Each theme gets its own concrete factory:

      MaterialWidgetFactory
      AntWidgetFactory

- ContactForm only works with WidgetFactory.
  It does NOT know which concrete widget classes
  are being created.


Participants:

1. Abstract Products
   - Button
   - TextBox

2. Concrete Products
   - MaterialButton
   - MaterialTextBox
   - AntButton
   - AntTextBox

3. Abstract Factory
   - WidgetFactory

4. Concrete Factories
   - MaterialWidgetFactory
   - AntWidgetFactory

5. Client
   - ContactForm


Flow:

    ContactForm
        |
        v
    WidgetFactory
       /      \
      /        \
Material      Ant
Factory       Factory
   |             |
   v             v
Material      Ant
Widgets       Widgets


Key idea:

    Abstract Factory creates a FAMILY
    of related objects.

For example:

    MaterialWidgetFactory
        -> MaterialButton
        -> MaterialTextBox

    AntWidgetFactory
        -> AntButton
        -> AntTextBox


Benefit:
- ContactForm doesn't depend on concrete widgets.
- New themes can be added without modifying ContactForm.
- Related widgets are created consistently.
- Supports Open/Closed Principle.
"""


from abc import ABC, abstractmethod


# ==================================================
# ABSTRACT PRODUCTS
# ==================================================

class Widget(ABC):

    @abstractmethod
    def render(self):
        pass


class Button(Widget):
    pass


class TextBox(Widget):
    pass


# ==================================================
# MATERIAL DESIGN PRODUCTS
# ==================================================

class MaterialButton(Button):

    def render(self):
        print("Material Button")


class MaterialTextBox(TextBox):

    def render(self):
        print("Material TextBox")


# ==================================================
# ANT DESIGN PRODUCTS
# ==================================================

class AntButton(Button):

    def render(self):
        print("Ant Button")


class AntTextBox(TextBox):

    def render(self):
        print("Ant TextBox")


# ==================================================
# ABSTRACT FACTORY
# ==================================================

class WidgetFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


# ==================================================
# CONCRETE FACTORY - MATERIAL
# ==================================================

class MaterialWidgetFactory(WidgetFactory):

    def create_button(self) -> Button:
        return MaterialButton()

    def create_textbox(self) -> TextBox:
        return MaterialTextBox()


# ==================================================
# CONCRETE FACTORY - ANT
# ==================================================

class AntWidgetFactory(WidgetFactory):

    def create_button(self) -> Button:
        return AntButton()

    def create_textbox(self) -> TextBox:
        return AntTextBox()


# ==================================================
# CLIENT
# ==================================================

class ContactForm:

    def render(self, factory: WidgetFactory):

        textbox = factory.create_textbox()
        button = factory.create_button()

        textbox.render()
        button.render()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    print("Material Theme:")

    material_factory = MaterialWidgetFactory()

    form = ContactForm()
    form.render(material_factory)

    print()

    print("Ant Theme:")

    ant_factory = AntWidgetFactory()

    form.render(ant_factory)
