def ReadFromFile(currentArray, fileName):
    """
    Function used in order to change the current list with a list from a file
    Input: currentArray - an array of integers representing the current array
    Output: an array with elements from file
    """
    array = []
    try:
        file = open(fileName, "r")
        numberOfElements = int(file.readline())
        arrayOfElements = [element for element in file.read().split(", ")]
        for index in range(numberOfElements + 1):
            if index > len(arrayOfElements) - 1:
                break
            try:
                element = int(arrayOfElements[index])
                array.append(element)
            except ValueError:
                pass
    except ValueError:
        print(" Invalid input ! Please check the input file !")
    except IOError:
        print(" File can not be found !")
        return currentArray
    return array


def WriteInFile(currentArray, fileName):
    """
    Function used in order to write the content of the current list in a file
    Input: currentArray - an array of integers representing the current array
    """
    try:
        file = open(fileName, "w")
        text = ""
        for element in currentArray:
            text += str(element) + ", "
        file.write(text)
    except IOError:
        print("IO Error")