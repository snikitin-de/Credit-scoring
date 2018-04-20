# Импорт модулей
from PyQt5 import QtCore, QtWidgets
import ui
import about


# Класс окна о программе
class About(QtWidgets.QMainWindow):
    # Инициализация класса
    def __init__(self, parent=None):
        super(About, self).__init__(parent=parent)
        # Установка ui
        self.gui = about.Ui_About()
        self.gui.setupUi(self)


# Главный класс программы
class Window(QtWidgets.QMainWindow):
    # Ловим событие на изменения формы
    resized = QtCore.pyqtSignal()

    # Инициализация класса
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        # Установка ui
        self.gui = ui.UiMainWindow()
        self.gui.setupUi(self)

    # Переопределяем события изменения размера формы
    def resizeEvent(self, event):
        self.resized.emit()
        # Если размер вкладки меньше необходимого, то задаем размер graphicsView необходимые значения
        if self.gui.tabGraph.width() < 1280 and self.gui.tabGraph.height() < 650:
            self.gui.graphicsView.setGeometry(QtCore.QRect(0, 0, 1280, 650))
        # Иначе задаем размер graphicsView по размеру вкладки
        elif self.gui.tabGraph.width() >= 1280 and self.gui.tabGraph.height() >= 650:
            self.gui.graphicsView.setGeometry(QtCore.QRect(0, 0, self.gui.tabGraph.width(), self.gui.tabGraph.height()))
        return super(Window, self).resizeEvent(event)


if __name__ == "__main__":
    # Импортируем модуль
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Создаем объект класса Window
    w = Window()
    # Устанавливаем минимальную ширину и высоту окна
    w.setMinimumHeight(720)
    w.setMinimumWidth(1280)
    # Показываем окно
    w.show()
    sys.exit(app.exec_())
