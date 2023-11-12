import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class NoteWidget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}
        self.read_notes()
        self.connects()

    def connects(self):
        self.ui.list_note.itemClicked.connect(self.show_notes)



    def read_notes(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {"Ласкаво просимо в розумні звмітки!": {
                "текст":"Додайте свою першу замітку", "теги":[]            
                }
            }
        self.ui.list_note.addItems(self.notes)
    
    def show_notes(self):
        name = self.ui.list_note.selectedItems()[0].text()
        self.ui.lineEdit.setText(name)
        self.ui.textEdit.setText(self.notes[name]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[name]["теги"])


app = QApplication([])
ex = NoteWidget()
ex.show()
app.exec_()
