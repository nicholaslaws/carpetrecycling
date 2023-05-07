""" Implement GUI window for the optimization code for ease of use """

import os
import sys
from PyQt5 import QtWidgets
import process_run

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("background-color: lightgrey;")

    def initUI(self):
        # Get list of .json files
        files = [f for f in os.listdir() if f.endswith('.json')]

        pad = 25
        windH = 600
        windL = 800
        buttL = 300
        buttH = 150
        textL = (windL/2) - (2*pad)
        textH = (windH) - (2*pad)
        

        # Create button
        button = QtWidgets.QPushButton('Optimize', self)
        button.clicked.connect(self.button_clicked)
        button.setFixedHeight(buttH)
        button.setFixedWidth(buttL)
        button.move(int((windL/4)-(buttL/2)), int((windH-buttH)/2)+pad)
        button.setStyleSheet("background-color: lightblue;")

        # Create dropdown button
        dropdown = QtWidgets.QComboBox(self)
        dropdown.addItems(files)
        dropdown.setCurrentIndex(0)
        dropdown.setFixedWidth(buttL-(2*pad))
        dropdown.currentIndexChanged.connect(self.dropdown_selected)
        dropdown.move(pad+int((windL/4)-(buttL/2)), 2*pad)
        dropdown.setStyleSheet("background-color: 21,150,150")
        self.dropdown = dropdown

        # Create text box
        self.text_box = QtWidgets.QTextEdit(self)
        self.text_box.setFixedHeight(textH)
        self.text_box.setFixedWidth(int(textL))
        self.text_box.move(int(windL-pad-textL), int(pad))
        self.text_box.setStyleSheet("background-color: white")

        # Set window properties
        self.setWindowTitle('Harvard SEAS - Carpet Composition Optimization Algorithm')
        self.setFixedSize(windL, windH)

    def button_clicked(self):
        self.text_box.clear()
        selected_file = self.dropdown.currentText()
        # Run the algorithm code
        self.text_box.insertPlainText(f'Optimizing design in: {selected_file}\n\n')
        self.text_box.insertPlainText(process_run.run_process(selected_file))


    def dropdown_selected(self, index):
        selected_file = self.dropdown.currentText()
        self.filename = selected_file
        print('Selected file:', selected_file)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
