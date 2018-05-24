"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: интерфейс главного окна программы и установка необходимых параметров
Дата разработки: 06.05.2018
"""

# Импорт модулей
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QAbstractItemView, QAction

import SpinBoxDelegate
import SpinBoxDelegateTrain


# Класс интерфейса и обработки событий
class MainUi:

    # Настройка интерфейса
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.tableWidgetInput = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetInput.setRowCount(0)
        self.tableWidgetInput.setColumnCount(10)
        self.tableWidgetInput.setObjectName("tableWidgetInput")
        self.horizontalLayout_2.addWidget(self.tableWidgetInput)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tabNetwork = QtWidgets.QWidget()
        self.tabNetwork.setObjectName("tabNetwork")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabNetwork)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.grpBoxNetworkStruct = QtWidgets.QGroupBox(self.tabNetwork)
        self.grpBoxNetworkStruct.setMaximumSize(QtCore.QSize(370, 16777215))
        self.grpBoxNetworkStruct.setObjectName("grpBoxNetworkStruct")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.grpBoxNetworkStruct)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.grpBoxNeuronLayers = QtWidgets.QGroupBox(self.grpBoxNetworkStruct)
        self.grpBoxNeuronLayers.setMaximumSize(QtCore.QSize(350, 200))
        self.grpBoxNeuronLayers.setObjectName("grpBoxNeuronLayers")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.grpBoxNeuronLayers)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblHiddenLayers = QtWidgets.QLabel(self.grpBoxNeuronLayers)
        self.lblHiddenLayers.setMaximumSize(QtCore.QSize(120, 20))
        self.lblHiddenLayers.setObjectName("lblHiddenLayers")
        self.verticalLayout_3.addWidget(self.lblHiddenLayers)
        self.spboxHiddenLayers = QtWidgets.QSpinBox(self.grpBoxNeuronLayers)
        self.spboxHiddenLayers.setMaximumSize(QtCore.QSize(120, 20))
        self.spboxHiddenLayers.setObjectName("spboxHiddenLayers")
        self.spboxHiddenLayers.setMinimum(1)
        self.verticalLayout_3.addWidget(self.spboxHiddenLayers)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tableWidgetLayersNetwork = QtWidgets.QTableWidget(self.grpBoxNeuronLayers)
        self.tableWidgetLayersNetwork.setMaximumSize(QtCore.QSize(250, 300))
        self.tableWidgetLayersNetwork.setRowCount(1)
        self.tableWidgetLayersNetwork.setColumnCount(1)
        self.tableWidgetLayersNetwork.setObjectName("tableWidgetLayersNetwork")
        self.tableWidgetLayersNetwork.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidgetLayersNetwork)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.grpBoxNeuronLayers)
        self.grpBoxActivation = QtWidgets.QGroupBox(self.grpBoxNetworkStruct)
        self.grpBoxActivation.setMaximumSize(QtCore.QSize(350, 70))
        self.grpBoxActivation.setObjectName("grpBoxActivation")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.grpBoxActivation)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblSlope = QtWidgets.QLabel(self.grpBoxActivation)
        self.lblSlope.setObjectName("lblSlope")
        self.gridLayout_3.addWidget(self.lblSlope, 1, 0, 1, 1)
        self.lblSlopeValue = QtWidgets.QLabel(self.grpBoxActivation)
        self.lblSlopeValue.setObjectName("lblSlopeValue")
        self.gridLayout_3.addWidget(self.lblSlopeValue, 1, 2, 1, 1)
        self.sliderSlope = QtWidgets.QSlider(self.grpBoxActivation)
        self.sliderSlope.setMaximumSize(QtCore.QSize(220, 16777215))
        self.sliderSlope.setMinimum(10)
        self.sliderSlope.setMaximum(4000)
        self.sliderSlope.setSliderPosition(1000)
        self.sliderSlope.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSlope.setObjectName("sliderSlope")
        self.gridLayout_3.addWidget(self.sliderSlope, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout_4.addWidget(self.grpBoxActivation)
        self.grpBoxTrain = QtWidgets.QGroupBox(self.grpBoxNetworkStruct)
        self.grpBoxTrain.setMaximumSize(QtCore.QSize(350, 200))
        self.grpBoxTrain.setObjectName("grpBoxTrain")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.grpBoxTrain)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblLearningSet = QtWidgets.QLabel(self.grpBoxTrain)
        self.lblLearningSet.setObjectName("lblLearningSet")
        self.gridLayout_5.addWidget(self.lblLearningSet, 0, 0, 1, 1)
        self.txtLearningSet = QtWidgets.QLineEdit(self.grpBoxTrain)
        self.txtLearningSet.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtLearningSet.setObjectName("txtLearningSet")
        self.gridLayout_5.addWidget(self.txtLearningSet, 0, 1, 1, 1)
        self.lblTestSet = QtWidgets.QLabel(self.grpBoxTrain)
        self.lblTestSet.setObjectName("lblTestSet")
        self.gridLayout_5.addWidget(self.lblTestSet, 1, 0, 1, 1)
        self.txtTestSet = QtWidgets.QLineEdit(self.grpBoxTrain)
        self.txtTestSet.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtTestSet.setObjectName("txtTestSet")
        self.gridLayout_5.addWidget(self.txtTestSet, 1, 1, 1, 1)
        self.lblEpochs = QtWidgets.QLabel(self.grpBoxTrain)
        self.lblEpochs.setObjectName("lblEpochs")
        self.gridLayout_5.addWidget(self.lblEpochs, 2, 0, 1, 1)
        self.txtEpochs = QtWidgets.QLineEdit(self.grpBoxTrain)
        self.txtEpochs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtEpochs.setObjectName("txtEpochs")
        self.gridLayout_5.addWidget(self.txtEpochs, 2, 1, 1, 1)
        self.lblLearningRate = QtWidgets.QLabel(self.grpBoxTrain)
        self.lblLearningRate.setObjectName("lblLearningRate")
        self.gridLayout_5.addWidget(self.lblLearningRate, 3, 0, 1, 1)
        self.txtLearningRate = QtWidgets.QLineEdit(self.grpBoxTrain)
        self.txtLearningRate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtLearningRate.setObjectName("txtLearningRate")
        self.gridLayout_5.addWidget(self.txtLearningRate, 3, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.btnCreateNetwork = QtWidgets.QPushButton(self.grpBoxTrain)
        self.btnCreateNetwork.setMaximumSize(QtCore.QSize(120, 25))
        self.btnCreateNetwork.setObjectName("btnCreateNetwork")
        self.btnTrain = QtWidgets.QPushButton(self.grpBoxTrain)
        self.btnTrain.setObjectName("btnTrain")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.addWidget(self.btnCreateNetwork, 0, 0)
        self.gridLayout_6.addWidget(self.btnTrain, 0, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.grpBoxTrain)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addWidget(self.grpBoxNetworkStruct)
        self.tableWidgetTrain = QtWidgets.QTableWidget(self.tabNetwork)
        self.tableWidgetTrain.setColumnCount(7)
        self.tableWidgetTrain.setObjectName("tableWidgetTrain")
        self.tableWidgetTrain.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.tableWidgetTrain)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tabNetwork, "")
        self.tabGraph = QtWidgets.QWidget()
        self.tabGraph.setObjectName("tabGraph")
        self.graphicsView = QtWidgets.QGraphicsView(self.tabGraph)
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tabGraph, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoadTrainData = QtWidgets.QMenu(self.menuFile)
        self.menuLoadTrainData.setObjectName("menuLoadTrainData")
        self.menuNetwork = QtWidgets.QMenu(self.menubar)
        self.menuNetwork.setObjectName("menuNetwork")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadTxtTrain = QtWidgets.QAction(MainWindow)
        self.actionLoadTxtTrain.setObjectName("actionLoadTxtTrain")
        self.actionLoadCSVTrain = QtWidgets.QAction(MainWindow)
        self.actionLoadCSVTrain.setObjectName("actionLoadCSVTrain")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+Q")
        self.menuLoadTrainData.addAction(self.actionLoadTxtTrain)
        self.menuLoadTrainData.addAction(self.actionLoadCSVTrain)
        self.menuFile.addAction(self.menuLoadTrainData.menuAction())
        self.menuFile.addAction(self.menuLoadTrainData.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.actionNetworkSave = QtWidgets.QAction(MainWindow)
        self.actionNetworkSave.setObjectName("actionNetworkSave")
        self.actionNetworkSave.setShortcut("Ctrl+K")
        self.actionNetworkLoad = QtWidgets.QAction(MainWindow)
        self.actionNetworkLoad.setObjectName("actionNetworkLoad")
        self.actionNetworkLoad.setShortcut("Ctrl+L")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuNetwork.addAction(self.actionNetworkSave)
        self.menuNetwork.addAction(self.actionNetworkLoad)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addMenu(self.menuNetwork)
        self.menubar.addAction(self.menuAbout.menuAction())

        # Делаем выделение всей строки, а не отдельной ячейки
        self.tableWidgetInput.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetTrain.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Заголовки входной таблицы
        self.headers_input = ['Денежные средства', 'Ценные бумаги', 'Совокупные активы', 'Нетто-продажи',
                              'Брутто-доходы', 'Совокупная задолженность', 'Основной капитал', 'Чистые активы',
                              'Оборотный капитал', 'Результат']

        # Устанавливаем заголовки таблицы
        self.tableWidgetInput.setHorizontalHeaderLabels(self.headers_input)

        self.tableWidgetInput.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Заголовок таблицы с слоями
        self.header_layers = ['Слои']

        # Заголовки таблицы с слоями
        self.tableWidgetLayersNetwork.setHorizontalHeaderLabels(self.header_layers)

        # Заголовоки таблицы с данными для обучения
        self.headers_train = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'Результат']
        self.tableWidgetTrain.setHorizontalHeaderLabels(self.headers_train)

        # Запрет на ввод текста в LineEdit
        reg = QRegExp("\d{1,}\.\d{0,}|\d{1,}")
        reg_num_only = QRegExp("\d{1,}")
        num_validator = QRegExpValidator(reg)
        num_only_validator = QRegExpValidator(reg_num_only)

        self.txtLearningRate.setValidator(num_validator)
        self.txtLearningSet.setValidator(num_only_validator)
        self.txtEpochs.setValidator(num_only_validator)
        self.txtTestSet.setValidator(num_only_validator)

        # Контекстное меню для таблицы исходных данных
        # Разделитель для меню
        act = QAction(None, self.tableWidgetInput)
        act.setSeparator(True)
        act1 = QAction(None, self.tableWidgetInput)
        act1.setSeparator(True)

        # Создание действий для таблицы
        self.add_row_alt = QAction("Добавить строку", self.tableWidgetInput)
        self.clear_row_alt = QAction("Очистить строку", self.tableWidgetInput)
        self.del_row_alt = QAction("Удалить строку", self.tableWidgetInput)
        self.clear_alt = QAction("Очистить таблицу", self.tableWidgetInput)
        self.save_alt = QAction("Сохранить таблицу", self.tableWidgetInput)
        self.result_alt = QAction("Результат (строка)", self.tableWidgetInput)
        self.result_all_alt = QAction("Результат (таблица)", self.tableWidgetInput)

        # Добавление действий к таблице
        self.tableWidgetInput.addAction(self.add_row_alt)
        self.tableWidgetInput.addAction(self.clear_row_alt)
        self.tableWidgetInput.addAction(self.del_row_alt)
        self.tableWidgetInput.addAction(act)
        self.tableWidgetInput.addAction(self.clear_alt)
        self.tableWidgetInput.addAction(self.save_alt)
        self.tableWidgetInput.addAction(act1)
        self.tableWidgetInput.addAction(self.result_alt)
        self.tableWidgetInput.addAction(self.result_all_alt)

        # Контекстное меню для таблицы данных для обучения
        # Разделитель для меню
        act = QAction(None, self.tableWidgetInput)
        act.setSeparator(True)

        # Создание действий для таблицы
        self.add_row_alt_train = QAction("Добавить строку", self.tableWidgetTrain)
        self.clear_row_alt_train = QAction("Очистить строку", self.tableWidgetTrain)
        self.del_row_alt_train = QAction("Удалить строку", self.tableWidgetTrain)
        self.clear_alt_train = QAction("Очистить таблицу", self.tableWidgetTrain)

        # Добавление действий к таблице
        self.tableWidgetTrain.addAction(self.add_row_alt_train)
        self.tableWidgetTrain.addAction(self.clear_row_alt_train)
        self.tableWidgetTrain.addAction(self.del_row_alt_train)
        self.tableWidgetTrain.addAction(act)
        self.tableWidgetTrain.addAction(self.clear_alt_train)

        # Установка контекстного меню к таблице
        self.tableWidgetInput.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableWidgetTrain.setContextMenuPolicy(Qt.ActionsContextMenu)

        # Установка делегата на ячейки таблицы
        self.tableWidgetInput.setItemDelegate(SpinBoxDelegate.SpinBoxDelegate())
        self.tableWidgetTrain.setItemDelegate(SpinBoxDelegateTrain.SpinBoxDelegateTrain())

        # Включаем сортировку таблиц
        self.tableWidgetInput.setSortingEnabled(True)
        self.tableWidgetTrain.setSortingEnabled(True)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Перевод интерфейса
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кредитный скоринг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Исходные данные"))
        self.grpBoxNetworkStruct.setTitle(_translate("MainWindow", "Структура нейронной сети"))
        self.grpBoxNeuronLayers.setTitle(_translate("MainWindow", "Нейроны в слоях"))
        self.lblHiddenLayers.setText(_translate("MainWindow", "Скрытый слой"))
        self.btnCreateNetwork.setText(_translate("MainWindow", "Создать сеть"))
        self.grpBoxActivation.setTitle(_translate("MainWindow", "Сигмоида"))
        self.lblSlope.setText(_translate("MainWindow", "Крутизна функции"))
        self.lblSlopeValue.setText(_translate("MainWindow", "1.0"))
        self.grpBoxTrain.setTitle(_translate("MainWindow", "Обучение нейронной сети"))
        self.lblLearningSet.setText(_translate("MainWindow", "Обучающее множество (%)"))
        self.lblTestSet.setText(_translate("MainWindow", "Тестовое множество (%)"))
        self.lblEpochs.setText(_translate("MainWindow", "Количество эпох"))
        self.lblLearningRate.setText(_translate("MainWindow", "Скорость обучения"))
        self.btnTrain.setText(_translate("MainWindow", "Обучить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNetwork), _translate("MainWindow", "Нейронная сеть"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraph), _translate("MainWindow", "Граф нейросети"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuLoadTrainData.setTitle(_translate("MainWindow", "Загрузить данные для обучения..."))
        self.actionLoadTxtTrain.setText(_translate("MainWindow", "Загрузить из текстового файла"))
        self.actionLoadCSVTrain.setText(_translate("MainWindow", "Загрузить из CSV файла"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.menuNetwork.setTitle(_translate("MainWindow", "Нейронная сеть"))
        self.actionNetworkSave.setText(_translate("MainWindow", "Сохранить сеть"))
        self.actionNetworkLoad.setText(_translate("MainWindow", "Загрузить сеть"))
        self.menuAbout.setTitle(_translate("MainWindow", "Справка"))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))


