from Infastructure.PlantRepository import PlantRepository
from UI.UI import UI
from Domain.Plant import Plant

repo = PlantRepository()
repo.add_plant(Plant("abc", 1, 2))
repo.add_plant(Plant("bcd", 10, 0))
repo.add_plant(Plant("basda", 20, 30))
repo.add_plant(Plant("ddd", 10, 15))
repo.add_plant(Plant("abcdef", 3, 0))
ui = UI(repo)

ui.run()