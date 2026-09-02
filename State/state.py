from abc import ABC, abstractmethod
from enum import Enum

# Open closed principle: its open for extention closed for mutaion


class Tool(ABC):
    @abstractmethod
    def mouseDown(self):
        pass

    @abstractmethod
    def mouseUp(self):
        pass


class Canvas:

    def __init__(self):
        self.__current_tool: Tool = None

    def mouse_down(self):
        self.__current_tool.mouseDown()

    def mouse_up(self):
        self.__current_tool.mouseUp()

    def set_current_tool(self, current_tool: Tool):
        if not isinstance(current_tool, Tool):
            raise TypeError("Current toll should be off type Tool")

        self.__current_tool = current_tool

    def get_current_tool(self) -> Tool:
        return self.__current_tool


class SelectionTool(Tool):
    def mouseDown(self):
        print("Selection icon")

    def mouseUp(self):
        print("Draw a Dashed Rectangle")


class BrushTool(Tool):
    def mouseDown(self):
        print("Brush icon")

    def mouseUp(self):
        print("Draw a line")


class EraserTool(Tool):
    def mouseDown(self):
        print("Eraser icon")

    def mouseUp(self):
        print("Erase something")


# BAD PRACTICE TOO MUCH IF ELSE

# class Canvas:

#     def __init__(self):
#         self.__current_tool = None

#     def mouse_down(self):
#         if self.__current_tool == ToolType.SELECTION:
#             print("Selection Icon")

#         elif self.__current_tool == ToolType.BRUSH:
#             print("Brush Icon")

#         elif self.__current_tool == ToolType.ERASER:
#             print("Eraser Icon")

#     def mouse_up(self):
#         if self.__current_tool == ToolType.SELECTION:
#             print("Draw Dashed Rectangle")

#         elif self.__current_tool == ToolType.BRUSH:
#             print("Draw a line")

#         elif self.__current_tool == ToolType.ERASER:
#             print("Erase Something")

#     def set_current_tool(self, current_tool):
#         self.__current_tool = current_tool

#     def get_current_tool(self):
#         return self.__current_tool


# class ToolType(Enum):
#     SELECTION = 'selection'
#     BRUSH = 'brush'
#     ERASER = 'eraser'
