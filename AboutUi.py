"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: интерфейс окна "О программе"
Дата разработки: 08.02.2018
"""

# Импорт модулей
from PyQt5 import QtCore, QtWidgets


# Класс интерфейса окна "О программе"
class AboutUi(object):
    # Настройка интерфейса
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(539, 143)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 131))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    # Перевод интерфейса
    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "О программе"))
        self.label.setText(_translate("About",
                                      "<html>"
                                      "<head/>"
                                      "<body>"
                                      "<p>Программа разработана как ВКР на тему &quot;"
                                      "Разработка аналитической системы на основе плоскостной нейронной сети "
                                      "прямого распространения&quot;</p>"
                                      "<p>Версия программы: 1.0</p><p>"
                                      "Разработчик: студент группы 446 "
                                      "Никитин Сергей Александрович ©"
                                      "</p><p>Рязань, РГРТУ, 2017</p><"
                                      "/body>"
                                      "</html>"))
