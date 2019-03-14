from Domain.Contact import Contact
from Infrastructure.ContactRepository import ContactRepository
from Application.ContactController import ContactController
from UI.UI import UI

def run():
    repo = ContactRepository()
    repo.addContact(Contact("Popescu", "+40-711-111999", "work"))
    repo.addContact(Contact("Mom", "+40-733-333444", "personal"))
    repo.addContact(Contact("Dana", "+40-744-444999", "personal"))
    controller = ContactController(repo)
    ui = UI(controller)

    ui.run()

run()