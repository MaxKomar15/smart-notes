import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog
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
        self.ui.create_btn.clicked.connect(self.add_note)
        self.ui.save_btn4.clicked.connect(self.save_note)
        self.ui.delete_btn5.clicked.connect(self.del_note)
        self.ui.add_tag.clicked.connect(self.add_tag)
        self.ui.open_btn3.clicked.connect(self.del_tag)



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

    def add_note(self):
        self.ui.lineEdit.clear()
        self.ui.textEdit.clear()
        self.ui.listWidget_2.clear()

    def save_file(self):
        try:
            with open("notes.json", "w", encoding="utf8") as files:
                json.dump(self.notes, files, ensure_ascii=False)
        except:
            message = QMessageBox()
            message.setText("Не вдалося зберегти!")
            message.show()
            message.exec_()

    def save_note(self):
        title = self.ui.lineEdit.text()
        text = self.ui.textEdit.toPlainText()
        if title not in self.notes:
            self.notes[title] = {"текст": text, "теги": []}
        else:
             self.notes[title]["текст"] = text
        self.save_file()
        self.ui.list_note.clear()
        self.ui.list_note.addItems(self.notes)

    def del_note(self):
        title = self.ui.lineEdit.text()
        if title in self.notes:
            del self.notes[title]
            self.save_file()
            self.add_note()
            self.ui.list_note.clear()
            self.ui.list_note.addItems(self.notes)
        

    def add_tag(self):
        title = self.ui.lineEdit.text() 
        tag_title, ok = QInputDialog.getText(self, "Введіть, тег", "Назва тега")
        if ok and tag_title != "":
            self.notes[title]["теги"].append(tag_title)
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.addItems(self.notes[title]["теги"])
            
    def del_tag(self):
        title = self.ui.lineEdit.text() 
        try:
            tag_title = self.ui.tag_list.selectedItems()[0].text()
        except:
            tag_title = None
        if tag_title and title != "":
            self.notes[title]["теги"].remove(tag_title)
            self.ui.listWidget_2.clear()
            self.iu.listWidget_2.addItems(self.notes[title]["теги"])



app = QApplication([])
ex = NoteWidget()
ex.show()
app.exec_()
