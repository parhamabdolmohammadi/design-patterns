# MEMENTO PATTERN
#
# Purpose:
# The Memento Pattern allows us to save a snapshot of an object's state
# and restore that state later without exposing the object's internal
# implementation.
#
# A common use case is UNDO functionality.
#
# The pattern has 3 main components:
#
# 1. Originator -> Editor
#    The object whose state we want to save and restore.
#
# 2. Memento -> EditorState
#    A snapshot containing the saved state of the Originator.
#
# 3. Caretaker -> History
#    Stores the Mementos (snapshots) and gives them back when needed.
#
# Flow:
# Editor -> creates EditorState -> History stores it
# Editor <- restores EditorState <- History returns it


# ORIGINATOR
# This is the object whose state changes and needs to support undo.
class Editor:
    def __init__(self):
        self.content = ""

    # Creates a snapshot (Memento) of the Editor's CURRENT state.
    #
    # Instead of History knowing about editor.content,
    # the Editor itself decides what information should be saved.
    def create_state(self):
        return EditorState(self.content)

    # Restores the Editor to a previously saved state.
    def restore(self, state: EditorState):
        self.content = state.get_content()


# MEMENTO
# Represents a snapshot of the Editor at a particular point in time.
#
# Its job is simply to store the state.
class EditorState:
    def __init__(self, content):
        # The saved state is private so outside classes
        # cannot directly modify the snapshot.
        self.__content = content

    def get_content(self):
        return self.__content


# CARETAKER
# Responsible for keeping track of previous states.
#
# History does NOT need to know what is inside EditorState.
# It simply stores and returns snapshots.
class History:
    def __init__(self):
        self.__states = []

    # Save a new snapshot.
    def push(self, state: EditorState):
        self.__states.append(state)

    # Return the most recently saved snapshot.
    # This gives us Undo behavior (LIFO).
    def pop(self):
        return self.__states.pop()


if __name__ == "__main__":
    editor = Editor()
    history = History()

    # -------------------------------
    # STATE 1
    # -------------------------------

    editor.content = "Hello"

    # Create a snapshot containing "Hello"
    # and store it in History.
    history.push(editor.create_state())

    # History:
    # ["Hello"]

    # -------------------------------
    # STATE 2
    # -------------------------------

    editor.content = "Hello World"

    # Save another snapshot.
    history.push(editor.create_state())

    # History:
    # ["Hello", "Hello World"]

    # -------------------------------
    # STATE 3
    # -------------------------------

    editor.content = "Hello World!!!"

    # We don't save this state because we want
    # the previous state to be our Undo destination.

    print(editor.content)
    # Hello World!!!

    # -------------------------------
    # UNDO
    # -------------------------------

    # pop() returns the most recently saved EditorState:
    # "Hello World"
    #
    # restore() tells Editor to restore itself using that snapshot.
    editor.restore(history.pop())

    print(editor.content)
    # Hello World

    # -------------------------------
    # UNDO AGAIN
    # -------------------------------

    # The next snapshot in History contains "Hello".
    editor.restore(history.pop())

    print(editor.content)
    # Hello
