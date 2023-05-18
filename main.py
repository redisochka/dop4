from PyQt5 import QtCore, QtWidgets, Qt
import sys

class MainClass():

    def calc(self):
        try:
            k = f'Ширина = {self.mainWindow.mainWindow_widthEdit.text()}, Длина = {self.mainWindow.mainWindow_lengthEdit.text()}, тип = {self.mainWindow.mainWindow_combobox_material_type.currentText()}'
            #задали переменные в одной строке, что бы памяти меньше кушало. . . и плюс что бы там внизу окна выводилось что мы выбрали
        except BaseException:
            k = 'ошбика ввода данныых' #базовый класс для исключения исключений :)

        self.mainWindow.mainWindow_label_mass.setText(k)

    class mainWindowClass(QtWidgets.QMainWindow):
    #далее создаем эту рамочку по красоте
        def __init__(self, parent=None, fatherlyClass=None): #база
            QtWidgets.QMainWindow.__init__(self, parent)
            self.centralwidget = QtWidgets.QWidget()
            self.centralwidget.setObjectName("centralwidget")

            self.mainWindow_widthEdit = QtWidgets.QLineEdit() #создает строку ввода
            self.mainWindow_widthEdit.setObjectName("width")

            self.mainWindow_lengthEdit = QtWidgets.QLineEdit() #создает строку ввода
            self.mainWindow_lengthEdit.setObjectName("length")

            self.mainWindow_combobox_material_type = QtWidgets.QComboBox() #строки для списка
            self.mainWindow_combobox_material_type.addItems(
                ['Пластик','Алюминий','Соломка','Текстиль'])
            self.mainWindow_combobox_material_type.setObjectName("material_type")

            self.mainWindow_label_mass = QtWidgets.QLabel() #
            self.mainWindow_label_mass.setObjectName("label_mass")
            self.mainWindow_label_mass.setText(" ")

            self.mainWindow_label_width = QtWidgets.QLabel() #создает текст
            self.mainWindow_label_width.setObjectName("label_width")
            self.mainWindow_label_width.setText("Ширина (см.)")

            self.mainWindow_label_length = QtWidgets.QLabel() #создает текст
            self.mainWindow_label_length.setObjectName("label_length")
            self.mainWindow_label_length.setText("Высота (см.)")

            self.mainWindow_label_material_type = QtWidgets.QLabel() #создает текст
            self.mainWindow_label_material_type.setObjectName("label_material_type")
            self.mainWindow_label_material_type.setText("Материал")

            self.mainWindow_button_calc = QtWidgets.QPushButton('OK') #определяет командную кнопку
            self.mainWindow_button_calc.setObjectName("button_find")

            hboxWidth = QtWidgets.QHBoxLayout() #выравнивание
            hboxWidth.addWidget(self.mainWindow_label_width)
            hboxWidth.addWidget(self.mainWindow_widthEdit)
            hboxWidth.addSpacing(1)

            hboxLength = QtWidgets.QHBoxLayout() #выравнивание
            hboxLength.addWidget(self.mainWindow_label_length)
            hboxLength.addWidget(self.mainWindow_lengthEdit)

            hboxMaterial = QtWidgets.QHBoxLayout() #выравнивание
            hboxMaterial.addWidget(self.mainWindow_label_material_type)
            hboxMaterial.addWidget(self.mainWindow_combobox_material_type)

            hboxButton = QtWidgets.QHBoxLayout() #выравнивание
            hboxButton.addWidget(self.mainWindow_button_calc)

            vbox = QtWidgets.QVBoxLayout() #выравнивание
            vbox.addLayout(hboxLength)
            vbox.addLayout(hboxWidth)
            vbox.addLayout(hboxMaterial)
            vbox.addLayout(hboxButton)
            vbox.addWidget(self.mainWindow_label_mass)

            self.centralwidget.setLayout(vbox) #задает геометрию - выравнивание
            self.setCentralWidget(self.centralwidget)

            self.mainWindow_button_calc.clicked.connect(fatherlyClass.calc) #присоединяем к кнопке функции

    def __init__(self):

        self.mainWindow = self.mainWindowClass(fatherlyClass=self)
        self.mainWindow.setWindowTitle('Жалюзи')
        self.mainWindow.setWindowFlags(QtCore.Qt.Window)
        self.mainWindow.setFixedWidth(320) #размеры окна
        self.mainWindow.setFixedHeight(200)
        self.mainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainClass()
    sys.exit(app.exec_()) #вызывает окно