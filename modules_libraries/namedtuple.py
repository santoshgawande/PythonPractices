#tuple
rect = (1,2)
print(rect[0])
#namedtuple is immutable
from collections import namedtuple
Rectangle = namedtuple("Rectangle","height width")
rectangle = Rectangle(3,5)
print(rectangle.height)