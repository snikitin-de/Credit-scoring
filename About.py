# Импорт модулей
from PyQt5 import QtWidgets
import AboutUi


# Класс окна о программе
class About(QtWidgets.QMainWindow):
    # Инициализация класса
    def __init__(self, parent=None):
        super(About, self).__init__(parent=parent)
        # Установка ui
        self.gui = AboutUi.AboutUi()
        self.gui.setupUi(self)
