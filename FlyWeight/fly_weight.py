

from enum import Enum, auto
from enum import Enum


class PointType(Enum):
    HOSPITAL = auto()
    CAFE = auto()
    RESTAURANT = auto()


class Point:

    def __init__(self, x: int, y: int, point_type: PointType, icon: list):
        self.__x = x  # 4byts
        self.__y = y  # 4bytes
        self.__point_type: PointType = point_type  # bytes
        self.__icon: list = icon  # 20kb

    def draw(self):
        print(f"{self.__point_type.name} at ({self.__x}, {self.__y})")


class PointService:
    def get_points(self) -> list[Point]:
        points: list[Point] = list()
        point = Point(1, 2, PointType.CAFE, None)
        points.append(point)

        return points


if __name__ == "__main__":
    service = PointService()
    for point in service.get_points():
        point.draw()
