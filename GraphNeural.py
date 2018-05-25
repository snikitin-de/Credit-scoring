"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: отрисовка графа нейронной сети
Дата разработки: 21.12.2017
"""

# Импорт модулей
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Класс вершина
class Node(QGraphicsEllipseItem):
    # Инициализация класса, принимающая на вход родителя
    def __init__(self, parent=None):
        QGraphicsEllipseItem.__init__(self, QRectF(-20, -20, 40, 40), parent)
        self.edges = []  # Список ребер
        self.setBrush(Qt.white)  # Устновка кисти в белый цвет

    # Добавление ребра
    def add_edge(self, edge):
        self.edges.append(edge)  # Добавляем ребро в список ребер


# Класс ребро
class Edge(QGraphicsLineItem):
    # Инициализация класса
    def __init__(self, source, dest, color, parent=None):
        QGraphicsLineItem.__init__(self, parent)
        self.source = source  # Первая вершина
        self.dest = dest  # Вторая вершина
        self.source.add_edge(self)  # Добавляем ребро для первой вершины
        self.dest.add_edge(self)  # Добавляем ребро для второй вершины
        self.setPen(QPen(color, 1.75))  # Установка цвета и размера карандаша
        self.setLine(QLineF(self.dest.pos(), self.source.pos()))  # Установка линии


# Класс отрисовки графа
class Graph(QGraphicsScene):
    # Инициализация класса, в аргументы конструктора класса передаем родителя и список слоев
    def __init__(self, layers, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.dst_layer = 500  # Дистанция между слоями
        self.dst_neuron = 100  # Дистанция между нейронами
        self.scene = QGraphicsScene()  # Графическая сцена
        self.layers = layers  # Слои нейронной сети
        self.groups = []  # Список групп объектов слоев
        self.y_centers = []  # Список координат y центра

    def g_scene(self):
        # Для всех слоев
        for layer in range(len(self.layers)-1, -1, -1):
            group = QGraphicsItemGroup()  # Присваиваем переменной group объект QGraphicsItemGroup
            # Устанавливаем положение элементов относительно друг друга в Z-плоскости
            group.setZValue(10)
            self.scene.addItem(group)  # Добавляем группу на сцену
            for neuron in range(0, self.layers[layer]):  # Для всех нейронов в слое
                node = Node(group)  # Создаем экземпляр класса Node в конструктор которого передаем текущую группу
                self.scene.addItem(node)  # Добавляем на сцену вершину
                node.setPos(self.dst_layer * layer, self.dst_neuron * neuron)  # Устанавливаем позицию вершины
                # Определяем цвет слоев в графе (зеленый - входной, синие - скрытые, красный - выходной)
                node.setPen(Qt.green if layer == 0 else Qt.red if layer == (len(self.layers)-1) else Qt.blue)
                group.addToGroup(node)  # Добавляем вершину в группу

            self.groups.append(group)  # Добавляем текущую группу в список групп
            self.y_centers.append(group.boundingRect().center().y())  # Добавляем в список центров центр текущей группы

        # Получаем список разницы между максимальным элементов в списке центров и текущим элементом
        ys = [max(self.y_centers) - center for center in self.y_centers]

        # Двигаем полученные группы элементов на необходимые расстояние для центрирования слоев
        for group, y in zip(self.groups, ys):
            [item.moveBy(0, y) for item in group.childItems()]

        for i in range(len(self.groups)-1):
            last_group = self.groups[i]  # Текущая группа
            next_group = self.groups[i+1]  # Следующая группа
            for last_item in last_group.childItems():  # Для всех элементов в текущей группе
                for next_item in next_group.childItems():  # Для всех элементов следующей группы
                    # Для входного слоя и скрытого, цвет линии - красный, иначе синий
                    if i == 0:
                        color = Qt.blue
                    else:
                        color = Qt.red
                    # Создаем объект класса Edge в который передаем текущий элемент и следующий
                    edge = Edge(last_item, next_item, color)
                    self.scene.addItem(edge)  # Добавляем ребро на сцену
        return self.scene  # Возвращаем сцену


