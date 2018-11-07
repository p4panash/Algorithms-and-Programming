from functions import ShowList, AddScore, AddScoreAtIndex, RemoveScoreAtIndex, RemoveScoresFrom, ReplaceScoreIndex
from functions import GetParticipantsLess, GetSortedParticipants, GetSortedParticipantsGreater
from functions import GetAverageScoreFrom, GetSmallestScoreFrom, GetMultiplesFrom
from functions import FilterByMultiple, FilterByGreaterValue
from functions import Undo, SaveChanges, ChangePositions


def TestShowList():
    assert ShowList([1, 2, 3, 4, 5]) == "1 2 3 4 5 "
    assert ShowList([]) == ""


def TestAddScore():
    assert AddScore([1, 2, 3, 4], 5) == [1, 2, 3, 4, 5]
    assert AddScore([], 0) == [0]


def TestAddScoreAtIndex():
    assert AddScoreAtIndex([1, 2, 3, 4], 30, 0) == [30, 1, 2 ,3 ,4]
    assert AddScoreAtIndex([1, 2, 3, 4], 30, 2) == [1, 2, 30, 3, 4]
    assert AddScoreAtIndex([1, 2, 3, 4], 40, 3) == [1, 2 , 3, 40, 4]
    assert AddScoreAtIndex([1, 2, 3, 4], 40, 4) == [1, 2, 3 ,4, 40]
    assert AddScoreAtIndex([], 30, 0) == [30]
    assert AddScoreAtIndex([], 30, 1) == [30]


def TestRemoveScoreAtIndex():
    assert RemoveScoreAtIndex([1, 2, 3, 4], 1) == [2, 3, 4]
    assert RemoveScoreAtIndex([1, 2, 3, 4], 3) == [1, 2, 4]
    assert RemoveScoreAtIndex([1, 2, 3, 4], 4) == [1, 2, 3]
    assert RemoveScoreAtIndex([1, 2, 3, 4], 5) == [1, 2, 3, 4]
    assert RemoveScoreAtIndex([], 1) == []
    assert RemoveScoreAtIndex([1], 1) == []


def TestRemoveScoresFrom():
    assert RemoveScoresFrom([1, 2, 3, 4], 0, 1) == [3, 4]
    assert RemoveScoresFrom([1, 2, 3, 4], 0, 3) == []
    assert RemoveScoresFrom([1, 2, 3, 4], 1, 3) == [1]
    assert RemoveScoresFrom([1, 2, 3, 4], 2, 3) == [1, 2]


def TestReplaceScoreIndex():
    assert ReplaceScoreIndex([1, 2, 3, 4], 0, 30) == [30, 2, 3, 4]
    assert ReplaceScoreIndex([1, 2, 3, 4], 3, 30) == [1, 2, 3, 30]
    assert ReplaceScoreIndex([1, 2, 3, 4], 1, 30) == [1, 30, 3, 4]
    assert ReplaceScoreIndex([1], 0, 40) == [40]
    assert ReplaceScoreIndex([], 0, 30) == []


def TestGetParticipantsLess():
    assert GetParticipantsLess([20, 23, 44, 99, 1, 412, 34], 50) == [20, 23, 44, 1, 34]
    assert GetParticipantsLess([20, 23, 44, 99, 1, 412, 34], 10) == [1]
    assert GetParticipantsLess([20, 23, 44, 99, 100, 412, 34], 10) == []
    assert GetParticipantsLess([], 50) == []


def TestGetSortedParticipants():
    assert GetSortedParticipants([20, 23, 44, 99, 1, 412, 34]) == [1, 20, 23, 34, 44, 99, 412]
    assert GetSortedParticipants([20, 23, -19, 99, 10, 34]) == [-19, 10, 20, 23, 34, 99]
    assert GetSortedParticipants([20, 20, 44, 44, 100, 412, 34]) == [20, 20, 34, 44, 44, 100, 412]
    assert GetSortedParticipants([]) == []


def TestGetSortedParticipantsGreater():
    assert GetSortedParticipantsGreater([20, 23, 44, 99, 1, 412, 34], 30) == [34, 44, 99, 412]
    assert GetSortedParticipantsGreater([20, 23, -19, 99, 10, 34], 0) == [10, 20, 23, 34, 99]
    assert GetSortedParticipantsGreater([20, 20, 44, 44, 100, 412, 34], 20) == [34, 44, 44, 100, 412]
    assert GetSortedParticipantsGreater([20, 23, -19, 99, 10, 34], 100) == []
    assert GetSortedParticipantsGreater([], 100) == []


