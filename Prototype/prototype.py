

from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def render(self):
        pass


class Circle(Component):

    def render(self):
        print("Rendering A circle")

    def set_radius(self, r: int):
        self.__radius = r

    def get_radius(self):
        return self.__radius


class ContextMenu:

    def duplicate(self, component: Component):

        if isinstance(component, Circle):
            source = component

            target = Circle()
            target.set_radius(source.get_radius())

            return target
