"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: ввести запрет на ввод в ячейки таблицы всех символов кроме цифр
Дата разработки: 24.04.2018
"""

# Импорт модулей
from PyQt5 import QtCore, QtWidgets


# Создаем класс делегата для зтого, чтобы можно было вводить в ячейки таблицы только цифры
class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):

    # Создаем компонент-редактор, используемый для правки значений количества позиций
    def createEditor(self, parent, options, index):
        if index.column() < 9:
            editor = QtWidgets.QDoubleSpinBox(parent)
            editor.setFrame(False)
            editor.setMinimum(1)
            editor.setMaximum(100000000)
            editor.setSingleStep(1)

            return editor

    # Заносим в компонент-редактор значение количества
    def setEditorData(self, editor, index):
        val = index.model().data(index, QtCore.Qt.EditRole)

        if type(val) is float:
            value = float(val)
            editor.setValue(value)

    # Указываем размеры компонента-редактора
    def updateEditorGeometry(self, editor, options, index):
        editor.setGeometry(options.rect)

    # Заносим исправленное значение в модель
    def setModelData(self, editor, model, index):
        value = str(editor.value())
        model.setData(index, value, QtCore.Qt.EditRole)


