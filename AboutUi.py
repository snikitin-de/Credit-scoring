# Импорт модулей
from PyQt5 import QtCore, QtWidgets


class AboutUi(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(539, 143)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 131))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

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
