import math

def IsPerfectSquare(number):
    if number < 0 :
        return False
    if math.sqrt(number) * math.sqrt(number) == number:
        return True
    return False

def DeletePerfectSquares(array):
    index = 0
    while index < len(array):
        if IsPerfectSquare(array[index]) == True:
            del array[index]
        else:
            index += 1
    return array

def ReadArray(array):
    for element in input("Introduce the array elements: ").split():
        array.append(int(element))
    return array

def PrintArray(array):
    text = ""
    for element in array:
        text += str(element) + " "
    return text

def TestDeletePerfectSquares():
    assert DeletePerfectSquares([]) == []
    assert DeletePerfectSquares([1, 2, 3, 5]) == [1, 2, 3, 5]
    assert DeletePerfectSquares([100, 49, 4]) == []
    assert DeletePerfectSquares([100, 1, 3]) == [1, 3]
    assert DeletePerfectSquares([1, 3, 100]) == [1, 3]
    assert DeletePerfectSquares([1, 100, 3]) == [1, 3]

def TestIsPerfectSquare():
    assert IsPerfectSquare(17) == False
    assert IsPerfectSquare(-10) == False
    assert IsPerfectSquare(-100) == False
    assert IsPerfectSquare(100) == True
    assert IsPerfectSquare(49) == True


def Testing():
    TestIsPerfectSquare()
    TestIsPerfectSquare()

def main():
    Testing()
    array = []
    ReadArray(array)
    DeletePerfectSquares(array)
    print("The resulted array is : " + PrintArray(array))

main()