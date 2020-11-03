import sys, re
from HelpGUI import *
from AboutGUI import * 
from MainGUI import *

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        def test():
            print("test")

        def help():
            otherview = HelpForm() 
            otherview.show() 

        def about():
            pass

        def exit():
            sys.exit(app.exec_())

        def add():
            if (self.ui.lineEdit.text() == ""):
                pass
            else:
                self.ui.listWidget.addItem(self.ui.lineEdit.text())
                self.ui.lineEdit.setText("")
        
        def delete():
            self.ui.listWidget.takeItem(self.ui.listWidget.row(self.ui.listWidget.currentItem()))
            
        
        def edit():
            item = self.ui.listWidget.currentItem()
            self.ui.lineEdit.setText(item.text())
            self.ui.listWidget.takeItem(self.ui.listWidget.row(self.ui.listWidget.currentItem()))
        
        def use():
            item = self.ui.listWidget.currentItem()
           
            self.ui.label_3.setText(item.text())
        
        def matchen():
            self.ui.label_4.setText("Eingabe wird überprüft..... bitte warten")
            if (self.ui.lineEdit_2.text() == ""):
                self.ui.label_4.setText("Bitte zuerst etwas eingeben...")
            else:
                if (self.ui.checkBox.checkState):
                    if (re.match(self.ui.label_3.text()+ "$", self.ui.lineEdit_2.text())):
                        self.ui.label_4.setText("Die Eingabe passt")
                    else:
                        self.ui.label_4.setText("Die Eingabe passt nicht")
                else: 
                    if (re.match(self.ui.label_3.text()+ "$", self.ui.lineEdit_2.text(), re.IGNORECASE)):
                        self.ui.label_4.setText("Die Eingabe passt")
                    else:
                        self.ui.label_4.setText("Die Eingabe passt nicht")


        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add.clicked.connect(add)
        self.ui.edit.clicked.connect(edit)
        self.ui.use.clicked.connect(use)
        self.ui.delete_2.clicked.connect(delete)
        
        ###########
        # Menubar #
        ###########

        self.ui.actionbeenden.triggered.connect(exit)
        self.ui.actionHilfe_2.triggered.connect(help)
        self.ui.actionueber.triggered.connect(about)
        
        self.ui.test.clicked.connect(matchen)


class HelpForm():
    def __init__(self, parent=None):
        #super(HelpForm, self).__init__(parent)
        self.helpUi = Ui_HelpWindow()
        self.helpUi.setupUi(self)

        self.helpUi.ok.connect(sys.exit(app.exec_()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())


