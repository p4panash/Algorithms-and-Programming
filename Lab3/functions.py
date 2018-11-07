def ShowList(array):
    """
    This function is used in order to print the elements from an array
    Input: array - an array of numbers representing the participants scores
    Output: text - a string which contains the elements from array
    """
    text = ""
    if type(array) is list:
        for score in array:
            text += str(score) + " "
    else:
        return array
    print(text)
    return text


def AddScore(array, score):
    """
    This function is used in order to add the score for the last participant
    Input: array - an array of numbers representing the participants scores
           score - an integer representing the participant score
    Output: array - an array with the scores of participants including the score from input
    """
    array.append(score)
    return array


def AddScoreAtIndex(array, score, index):
    """
    This function is used in order to add the score for the last participant
    Input: array - an array of numbers representing the participants scores
           score - an integer representing the participant score
    Output: array - an array with the scores of participants including the score from input
    """
    array.insert(index, score)
    return array


def RemoveScoreAtIndex(array, index):
    """
    This function is used in order to delete a score at a given index
    Input: array - an array of numbers representing the participants scores
           index - an integer representing the participant position
    Output: array - an array with the scores of participants excluding the score from position given from input
    """
    if index <= len(array) - 1:
        del array[index]
    return array


def RemoveScoresFrom(array, start, end):
    """
    This function is used in order to remove multiple scores from the array
    Input: array - an array of numbers representing the participants scores
           start - an integer representing the start position for delete
           end - an integer represent the position of the last participant to be delete
    Output: array - an array with the scores of participants excluding the participants between the given interval
    """
    if start >= 0 and end <= len(array) - 1:
        positions = ChangePositions(start, end)
        del array[positions[0]:positions[1] + 1]
    return array


def ReplaceScoreIndex(array, index, newScore):
    """
    This function is used in order to replace a participant score
    Input: array - an array of numbers representing the participants scores
           index - an integer representing the position of the participant
           newScore - an integer representing the new score of the participant
    Output: array - an array with the scores of participants including the updated score
    """
    if index >= 0 and index <= len(array) - 1:
        array[index] = newScore
    return array


def GetParticipantsLess(array, givenScore):
    """
    This function is used in order to print all the participant with scores less than a given value
    Input: array - an array of numbers representing the participants scores
           givenScore - an integer representing the score used in searching values smaller than
    Output: result - an array with the scores of participants including the updated score
    """
    result = []
    for score in array:
        if score < givenScore:
            result.append(score)
    return result


def GetSortedParticipants(array):
    """
    This function is used in order to print the participants scores sorted
    Input: array - an array of numbers representing the participants scores
    Output: result - an array with the scores of participants sorted
    """
    result = array[:]
    result.sort()
    return result


def GetSortedParticipantsGreater(array, givenScore):
    """
    This function is used in order to print the participants ,with scores higher than a given value, sorted
    Input: array - an array of numbers representing the participants scores
           givenScore - an integer representing the value used in sorting participants scores
    Output: array - an array with the sorted scores of participants, greater than a given value
    """
    result = []
    tempList = array[:]
    tempList.sort()
    for score in tempList:
        if score > givenScore:
            result.append(score)
    return result


def GetAverageScoreFrom(array, startPosition, endPosition):
    """
    This function is used in order to print the average score between the participants
    Input: array - an array of numbers representing the participants scores
           startPosition - an integer representing the position where to start calculating the average score
           endPosition - an integer representing the position where to stop calculating the average score
    Output: an float value representing the average score between the given interval, in case the data is wrong the function will return the message Doesn't exist
    """
    if startPosition >= 0 and endPosition <= len(array) - 1:
        positions = ChangePositions(startPosition, endPosition)
        return sum(array[positions[0]:positions[1] + 1]) / len(array[positions[0]:positions[1] + 1])
    return "Doesn't exist !"


def GetSmallestScoreFrom(array, startPosition, endPosition):
    """
    This function is used in order to print the participants scores sorted higher than a given value
    Input: array - an array of numbers representing the participants scores
           startPosition - an integer representing the position where to start calculating the average score
           endPosition - an integer representing the position where to stop calculating the average score
    Output: an float value representing the average score between the given interval, in case the data is wrong the function will return the message Doesn't exist
    """
    if startPosition >= 0 and endPosition <= len(array) - 1:
        positions = ChangePositions(startPosition, endPosition)
        return min(array[positions[0]:positions[1] + 1])
    return "Doesn't exist !"


def GetMultiplesFrom(array, startPosition, endPosition, number):
    """
    This function is used in order to print the participants scores sorted higher than a given value
    Input: array - an array of numbers representing the participants scores
        startPosition - an integer representing the position where to start calculating the average score
        endPosition - an integer representing the position where to stop calculating the average score
        number - an integer representing the number used in order to form the result
    Output: an float value representing the average score between the given interval, in case the data is wrong the function will return the message Doesn't exist
    """
    multiple = []
    if startPosition >= 0 and endPosition <= len(array) - 1:
        for score in array[startPosition:endPosition + 1]:
            if score % number == 0:
                multiple.append(score)
    return multiple


def FilterByMultiple(array):
    """
    This function is used in order to filter the array by keeping only the participants with scores that are multiple of 10
    Input: array - an array of numbers representing the participants scores
    Output: an array only with participants score that are multiple of 10
    """
    result = []
    for score in array:
        if score % 10 == 0:
            result.append(score)
    return result


def FilterByGreaterValue(array, value):
    """
    This function is used in order to filter the array by keeping only the scores higher than a given value
    Input: array - an array of numbers representing the participants scores
           value - an integer representing the number used in order to filter the list
    Output: an array only with participants score higher than a given value
    """
    result = []
    for score in array:
        if score > value:
            result.append(score)
    return result


def Undo(array, changes):
    """
    This function is used in order to restore the content of the array
    Input: array - an array of numbers representing the participants scores
           changes - an array of arrays representing the changes made over time
    Output: an array representing the array before the last change if there is one, otherwise it will return the array from input
    """
    if len(changes) > 0:
        lastChange = changes[len(changes) - 1][:]
        del changes[len(changes) - 1]
        return lastChange
    return array

def SaveChanges(array, changes):
    """
    This function is used to save the array in the changes array before performing an action that will alter it
    Input: array - an array of numbers representing the participants scores
           changes - an array of arrays representing the changes made over time
    Output: the updated array of changes
    """
    result = changes
    result.append(array[:])
    return result

def ChangePositions(startPosition, endPosition):
    """
    This function is used to interchange two values if the first is greater than the second
    Input: startPosition - an integer representing an index of an array, it should be less than endPosition
           endPosition - an integer representing an index of an array
    Output: a sorted array with two elements
    """
    if startPosition > endPosition:
        return [endPosition, startPosition]
    return [startPosition, endPosition]