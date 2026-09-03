"""
COMMAND PATTERN WITH UNDO

What is the Command Pattern?
- Command is a behavioral design pattern.
- It turns a request/action into an object.
- The object that requests an operation is separated from the object
  that actually performs the operation.

In this example:

Command             = Base command interface
UndoableCommand     = Interface for commands that can be reversed
BoldCommand         = Concrete undoable command
Document            = Receiver (object actually being modified)
History             = Stores previously executed undoable commands
UndoCommand         = Executes the undo operation


HOW UNDO WORKS:

1. BoldCommand.execute() saves the document's current content.
2. BoldCommand performs the operation.
3. BoldCommand stores itself in History.
4. UndoCommand removes the latest command from History.
5. UndoCommand calls unexecute() on that command.
6. BoldCommand restores the previous content.


Example:

Before:
    "Hello"

BoldCommand.execute():
    previous = "Hello"
    document = "<b>Hello</b>"

UndoCommand.execute():
    document = "Hello"


WHY STORE THE COMMAND IN HISTORY?

History doesn't need to know how to undo every possible operation.

It simply stores UndoableCommand objects:

    BoldCommand
    ResizeCommand
    ItalicCommand
    ...

Every command knows how to undo itself through:

    unexecute()

This uses polymorphism.


---------------------------------------------------------
COMMAND WITH UNDO vs MEMENTO
---------------------------------------------------------

They are similar because both can implement UNDO,
but they store different things.

COMMAND WITH UNDO:
- Stores the operation/action that was performed.
- The command itself knows how to reverse that operation.
- History stores commands.

    History:
        BoldCommand
        ResizeCommand
        ItalicCommand

    Undo:
        command = history.pop()
        command.unexecute()


MEMENTO:
- Stores snapshots of an object's STATE.
- It doesn't necessarily know what operation caused the change.
- History stores states/mementos.

    History:
        EditorState("Hello")
        EditorState("Hello World")
        EditorState("Hello World!!!")

    Undo:
        state = history.pop()
        editor.restore(state)


Easy way to remember:

    Command → remember WHAT WE DID
    Memento → remember WHAT WE HAD

Command:
    "I made the text bold, so I know how to undo bold."

Memento:
    "Before the change, the text was 'Hello', so restore 'Hello'."


WHEN TO USE:

Command with Undo:
- Useful when individual operations have clear reverse operations.
- Each command can contain the information required to undo itself.

Memento:
- Useful when restoring an object's previous state is easier than
  reversing individual operations.
"""

# =========================================================
# COMMAND INTERFACE
# Every command must be executable.
# =========================================================


from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# =========================================================
# UNDOABLE COMMAND INTERFACE
# An undoable command can both execute AND undo itself.
# =========================================================
class UndoableCommand(Command):

    @abstractmethod
    def unexecute(self):
        pass


# =========================================================
# DOCUMENT (RECEIVER)
# The actual object being modified by commands.
# =========================================================
class Document:

    def __init__(self):
        self.content = ""

    def make_bold(self):
        self.content = f"<b>{self.content}</b>"


# =========================================================
# HISTORY
# Keeps track of commands that can later be undone.
# =========================================================
class History:

    def __init__(self):
        self.__commands = []

    def push(self, command: UndoableCommand):
        self.__commands.append(command)

    def pop(self):
        return self.__commands.pop()


# =========================================================
# CONCRETE UNDOABLE COMMAND
# Stores the previous state before modifying the document.
# =========================================================
class BoldCommand(UndoableCommand):

    def __init__(self, document: Document, history: History):
        self.__document = document
        self.__history = history
        self.__prev_content = None

    def execute(self):
        # Save the old state before changing it
        self.__prev_content = self.__document.content

        # Perform the operation
        self.__document.make_bold()

        # Remember this command so we can undo it later
        self.__history.push(self)

    def unexecute(self):
        # Restore the previous state
        self.__document.content = self.__prev_content


# =========================================================
# UNDO COMMAND
# Takes the most recent command and reverses it.
# =========================================================
class UndoCommand(Command):

    def __init__(self, history: History):
        self.__history = history

    def execute(self):
        last = self.__history.pop()
        last.unexecute()


# =========================================================
# CLIENT
# =========================================================

if __name__ == "__main__":

    document = Document()
    document.content = "Hello World"

    history = History()

    bold_command = BoldCommand(document, history)

    # Execute Bold
    bold_command.execute()

    print(document.content)
    # <b>Hello World</b>

    # Undo Bold
    undo_command = UndoCommand(history)
    undo_command.execute()

    print(document.content)
    # Hello World