def TestGetAverageScoreFrom():
    assert GetAverageScoreFrom([20, 23, 44, 99, 1, 412, 34], 0, 2) == 29.0
    assert GetAverageScoreFrom([20, 23, -19, 99, 10, 34], 1, 4) == 28.25
    assert GetAverageScoreFrom([20, 20, 44, 44, 100, 412, 34], 0, 0) == 20.0
    assert GetAverageScoreFrom([20, 23, -19, 99, 10, 34], 2, 6) == "Doesn't exist !"
    assert GetAverageScoreFrom([], 0, 6) == "Doesn't exist !"


def TestGetSmallestScoreFrom():
    assert GetSmallestScoreFrom([20, 23, 44, 99, 1, 412, 34], 0, 19) == "Doesn't exist !"
    assert GetSmallestScoreFrom([20, 23, -19, 99, 10, 34], 0, 5) == -19
    assert GetSmallestScoreFrom([20, 20, 44, 44, 100, 412, 34], 0, 1) == 20
    assert GetSmallestScoreFrom([0, 0, 0, 0, 0, 34], 0, 3) == 0
    assert GetSmallestScoreFrom([], 1, 5) == "Doesn't exist !"


def TestGetMultiplesFrom():
    assert GetMultiplesFrom([20, 23, 44, 99, 1, 412, 34], 0, 1, 4) == [20]
    assert GetMultiplesFrom([20, 23, -19, 99, 10, 34], 3, 4, 5) == [10]
    assert GetMultiplesFrom([20, 20, 44, 44, 100, 412, 34], 0, 5, 1) == [20, 20, 44, 44, 100, 412]
    assert GetMultiplesFrom([20, 23, -19, 99, 10, 34], 0, 5, 7) == []
    assert GetMultiplesFrom([], 1, 6, 8) == []


def TestFilterByMultiple():
    assert FilterByMultiple([20, 23, 44, 99, 1, 412, 34]) == [20]
    assert FilterByMultiple([20, 23, -19, 99, 10, 34]) == [20, 10]
    assert FilterByMultiple([20, 20, 44, 44, 100, 412, 34]) == [20, 20, 100]
    assert FilterByMultiple([19, 23, -19, 99, 21, 34]) == []
    assert FilterByMultiple([]) == []


def TestFilterByGreaterValue():
    assert FilterByGreaterValue([20, 23, 44, 99, 1, 412, 34], 0) == [20, 23, 44, 99, 1, 412, 34]
    assert FilterByGreaterValue([20, 23, -19, 99, 10, 34], 10) == [20, 23, 99, 34]
    assert FilterByGreaterValue([20, 20, 44, 44, 100, 41, 34], 44) == [100]
    assert FilterByGreaterValue([20, 23, -19, 99, 10, 34], 100) == []
    assert FilterByGreaterValue([], 1) == []


def TestSaveChanges():
    changes = []
    assert SaveChanges([1, 2, 3], changes) == [[1, 2, 3]]
    assert SaveChanges([20, 23, -19, 99, 10, 34], changes) == [[1, 2, 3], [20, 23, -19, 99, 10, 34]]
    assert SaveChanges([222], changes) == [[1, 2, 3], [20, 23, -19, 99, 10, 34], [222]]
    assert SaveChanges([], changes) == [[1, 2, 3], [20, 23, -19, 99, 10, 34], [222], []]
    assert SaveChanges([10, 20, 30], changes) == [[1, 2, 3], [20, 23, -19, 99, 10, 34], [222], [], [10, 20, 30]]


def TestUndo():
    array = [1, 2, 3, 4, 5, 6]
    changes = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    array = Undo(array, changes)
    assert array == [1, 2, 3, 4, 5]
    array = Undo(array, changes)
    assert array == [1, 2, 3, 4]
    array = Undo(array, changes)
    assert array == [1, 2, 3]
    array = Undo(array, changes)
    assert array == [1, 2]
    array = Undo(array, changes)
    assert array == [1]
    array = Undo(array, changes)
    assert array == [1]


def TestChangePositions():
    assert ChangePositions(1, 2) == [1, 2]
    assert ChangePositions(1, -2) == [-2, 1]
    assert ChangePositions(10, 10) == [10, 10]


def AllTests():
    TestShowList()
    TestAddScore()
    TestAddScoreAtIndex()
    TestRemoveScoresFrom()
    TestReplaceScoreIndex()
    TestGetParticipantsLess()
    TestGetSortedParticipants()
    TestGetSortedParticipantsGreater()
    TestGetAverageScoreFrom()
    TestGetSmallestScoreFrom()
    TestGetMultiplesFrom()
    TestFilterByMultiple()
    TestFilterByGreaterValue()
    TestSaveChanges()
    TestUndo()
    TestChangePositions()


AllTests()