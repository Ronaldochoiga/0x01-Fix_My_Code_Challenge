#!/usr/bin/python3
""" Module for the square class """

class square():
    """ square class indicated """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ this is the instantiation of the class module """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def Permiter_of_my_square(self):
        """ this functions calculates the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ This is the printed rep """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ creation of a square object """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_of_my_square())
