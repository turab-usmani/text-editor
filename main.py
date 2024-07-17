from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtGui import QFontDatabase, QFont, QShortcut, QKeySequence, QTextCharFormat, QTextCursor
from PyQt6.QtCore import Qt
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('assets/main_window.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.show()
        self.file_name = ""

        self.SaveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.OpenShortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.ExitShortcut = QShortcut(QKeySequence("Esc"), self)

        self.FontIncreaseButton.clicked.connect(self.increase_font_size)
        self.FontDecreaseButton.clicked.connect(self.decrease_font_size)
        self.FontComboBox.addItems(QFontDatabase.families())
        self.FontComboBox.currentTextChanged.connect(self.change_font)
        self.BoldButton.clicked.connect(self.bold_text)
        self.ItalicButton.clicked.connect(self.italicise_text)
        self.UnderlineButton.clicked.connect(self.underline_text)
        self.FontColourButton.clicked.connect(self.change_font_colour)
        self.BgColourButton.clicked.connect(self.change_bg_colour)
        self.actionSave.triggered.connect(self.save_file)
        self.SaveShortcut.activated.connect(self.save_file)
        self.OpenShortcut.activated.connect(self.open_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSaveas.triggered.connect(self.saveas_file)
        self.actionExit.triggered.connect(self.exit_app)
        self.LeftAlignButton.clicked.connect(self.align_left)
        self.RightAlignButton.clicked.connect(self.align_right)
        self.CenterAlignButton.clicked.connect(self.align_center)
        self.JustifyButton.clicked.connect(self.align_justify)
        self.SuperScriptButton.clicked.connect(self.superscript_text)
        self.SubScriptButton.clicked.connect(self.subscript_text)
        self.ExitShortcut.activated.connect(self.exit_app)

    def increase_font_size(self):
        try:
            self.TextBox.setFontPointSize(self.TextBox.fontPointSize() + 1)
        except Exception as e:
            print(e)

    def decrease_font_size(self):
        try:
            self.TextBox.setFontPointSize(self.TextBox.fontPointSize() - 1)
        except Exception as e:
            print(e)

    def change_font(self):
        try:
            self.TextBox.setFontFamily(self.FontComboBox.currentText())
        except Exception as e:
            print(e)


    def bold_text(self):
        try:
            if self.TextBox.fontWeight() == QFont.Weight.Bold:
                self.TextBox.setFontWeight(QFont.Weight.Normal)
            else:
                self.TextBox.setFontWeight(QFont.Weight.Bold)
        except Exception as e:
            print(e)

    def italicise_text(self):
        try:
            if self.TextBox.fontItalic():
                self.TextBox.setFontItalic(False)
            else:
                self.TextBox.setFontItalic(True)
        except Exception as e:
            print(e)

    def underline_text(self):
        try:
            if self.TextBox.fontUnderline():
                self.TextBox.setFontUnderline(False)
            else:
                self.TextBox.setFontUnderline(True)
        except Exception as e:
            print(e)


    def change_font_colour(self):
        try:
            self.TextBox.setTextColor(QtWidgets.QColorDialog.getColor())
        except Exception as e:
            print(e)

    def change_bg_colour(self):
        try:
            self.TextBox.setTextBackgroundColor(QtWidgets.QColorDialog.getColor())
        except Exception as e:
            print(e)

    def saveas_file(self):
        try:
            # Open a file dialog to select the save location
            self.file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

            if self.file_name:
                # Save the contents of the text edit to the file
                with open(self.file_name, 'w') as file:
                    file.write(self.TextBox.toPlainText())
        except Exception as e:
            print(e)

    def open_file(self):
        try:
            self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Save File", "",
                                                                 "Text Files (*.txt);;All Files (*)")
            if self.file_name:
                with open(self.file_name, 'r+') as file:
                    self.TextBox.insertPlainText(file.read())

        except Exception as e:
           print(e)

    def save_file(self):
        try:
            if self.file_name:
                with open(self.file_name, 'w') as file:
                    file.write(self.TextBox.toPlainText())
            else:
                self.saveas_file()
        except Exception as e:
           print("Exception ", e)

    def exit_app(self):
        try:
            QtWidgets.QApplication.quit()
        except Exception as e:
            print(e)


    def align_left(self):
        try:
            self.TextBox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        except Exception as e:
            print(e)


    def align_center(self):
        try:
            self.TextBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except Exception as e:
            print(e)

    def align_right(self):
        try:
            self.TextBox.setAlignment(Qt.AlignmentFlag.AlignRight)
        except Exception as e:
            print(e)


    def align_justify(self):
        try:
            self.TextBox.setAlignment(Qt.AlignmentFlag.AlignJustify)
        except Exception as e:
            print(e)


    def superscript_text(self):
        try:
            if self.TextBox.currentCharFormat().verticalAlignment() == QTextCharFormat.VerticalAlignment.AlignNormal:
                new_format = QTextCharFormat()
                new_format.setVerticalAlignment(QTextCharFormat.VerticalAlignment.AlignSuperScript)
                self.TextBox.setCurrentCharFormat(new_format)
            else:
                new_format = QTextCharFormat()
                new_format.setVerticalAlignment(QTextCharFormat.VerticalAlignment.AlignNormal)
                self.TextBox.setCurrentCharFormat(new_format)

        except Exception as e:
            print(e)

    def subscript_text(self):
        try:
            if self.TextBox.currentCharFormat().verticalAlignment() == QTextCharFormat.VerticalAlignment.AlignNormal:
                new_format = QTextCharFormat()
                new_format.setVerticalAlignment(QTextCharFormat.VerticalAlignment.AlignSubScript)
                self.TextBox.setCurrentCharFormat(new_format)
            else:
                new_format = QTextCharFormat()
                new_format.setVerticalAlignment(QTextCharFormat.VerticalAlignment.AlignNormal)
                self.TextBox.setCurrentCharFormat(new_format)
        except Exception as e:
            print("Exception" , e)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec()

