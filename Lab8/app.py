from Domain.MyVector import MyVector
from Infrastructure.VectorRepository import VectorRepository
from Application.VectorController import VectorController
from UI.UI import UI

def start():
    repo = VectorRepository()
    repo.addVector(MyVector("abc", "r", 1, [1, 2, 3, 4]))
    repo.addVector(MyVector("aaa", "g", 3, [2, 2, 3, 4, 7, 8]))
    repo.addVector(MyVector("test", "b", 3, [4, 5]))
    repo.addVector(MyVector("1", 'r', 2, [10, 3, 9]))
    repo.addVector(MyVector("2", 'y', 4, [1, 3, 6, 9]))

    controller = VectorController(repo)

    ui = UI(controller)
    ui.run()

start()