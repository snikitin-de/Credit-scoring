from PyQt5 import QtCore, QtWidgets


# Создаем класс делегата
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


