from PyQt5 import QtWidgets

import SpinBoxDelegate


# Создаем класс делегата
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


