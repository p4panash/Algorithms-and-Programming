class MyPoint:
    def __init__(self, coord_x, coord_y, colour):
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._colour = colour


    def GetCoord_x(self):
        return self._coord_x


    def GetCoord_y(self):
        return self._coord_y


    def GetColour(self):
        return self._colour


    def SetCoord_x(self, coord_x):
        self._coord_x = coord_x


    def SetCoord_y(self, coord_y):
        self._coord_y = coord_y


    def SetColour(self, colour):
        self._colour = colour


    def __str__(self):
        return "Point (" + str(self._coord_x) + " " + str(self._coord_y) + " ) of colour " + self._colour + "."


    def CheckIfIsInside(self, upLeftCorner, lenght, width):
        if ((self._coord_x >= upLeftCorner.GetCoord_x() and self._coord_x() <= upLeftCorner.GetCoord_x() + lenght)
            and (self._getcoord_y() <= upLeftCorner.GetCoord_y() and self._coord_y() >= upLeftCorner.GetCoord_y() - width)):
            return True
        return False
