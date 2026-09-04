"""
MEDIATOR PATTERN

What is Mediator?
- Mediator is a behavioral design pattern.
- It reduces direct dependencies between objects.
- Instead of UI controls talking directly to each other,
  they communicate through a Mediator.

In this example:

UIControl
- Base class for all UI controls.
- Stores a reference to its owner/mediator.

DialogBox
- Mediator interface.
- Defines changed(), which is called whenever a control changes.

ArticleDialogBox
- Concrete Mediator.
- Coordinates ListBox, TextBox, and Button.

ListBox / TextBox / Button
- Colleague components.
- They do NOT directly know about each other.
- They only notify their mediator.

Flow example:

ListBox changes
      ↓
notifies ArticleDialogBox
      ↓
ArticleDialogBox updates TextBox
      ↓
TextBox changes
      ↓
notifies ArticleDialogBox
      ↓
ArticleDialogBox updates Button
"""


from abc import ABC, abstractmethod


# ==================================================
# BASE UI CONTROL
#
# Every control stores a reference to its mediator.
# ==================================================

class UIControl:

    def __init__(self, owner):
        self._owner = owner


# ==================================================
# MEDIATOR INTERFACE
#
# All concrete mediators must implement changed().
# ==================================================

class DialogBox(ABC):

    @abstractmethod
    def changed(self, control: UIControl):
        pass


# ==================================================
# LIST BOX
#
# Concrete colleague.
# When its selection changes, it notifies the mediator.
# ==================================================

class ListBox(UIControl):

    def __init__(self, owner):
        super().__init__(owner)
        self.__selection = None

    def set_selection(self, selection):
        self.__selection = selection

        # Notify the mediator that this control changed.
        self._owner.changed(self)

    def get_selection(self):
        return self.__selection


# ==================================================
# TEXT BOX
#
# Concrete colleague.
# When its content changes, it notifies the mediator.
# ==================================================

class TextBox(UIControl):

    def __init__(self, owner):
        super().__init__(owner)
        self.__content = None

    def set_content(self, content):
        self.__content = content

        # Notify the mediator.
        self._owner.changed(self)

    def get_content(self):
        return self.__content


# ==================================================
# BUTTON
#
# Concrete colleague.
#
# In this example, changing enabled state does NOT need
# to notify the mediator because the mediator itself is
# deciding when the button should be enabled/disabled.
# ==================================================

class Button(UIControl):

    def __init__(self, owner):
        super().__init__(owner)
        self.__enabled = False

    def set_enabled(self, enabled):
        self.__enabled = enabled

    def get_enabled(self):
        return self.__enabled


# ==================================================
# CONCRETE MEDIATOR
#
# Knows how the controls should interact with each other.
#
# The controls themselves do not contain this coordination
# logic.
# ==================================================

class ArticleDialogBox(DialogBox):

    def __init__(self):

        # Every control receives this mediator as its owner.
        self.__articles_list_box = ListBox(self)
        self.__title_text_box = TextBox(self)
        self.__save_button = Button(self)

    # --------------------------------------------------
    # MEDIATOR METHOD
    #
    # Determines which control changed and decides
    # what should happen next.
    # --------------------------------------------------

    def changed(self, control: UIControl):

        if control == self.__articles_list_box:
            self.article_selected()

        elif control == self.__title_text_box:
            self.title_changed()

    # --------------------------------------------------
    # Called when the ListBox selection changes.
    #
    # The mediator takes the selected article and updates
    # the TextBox.
    # --------------------------------------------------

    def article_selected(self):

        selection = self.__articles_list_box.get_selection()

        self.__title_text_box.set_content(selection)

    # --------------------------------------------------
    # Called when the TextBox content changes.
    #
    # If the title is empty:
    #     disable Save
    #
    # Otherwise:
    #     enable Save
    # --------------------------------------------------

    def title_changed(self):

        content = self.__title_text_box.get_content()

        is_empty = content is None or content == ""

        self.__save_button.set_enabled(not is_empty)

    # --------------------------------------------------
    # Used only to simulate the user interacting with
    # the dialog.
    # --------------------------------------------------

    def simulate_user_interaction(self):

        # User selects an article.
        self.__articles_list_box.set_selection("Article 1")

        print(
            f"TextBox: {self.__title_text_box.get_content()}"
        )

        print(
            f"Button enabled: {self.__save_button.get_enabled()}"
        )


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    dialog_box = ArticleDialogBox()

    dialog_box.simulate_user_interaction()
