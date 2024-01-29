"""this module is for rectangle class
    """


class Rectangle:
    """rectangle class to calculate size
    """

    number_of_instances = 0
    print_symbol = "#"

    def _init_(self, width=0, height=0):
        """initiation
        Args:
            width: int >0
            height: int > 0
        """
        if not isinstance(width, (int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, (int)):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return rectangle area
        """
        return self._height * self._width

    def perimeter(self):
        """returns rectangle perimeter
        """
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width + self._height) * 2

    def _str_(self):
        """represent the object in string when called

        Returns:
            area with str stored in print_symbol
        """
        prn = ""
        if self._height == 0 or self._width == 0:
            return prn
        for i in range(self.__height):
            prn += str(self.print_symbol) * self.__width + "\n"
        return prn[:-1]

    def _repr_(self):
        """represent the object in string when called

        Returns:
            area with #
        """
        return f"Rectangle{self._width, self._height}"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def _del_(self):
        """deleting message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
