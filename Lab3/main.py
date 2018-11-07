#Lab 3-5

#Lab 3
from functions import ShowList, AddScore, AddScoreAtIndex, RemoveScoreAtIndex, RemoveScoresFrom, ReplaceScoreIndex
#Homework Lab 3
from functions import GetParticipantsLess, GetSortedParticipants, GetSortedParticipantsGreater
#Lab 4
from functions import GetAverageScoreFrom, GetSmallestScoreFrom, GetMultiplesFrom
#Homework Lab 4
from functions import FilterByMultiple, FilterByGreaterValue, Undo, SaveChanges
#Lab 6
from ReadFile import ReadFromFile, WriteInFile

def UI(array, changes):
    """
    Function that handles menu and menu actions
    Input: array - an array with the participants score
           changes - an array of arrays where the changes made on the principal array are stored
    """
    try :
        option = int(input(" 1. Add result of a new participant \n 2. Modify scores \n 3. Print participants \n 4. Obtain different characteristics of participants \n 5. Filter scores \n 6. Undo \n 7. Read from file \n 8. Write in file \n 9. Show results \n 0. Exit \n"))
        while option != 0:
            while (option < 0 or option > 8) and option != 9:
                option = int(input(" Wrong option ! \n 1. Add result of a new participant \n 2. Modify scores \n 3. Print participants \n 4. Obtain different characteristics of participants \n 5. Filter scores \n 6. Undo \n 7. Read from file \n 8. Write in file \n 9. Show results \n 0. Exit \n"))
            if option == 1:
                secondOption = int(input(" 1. Add score of last participant \n 2. Add score of a certain participant \n"))
                while secondOption < 1 or secondOption > 2:
                    secondOption = int(input(" Wrong option ! \n 1. Add score of last participant \n 2. Add score of a certain participant \n"))
                if secondOption == 1:
                    score = int(input(" Introduce the score: "))
                    changes = SaveChanges(array, changes)
                    array = AddScore(array, score)
                elif secondOption == 2:
                    index = int(input(" Introduce the participant number: "))
                    score = int(input(" Introduce the score: "))
                    changes = SaveChanges(array, changes)
                    array = AddScoreAtIndex(array, score, index - 1)
            if option == 2:
                secondOption = int(input(" 1. Remove score \n 2. Remove multiple scores \n 3. Replace scores \n"))
                while secondOption < 1 or secondOption > 3:
                    secondOption = int(input(" Wrong option ! \n 1. Remove score \n 2. Remove multiple scores \n 3. Replace scores \n"))
                if secondOption == 1:
                    index = int(input(" Introduce the participant number: "))
                    changes = SaveChanges(array, changes)
                    array = RemoveScoreAtIndex(array, index - 1)
                elif secondOption == 2:
                    start = int(input(" Introduce the number of the first participant you want to delete: "))
                    end = int(input(" Introduce the number of the last participant you want to delete: "))
                    changes = SaveChanges(array, changes)
                    array = RemoveScoresFrom(array, start - 1, end - 1)
                elif secondOption == 3:
                    index = int(input(" Introduce the number of the participant: "))
                    newScore = int(input(" Introduce the new score: "))
                    changes = SaveChanges(array, changes)
                    array = ReplaceScoreIndex(array, index - 1, newScore)
            if option == 3:
                secondOption = int(input(" 1. Print participants with score less than your input \n 2. Print participants sorted by their score \n 3. Print participants sorted by their score with score greater than your input \n"))
                while secondOption < 1 or secondOption > 3:
                    secondOption = int(input(" Wrong option ! \n 1. Print participants with score less than your input \n 2. Print participants sorted by their score \n 3. Print participants sorted by their score with score greater than your input \n"))
                if secondOption == 1:
                    score = int(input(" Introduce a score: "))
                    ShowList(GetParticipantsLess(array, score))
                elif secondOption == 2:
                    ShowList(GetSortedParticipants(array))
                elif secondOption == 3:
                    score = int(input(" Introduce a score: "))
                    ShowList(GetSortedParticipantsGreater(array, score))
            if option == 4:
                secondOption = int(input(" 1. Print average score between certain participants \n 2. Print the smallest score for certain participants \n 3. Print scores for certain participants which are multiple of a given number \n"))
                while secondOption < 1 or secondOption > 3:
                    secondOption = int(input(" Wrong option ! \n 1. Print average score between certain participants \n 2. Print the smallest score for certain participants \n 3. Print scores for certain participants which are multiple of a given number \n"))
                if secondOption == 1:
                    startPosition = int(input(" Introduce first participant: "))
                    endPosition = int(input(" Introduce last participant: "))
                    print(str(GetAverageScoreFrom(array, startPosition - 1, endPosition - 1)))
                elif secondOption == 2:
                    startPosition = int(input(" Introduce first participant: "))
                    endPosition = int(input(" Introduce last participant: "))
                    print(str(GetSmallestScoreFrom(array, startPosition - 1, endPosition - 1)))
                elif secondOption == 3:
                    multiple = int(input(" Introduce a number: "))
                    startPosition = int(input(" Introduce first participant: "))
                    endPosition = int(input(" Introduce last participant: "))
                    ShowList(GetMultiplesFrom(array, startPosition - 1, endPosition - 1, multiple))
            if option == 5:
                secondOption = int(input(" 1. Keep only participants with scores multiple of 10 \n 2. Keep only participants with scores higher than a given value \n"))
                while secondOption < 1 or secondOption > 2:
                    secondOption = int(input(" Wrong option ! \n 1. Keep only participants with scores multiple of 10 \n 2. Keep only participants with scores higher than a given value \n"))
                if secondOption == 1:
                    changes = SaveChanges(array, changes)
                    array = FilterByMultiple(array)
                if secondOption == 2:
                    value = int(input(" Introduce value :"))
                    changes = SaveChanges(array, changes)
                    array = FilterByGreaterValue(array, value)
            if option == 6:
                array = Undo(array, changes)
            if option == 7:
                inputName = input(" Introduce file name: ")
                array = ReadFromFile(array, inputName)
            if option == 8:
                outputName = input(" Introduce file name: ")
                WriteInFile(array, outputName)
            if option == 9:
                ShowList(array)
            option = int(input(" 1. Add result of a new participant \n 2. Modify scores \n 3. Print participants \n 4. Obtain different characteristics of participants \n 5. Filter scores \n 6. Undo \n 7. Read from file \n 8. Write in file \n 9. Show results \n 0. Exit \n"))
    except ValueError:
        print(" Invalid input ! Try again !")
        UI(array, changes)


def main() :
    """
    The main function, this is where the participants score and list of changes are stored. Also this calls the UI function
    Input: none
    Output: none
    """
    array = [88, 21, 32, 90]
    changes = []
    UI(array, changes)

main()