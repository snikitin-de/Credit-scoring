"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: ввести запрет на ввод в ячейки таблицы всех символов кроме цифр
Дата разработки: 24.04.2018
"""

# Импорт модулей
from PyQt5 import QtWidgets

import SpinBoxDelegate


# Создаем класс делегата для зтого, чтобы можно было вводить в ячейки таблицы только цифры
# Наследуемся от класса с делегатом для того, чтобы изменить некоторые параметры ячейки не переписывая весь класс
class SpinBoxDelegateTrain(SpinBoxDelegate.SpinBoxDelegate):

    # Создаем компонент-редактор, используемый для правки значений количества позиций
    def createEditor(self, parent, options, index):
        if index.column() < 5:
            editor = QtWidgets.QDoubleSpinBox(parent)
            editor.setFrame(False)
            editor.setMinimum(-100)
            editor.setMaximum(100)
            editor.setSingleStep(0.00001)
            editor.setDecimals(5)

            return editor


