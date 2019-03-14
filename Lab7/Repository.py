class PointRepository:
    def __init__(self):
        self._points = []


    def AddPoint(self, point):
        self._points.append(point)


    def GetAllPoints(self):
        return self._points


    def GetPointAtIndex(self, index):
        if index > 0 and index <= len(self._points) - 1:
            return self._points[index]
        raise ValueError("Invalid index !")


    def GetAllPointsInsideRectangle(self, upLeftCorner, length, width):
        result = []
        for el in self._points:
            if el.CheckIfIsInside(upLeftCorner, length, width):
                result.append(el)
        return result


    def UpdateColour(self, coord_x, coord_y, colour):
        for el in self._points:
            if el.GetCoord_x == coord_x and el.GetCoord_y == coord_y:
                el.SetColour(colour)


    def DeletePointByCoord(self, coord_x, coord_y):
        for index in range(0, len(self._points)):
            if self._points[index].GetCoord_x() == coord_x and self._points[index].GetCoord_y() == coord_y:
                del self._points[index]