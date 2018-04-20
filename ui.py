# Импорт модулей
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QPainter, QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog, QAbstractItemView, QAction, QProgressBar
import numpy as np
import matplotlib.pyplot as plt
import configparser as cp
import csv
import graph_neuron
import neuron_network
import main


# Класс интерфейса и обработки событий
class UiMainWindow:
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
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblCompany = QtWidgets.QLabel(self.layoutWidget)
        self.lblCompany.setObjectName("lblCompany")
        self.verticalLayout.addWidget(self.lblCompany)
        self.txtCompany = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtCompany.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtCompany.setObjectName("txtCompany")
        self.verticalLayout.addWidget(self.txtCompany)
        self.lblCash = QtWidgets.QLabel(self.layoutWidget)
        self.lblCash.setObjectName("lblCash")
        self.verticalLayout.addWidget(self.lblCash)
        self.txtCash = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtCash.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtCash.setObjectName("txtCash")
        self.verticalLayout.addWidget(self.txtCash)
        self.lblQuickSellingSecurities = QtWidgets.QLabel(self.layoutWidget)
        self.lblQuickSellingSecurities.setObjectName("lblQuickSellingSecurities")
        self.verticalLayout.addWidget(self.lblQuickSellingSecurities)
        self.txtQuickSellingSecurities = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtQuickSellingSecurities.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtQuickSellingSecurities.setObjectName("txtQuickSellingSecurities")
        self.verticalLayout.addWidget(self.txtQuickSellingSecurities)
        self.lblTotalAssets = QtWidgets.QLabel(self.layoutWidget)
        self.lblTotalAssets.setObjectName("lblTotalAssets")
        self.verticalLayout.addWidget(self.lblTotalAssets)
        self.txtTotalAssets = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtTotalAssets.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtTotalAssets.setObjectName("txtTotalAssets")
        self.verticalLayout.addWidget(self.txtTotalAssets)
        self.lblNetSales = QtWidgets.QLabel(self.layoutWidget)
        self.lblNetSales.setObjectName("lblNetSales")
        self.verticalLayout.addWidget(self.lblNetSales)
        self.txtNetSales = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNetSales.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtNetSales.setObjectName("txtNetSales")
        self.verticalLayout.addWidget(self.txtNetSales)
        self.lblGrossIncome = QtWidgets.QLabel(self.layoutWidget)
        self.lblGrossIncome.setObjectName("lblGrossIncome")
        self.verticalLayout.addWidget(self.lblGrossIncome)
        self.txtGrossIncome = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtGrossIncome.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtGrossIncome.setObjectName("txtGrossIncome")
        self.verticalLayout.addWidget(self.txtGrossIncome)
        self.lblTotalDebt = QtWidgets.QLabel(self.layoutWidget)
        self.lblTotalDebt.setObjectName("lblTotalDebt")
        self.verticalLayout.addWidget(self.lblTotalDebt)
        self.txtTotalDebt = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtTotalDebt.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtTotalDebt.setObjectName("txtTotalDebt")
        self.verticalLayout.addWidget(self.txtTotalDebt)
        self.lblMainCapital = QtWidgets.QLabel(self.layoutWidget)
        self.lblMainCapital.setObjectName("lblMainCapital")
        self.verticalLayout.addWidget(self.lblMainCapital)
        self.txtMainCapital = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtMainCapital.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtMainCapital.setObjectName("txtMainCapital")
        self.verticalLayout.addWidget(self.txtMainCapital)
        self.lblNetAssets = QtWidgets.QLabel(self.layoutWidget)
        self.lblNetAssets.setObjectName("lblNetAssets")
        self.verticalLayout.addWidget(self.lblNetAssets)
        self.txtNetAssets = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNetAssets.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtNetAssets.setObjectName("txtNetAssets")
        self.verticalLayout.addWidget(self.txtNetAssets)
        self.lblWorkingCapital = QtWidgets.QLabel(self.layoutWidget)
        self.lblWorkingCapital.setObjectName("lblWorkingCapital")
        self.verticalLayout.addWidget(self.lblWorkingCapital)
        self.txtWorkingCapital = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtWorkingCapital.setMaximumSize(QtCore.QSize(270, 16777215))
        self.txtWorkingCapital.setObjectName("txtWorkingCapital")
        self.verticalLayout.addWidget(self.txtWorkingCapital)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnAddTableInput = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAddTableInput.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnAddTableInput.setObjectName("btnAddTableInput")
        self.gridLayout_2.addWidget(self.btnAddTableInput, 0, 0, 1, 1)
        self.btnResultPredict = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnResultPredict.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnResultPredict.setObjectName("btnResultPredict")
        self.gridLayout_2.addWidget(self.btnResultPredict, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.tableWidgetInput = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetInput.setRowCount(0)
        self.tableWidgetInput.setColumnCount(7)
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
        self.lblInputNeurons = QtWidgets.QLabel(self.grpBoxNeuronLayers)
        self.lblInputNeurons.setMaximumSize(QtCore.QSize(120, 20))
        self.lblInputNeurons.setObjectName("lblInputNeurons1")
        self.verticalLayout_3.addWidget(self.lblInputNeurons)
        self.spboxInputLayer = QtWidgets.QSpinBox(self.grpBoxNeuronLayers)
        self.spboxInputLayer.setMaximumSize(QtCore.QSize(120, 20))
        self.spboxInputLayer.setObjectName("spboxInputLayer")
        self.spboxInputLayer.setMinimum(1)
        self.verticalLayout_3.addWidget(self.spboxInputLayer)
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
        self.tabResult = QtWidgets.QWidget()
        self.tabResult.setObjectName("tabResult")
        self.tabWidget.addTab(self.tabResult, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tabResult)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidgetResult = QtWidgets.QTableWidget(self.tabResult)
        self.tableWidgetResult.setRowCount(0)
        self.tableWidgetResult.setColumnCount(2)
        self.tableWidgetResult.setObjectName("tableWidgetResult")
        self.horizontalLayout_8.addWidget(self.tableWidgetResult)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoadTrainData = QtWidgets.QMenu(self.menuFile)
        self.menuLoadTrainData.setObjectName("menuLoadTrainData")
        self.menuLoadInitialData = QtWidgets.QMenu(self.menuFile)
        self.menuLoadInitialData.setObjectName("menuLoadInitialData")
        self.menuNetwork = QtWidgets.QMenu(self.menubar)
        self.menuNetwork.setObjectName("menuNetwork")
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadTxt = QtWidgets.QAction(MainWindow)
        self.actionLoadTxt.setObjectName("actionLoadTxt")
        self.actionLoadCSV = QtWidgets.QAction(MainWindow)
        self.actionLoadCSV.setObjectName("actionLoadCSV")
        self.actionLoadTxtTrain = QtWidgets.QAction(MainWindow)
        self.actionLoadTxtTrain.setObjectName("actionLoadTxtTrain")
        self.actionLoadCSVTrain = QtWidgets.QAction(MainWindow)
        self.actionLoadCSVTrain.setObjectName("actionLoadCSVTrain")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+Q")
        self.menuLoadInitialData.addAction(self.actionLoadTxt)
        self.menuLoadInitialData.addAction(self.actionLoadCSV)
        self.menuLoadTrainData.addAction(self.actionLoadTxtTrain)
        self.menuLoadTrainData.addAction(self.actionLoadCSVTrain)
        self.menuFile.addAction(self.menuLoadInitialData.menuAction())
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
        self.actionResultsSave = QtWidgets.QAction(MainWindow)
        self.actionResultsSave.setObjectName("actionResultsSave")
        self.actionResultsSave.setShortcut("Ctrl+S")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setShortcut("F1")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuNetwork.addAction(self.actionNetworkSave)
        self.menuNetwork.addAction(self.actionNetworkLoad)
        self.menuResults.addAction(self.actionResultsSave)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addMenu(self.menuNetwork)
        self.menubar.addMenu(self.menuResults)
        self.menubar.addAction(self.menuAbout.menuAction())

        # Сигнал на закрытие окна программы
        self.actionExit.triggered.connect(exit)

        # Делаем выделение всей строки, а не отдельной ячейки
        self.tableWidgetInput.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetTrain.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetResult.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Заголовки входной таблицы
        headers_input = ['Предприятие', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6']
        self.tableWidgetInput.setHorizontalHeaderLabels(headers_input)

        # Заголовок таблицы с слоями
        header_layers = ['Слои']
        # Заголовки таблицы с слоями
        self.tableWidgetLayersNetwork.setHorizontalHeaderLabels(header_layers)

        # Заголовоки таблицы с данными для обучения
        headers_train = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'Результат']
        self.tableWidgetTrain.setHorizontalHeaderLabels(headers_train)

        headers_result = ['Предприятие', 'Результат']
        self.tableWidgetResult.setHorizontalHeaderLabels(headers_result)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Запрет на ввод текста в LineEdit
        reg = QRegExp("\d{1,}\.\d{0,}|\d{1,}")
        reg_num_only = QRegExp("\d{1,}")
        num_validator = QRegExpValidator(reg)
        num_only_validator = QRegExpValidator(reg_num_only)
        self.txtCash.setValidator(num_validator)
        self.txtTotalDebt.setValidator(num_validator)
        self.txtLearningRate.setValidator(num_validator)
        self.txtGrossIncome.setValidator(num_validator)
        self.txtMainCapital.setValidator(num_validator)
        self.txtWorkingCapital.setValidator(num_validator)
        self.txtNetAssets.setValidator(num_validator)
        self.txtNetSales.setValidator(num_validator)
        self.txtQuickSellingSecurities.setValidator(num_validator)
        self.txtTotalAssets.setValidator(num_validator)
        self.txtLearningSet.setValidator(num_only_validator)
        self.txtEpochs.setValidator(num_only_validator)
        self.txtTestSet.setValidator(num_only_validator)

        # Обработка событий
        # Добавление данных в таблицу
        def add_table_data():
            # Получаем в переменные значения полей
            company = self.txtCompany.text()
            cash = self.txtCash.text()
            quick_sell = self.txtQuickSellingSecurities.text()
            total_assets = self.txtTotalAssets.text()
            net_sales = self.txtNetSales.text()
            gross_income = self.txtGrossIncome.text()
            total_debt = self.txtTotalDebt.text()
            main_capital = self.txtMainCapital.text()
            net_assets = self.txtNetAssets.text()
            work_capital = self.txtWorkingCapital.text()

            # Если поля пустые, то выводим ошибку
            if company == ''\
                    or cash == '' \
                    or quick_sell == '' \
                    or total_assets == '' \
                    or net_sales == '' \
                    or gross_income == '' \
                    or total_debt == '' \
                    or main_capital == '' \
                    or net_assets == '' \
                    or work_capital == '':
                # Вывод ошибки
                empty_input_msg = QMessageBox()
                empty_input_msg.setIcon(QMessageBox.Critical)
                empty_input_msg.setWindowTitle("Ошибка добавления данных")
                empty_input_msg.setText("Одно или несколько полей исходных данных пустые!")
                empty_input_msg.exec()
            else:
                # Рассчет коэффициентов модели Чессера
                x1 = (float(cash) + float(quick_sell)) / float(total_assets)
                x2 = float(net_sales) / (float(cash) + float(quick_sell))
                x3 = float(gross_income) / float(total_assets)
                x4 = float(total_debt) / float(total_assets)
                x5 = float(main_capital) / float(net_assets)
                x6 = float(work_capital) / float(net_sales)

                # Создание списка с коэффициентами
                data_x = [round(x1, 5), round(x2, 5), round(x3, 5), round(x4, 5), round(x5, 5), round(x6, 5)]

                # Количество строк в таблице
                row_count = self.tableWidgetInput.rowCount()

                # Устанавливаем новое количество строк, т.к. нам надо добавить новую запись в таблицу
                self.tableWidgetInput.setRowCount(row_count + 1)

                self.tableWidgetInput.setItem(row_count, 0, QTableWidgetItem(company))

                # Считываем коэффициенты из списка и заносим их в таблицу
                for i in range(1, 7):
                    self.tableWidgetInput.setItem(row_count, i, QTableWidgetItem(str(data_x[i - 1])))

        # Загрузка данных из текстового файла в таблицу с исходными данными
        def load_txt():
            # Диалог выбора файла
            path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Текстовые файлы (*.txt)")[0]

            data_txt = []  # Список, в котором хранятся данные из текстового файла

            if path != "":
                f = open(path)  # Открываем файл с данными
                for line in f.readlines():  # Построчно считываем файл
                    # Добавляем в список строку из файла в виде кортежа ([входные_даннные], результат)
                    data_txt.append(line.replace("\n", "").split(" "))

                # Количество строк в таблице
                row_count = self.tableWidgetInput.rowCount()

                # Установка числа строк таблицы
                self.tableWidgetInput.setRowCount(row_count + len(data_txt))

                # Заполнение таблицы
                for i in range(len(data_txt)):
                    for j in range(self.tableWidgetInput.columnCount()):
                        self.tableWidgetInput.setItem(row_count + i, j, QTableWidgetItem(str(data_txt[i][j])))

        # Функция чтения CSV файла
        def csv_reader(file_obj):
            reader = csv.reader(file_obj)

            data_csv = []  # Список, в котором хранятся данные из CSV файла

            for row in reader:
                data_csv.append(" ".join(row).split(';'))

            return data_csv  # Возвращаем список с данными

        # Загрузка CSV файла в таблицу
        def load_csv():
            # Диалог выбора файла
            csv_path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Файды Excel (*.csv)")[0]

            if csv_path != "":
                # Читаем CSV файл
                with open(csv_path, 'r', newline='') as f_obj:

                    data_csv = csv_reader(f_obj)

                    # Количество строк в таблице
                    row_count = self.tableWidgetInput.rowCount()

                    # Установка числа строк таблицы
                    self.tableWidgetInput.setRowCount(row_count + len(data_csv))

                    # Заполнение таблицы
                    for i in range(len(data_csv)):
                        for j in range(self.tableWidgetInput.columnCount()):
                            self.tableWidgetInput.setItem(row_count + i, j, QTableWidgetItem(str(data_csv[i][j])))

        # Сигнал на нажатие кнопки "Добавить в таблицу"
        self.btnAddTableInput.clicked.connect(add_table_data)
        # Сигнал на загрузку текстового файла в таблицу
        self.actionLoadTxt.triggered.connect(load_txt)
        # Сигнал на загрузку CSV файла в таблицу
        self.actionLoadCSV.triggered.connect(load_csv)

        # Контекстное меню для таблицы исходных данных
        # Создание действий для таблицы
        add_row_alt = QAction("Добавить строку", self.tableWidgetInput)
        clear_row_alt = QAction("Очистить строку", self.tableWidgetInput)
        del_row_alt = QAction("Удалить строку", self.tableWidgetInput)
        clear_alt = QAction("Очистить таблицу", self.tableWidgetInput)
        save_alt = QAction("Сохранить таблицу", self.tableWidgetInput)

        # Добавить пустую строку
        def add_row():
            self.tableWidgetInput.insertRow(self.tableWidgetInput.rowCount())

        # Очистить строку
        def clr_row():
            index = self.tableWidgetInput.currentIndex().row()
            self.tableWidgetInput.removeRow(index)
            self.tableWidgetInput.insertRow(index)

        # Удалить выделенную строку
        def del_row():
            self.tableWidgetInput.removeRow(self.tableWidgetInput.currentIndex().row())

        # Очистить таблицу
        def clr_alt():
            self.tableWidgetInput.clear()
            self.tableWidgetInput.setRowCount(0)
            self.tableWidgetInput.setHorizontalHeaderLabels(headers_input)

        # Сохранить таблицу
        def sv_alt():
            if self.tableWidgetInput.rowCount() > 0:
                # Диалог сохранения таблицы с исходными данными
                path = QFileDialog.getSaveFileName(None, 'Сохранить исходные данные',
                                                         'c:\\', "Текстовые файлы (*.txt)")[0]

                if path != "":
                    f = open(path, 'a', encoding='cp1251')

                    for i in range(self.tableWidgetInput.rowCount()):
                        for j in range(self.tableWidgetInput.columnCount()):
                            f.write(self.tableWidgetInput.item(i, j).text() + " ")
                        f.write("\n")

                    f.close()
                else:
                    # Вывод ошибки
                    empty_input_msg = QMessageBox()
                    empty_input_msg.setIcon(QMessageBox.Critical)
                    empty_input_msg.setWindowTitle("Ошибка сохранения")
                    empty_input_msg.setText("Файл для сохранения не указан!")
                    empty_input_msg.exec()
            else:
                # Вывод ошибки
                empty_input_msg = QMessageBox()
                empty_input_msg.setIcon(QMessageBox.Critical)
                empty_input_msg.setWindowTitle("Ошибка сохранения")
                empty_input_msg.setText("Таблица пустая!")
                empty_input_msg.exec()

        # Сигнал на добавление строки
        add_row_alt.triggered.connect(add_row)
        # Сигнал на очистку строки
        clear_row_alt.triggered.connect(clr_row)
        # Сигнал на удаление строки
        del_row_alt.triggered.connect(del_row)
        # Сигнал на очистку таблицы
        clear_alt.triggered.connect(clr_alt)
        # Сигнал на охранение таблицы
        save_alt.triggered.connect(sv_alt)

        # Добавление действий к таблице
        self.tableWidgetInput.addAction(add_row_alt)
        self.tableWidgetInput.addAction(clear_row_alt)
        self.tableWidgetInput.addAction(del_row_alt)
        self.tableWidgetInput.addAction(clear_alt)
        self.tableWidgetInput.addAction(save_alt)

        # Установка контекстного меню к таблице
        self.tableWidgetInput.setContextMenuPolicy(Qt.ActionsContextMenu)

        # Контекстное меню для таблицы данных для обучения
        # Создание действий для таблицы
        add_row_alt_train = QAction("Добавить строку", self.tableWidgetTrain)
        clear_row_alt_train = QAction("Очистить строку", self.tableWidgetTrain)
        del_row_alt_train = QAction("Удалить строку", self.tableWidgetTrain)
        clear_alt_train = QAction("Очистить таблицу", self.tableWidgetTrain)

        # Добавить пустую строку
        def add_row_train():
            self.tableWidgetTrain.insertRow(self.tableWidgetTrain.rowCount())

        # Очистить строку
        def clr_row_train():
            index = self.tableWidgetTrain.currentIndex().row()
            self.tableWidgetTrain.removeRow(index)
            self.tableWidgetTrain.insertRow(index)

        # Удалить выделенную строку
        def del_row_train():
            self.tableWidgetTrain.removeRow(self.tableWidgetTrain.currentIndex().row())

        # Очистить таблицу
        def clr_alt_train():
            self.tableWidgetTrain.clear()
            self.tableWidgetTrain.setRowCount(0)
            self.tableWidgetTrain.setHorizontalHeaderLabels(headers_train)

        # Сигнал на добавление строки
        add_row_alt_train.triggered.connect(add_row_train)
        # Сигнал на очистку строки
        clear_row_alt_train.triggered.connect(clr_row_train)
        # Сигнал на удаление строки
        del_row_alt_train.triggered.connect(del_row_train)
        # Сигнал на очистку таблицы
        clear_alt_train.triggered.connect(clr_alt_train)

        # Добавление действий к таблице
        self.tableWidgetTrain.addAction(add_row_alt_train)
        self.tableWidgetTrain.addAction(clear_row_alt_train)
        self.tableWidgetTrain.addAction(del_row_alt_train)
        self.tableWidgetTrain.addAction(clear_alt_train)

        self.tableWidgetTrain.setContextMenuPolicy(Qt.ActionsContextMenu)

        # Список слоев с нейронами
        lay = []

        # Функция добавления числа входных нейроннов в список
        def input_output_neurons():
            self.tableWidgetLayersNetwork.setRowCount(1)
            item = QTableWidgetItem(str(self.spboxInputLayer.value()))
            item.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
            self.tableWidgetLayersNetwork.setItem(0, 0, item)
            hidden_layers_count()

        def hidden_layers_count():
            self.tableWidgetLayersNetwork.setRowCount(3)
            self.tableWidgetLayersNetwork.setItem(2, 0, QTableWidgetItem())
            item = QTableWidgetItem(str(self.spboxHiddenLayers.value()))
            item.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
            self.tableWidgetLayersNetwork.setItem(1, 0, item)
            item2 = QTableWidgetItem(str(1))
            item2.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
            self.tableWidgetLayersNetwork.setItem(2, 0, item2)

        # Обработка spinBox
        self.spboxInputLayer.valueChanged.connect(input_output_neurons)
        self.spboxHiddenLayers.valueChanged.connect(hidden_layers_count)

        # Загрузка данных из текстового файла в таблицу с данными для обучения
        def load_txt_train():
            path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Текстовые файлы (*.txt)")[0]

            data_txt = []  # Список, в котором хранятся данные из файла

            if path != "":
                f = open(path)  # Открываем файл с данными
                for line in f.readlines():  # Построчно считываем файл
                    # Добавляем в список строку из файла в виде кортежа ([входные_даннные], результат)
                    data_txt.append(line.replace("\n", "").split(" "))

                # Количество строк в таблице
                row_count = self.tableWidgetTrain.rowCount() - 1

                # Установка числа строк таблицы
                self.tableWidgetTrain.setRowCount(row_count + len(data_txt) - 1)

                # Заполнение таблицы
                for i in range(len(data_txt)):
                    for j in range(7):
                        self.tableWidgetTrain.setItem(row_count + i, j, QTableWidgetItem(str(data_txt[i][j])))

        # Загрузка CSV файла в таблицу с данными для обучения
        def load_csv_train():
            # Диалог выбора файла
            csv_path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Файды Excel (*.csv)")[0]

            if csv_path != "":
                # Читаем CSV файл
                with open(csv_path, 'r', newline='') as f_obj:

                    data_csv = csv_reader(f_obj)

                    # Количество строк в таблице
                    row_count = self.tableWidgetTrain.rowCount()

                    # Установка числа строк таблицы
                    self.tableWidgetTrain.setRowCount(row_count + len(data_csv))

                    # Заполнение таблицы
                    for i in range(len(data_csv)):
                        for j in range(self.tableWidgetTrain.columnCount()):
                            self.tableWidgetTrain.setItem(row_count + i, j,
                                                          QTableWidgetItem(str(data_csv[i][j])))

        # Сигнал на загрузку текстового файла в таблицу с данными для обучения
        self.actionLoadTxtTrain.triggered.connect(load_txt_train)
        # Сигнал на загрузку CSV файла в таблицу с данными для обучения
        self.actionLoadCSVTrain.triggered.connect(load_csv_train)

        # Изменение кривизны функции
        def slope():
            self.lblSlopeValue.setText(str(self.sliderSlope.value() / 1000))
            return int(self.sliderSlope.value()) / 1000

        # Сигнал изменения положения слайдера
        self.sliderSlope.valueChanged.connect(slope)

        self.network = None

        # Функция создания нейронной сети и ее графа
        def create_nn():
            row_count = self.tableWidgetLayersNetwork.rowCount()

            for item in range(0, row_count):
                try:
                    it = int(self.tableWidgetLayersNetwork.item(item, 0).text())
                    lay.append(it)
                except Exception:
                    create_error_msg = QMessageBox()
                    create_error_msg.setIcon(QMessageBox.Critical)
                    create_error_msg.setWindowTitle("Ошибка создания сети")
                    create_error_msg.setText("Таблица слоев пустая!")
                    create_error_msg.exec()

            # Проверяем число слоев
            if len(lay) != 0:
                # Рисуем граф
                gn = graph_neuron.Graph(lay)
                self.graphicsView.setScene(gn.g_scene())
                self.graphicsView.setRenderHint(QPainter.Antialiasing)

                learning_rate = self.txtLearningRate.text()  # Считываем из поля скорость обучения нейронной сети

                if learning_rate == '':
                    create_error_msg = QMessageBox()
                    create_error_msg.setIcon(QMessageBox.Critical)
                    create_error_msg.setWindowTitle("Ошибка создания сети")
                    create_error_msg.setText("Скорость обучения сети не может быть пустым значением!")
                    create_error_msg.exec()
                else:
                    # Создаем экземпляр класса нейронной сети
                    self.network = neuron_network.NN(slope=slope(),
                                                     input_neurons=lay[0],
                                                     hidden_neurons=lay[1],
                                                     learning_rate=float(learning_rate))

            # Очищаем список слоев с нейронами
            lay.clear()

        # Обработка нажатия кнопки создания нейронной сети
        self.btnCreateNetwork.clicked.connect(create_nn)

        # Функция обучения нейронной сети
        def train_nn():
            data = []  # Список, в котором хранятся данные из таблицы с данными для обучения
            lines = []  # Список в котором хранятся строки из таблицы с данными для обучения
            line = ''  # Строка таблицы

            # Считываем таблицу в список строк
            for i in range(self.tableWidgetTrain.rowCount()):
                for j in range(self.tableWidgetTrain.columnCount()):
                    line += self.tableWidgetTrain.item(i, j).text() + ' '
                lines.append(line.strip())
                line = ''

            self.value_error = False

            try:
                for l in lines:  # Построчно считываем таблицу
                    # Добавляем в список строку в виде кортежа ([входные_даннные], результат)
                    data.append((list(map(float, l.split(" ")[:-1])), int(l.split(" ")[-1])))
            except ValueError:
                train_error_msg = QMessageBox()
                train_error_msg.setIcon(QMessageBox.Critical)
                train_error_msg.setWindowTitle("Ошибка обучения сети")
                train_error_msg.setText("Данные для обучения неверны!")
                train_error_msg.exec()
                self.value_error = True

            # Количество строк обучающего множества
            train_set = self.txtLearningSet.text()

            # Количество строк тестово множества
            test_set = self.txtTestSet.text()

            # Считываем количество эпох
            epochs = self.txtEpochs.text()

            # Обработка ошибок
            if self.value_error is not True:
                if epochs == '' or train_set == '' or test_set == '' or self.tableWidgetTrain.rowCount() == 0:
                    train_error_msg = QMessageBox()
                    train_error_msg.setIcon(QMessageBox.Critical)
                    train_error_msg.setWindowTitle("Ошибка обучения сети")
                    train_error_msg.setText("Количество эпох обучения или количество строк обучающего или "
                                            "тестового набора сети не может быть пустым значением "
                                            "или таблица с данными для обучения пустая!")
                    train_error_msg.exec()
                else:
                    # Создаем поля для вывода прогресса обучения, ошибки и тип множества
                    self.lblStatusTrain = QtWidgets.QLabel(self.statusbar)
                    self.lblStatusTrain.setObjectName("lblStatusTrain")
                    self.lblStatusTrain.setText("Прогресс обучения:")
                    self.lblStatusTrainLoss = QtWidgets.QLabel(self.statusbar)
                    self.lblStatusTrainLoss.setObjectName("lblStatusTrainLoss")
                    self.lblTrainSet = QtWidgets.QLabel(self.statusbar)
                    self.lblTrainSet.setObjectName("lblTrainSet")
                    self.lblAccuracyNN = QtWidgets.QLabel(self.statusbar)
                    self.lblAccuracyNN.setObjectName("lblAccuracyNN")
                    # Создаем progress bar
                    self.prgBarTrain = QProgressBar(self.statusbar)

                    # Удаление виджетов из status bar
                    for i in range(3, 8, 1):
                        if self.statusbar.childAt(2, i) is not None:
                            self.statusbar.removeWidget(self.statusbar.childAt(2, i))

                    self.lblTrainSet.setText("Обучающее множество")
                    self.statusbar.addWidget(self.lblTrainSet)
                    self.statusbar.addWidget(self.lblStatusTrain)
                    self.statusbar.addWidget(self.prgBarTrain)

                    if int(train_set) > self.tableWidgetTrain.rowCount() or\
                            int(test_set) > self.tableWidgetTrain.rowCount()\
                            or int(train_set) == 0 or int(test_set) == 0:
                        train_error_msg = QMessageBox()
                        train_error_msg.setIcon(QMessageBox.Critical)
                        train_error_msg.setWindowTitle("Ошибка обучения сети")
                        train_error_msg.setText("Обучающее или тестовое множество не может быть больше чем строк "
                                                "в таблице или равным нулю!")
                        train_error_msg.exec()
                    else:
                        end = int(train_set) + int(test_set)

                        # Заполнение ячеек белым цветом
                        for i in range(self.tableWidgetTrain.rowCount()):
                            for j in range(7):
                                self.tableWidgetTrain.item(i, j).setBackground(Qt.white)

                        # Обучающее множество
                        for i in range(0, int(train_set)):
                            for j in range(7):
                                self.tableWidgetTrain.item(i, j).setBackground(Qt.green)

                        # Тестовое множество
                        for i in range(int(train_set), int(end)):
                            for j in range(7):
                                self.tableWidgetTrain.item(i, j).setBackground(Qt.yellow)

                        # Создаем списки для построения графиков
                        self.t_x = [i for i in range(0, int(epochs))]  # Список X
                        self.tr_y = []  # Список Y обучающего множества
                        self.tst_y = []  # Список Y тестового множества

                        try:
                            # Обучение на обучающем множестве
                            for e in range(int(epochs)):
                                inputs_ = []
                                correct_predictions = []
                                row_count = int(train_set)
                                for input_stat, correct_predict in data[:row_count]:
                                    self.network.train(np.array(input_stat), correct_predict)
                                    inputs_.append(np.array(input_stat))
                                    correct_predictions.append(np.array(correct_predict))

                                train_loss = self.network.mse(self.network.predict(np.array(inputs_).T),
                                                              np.array(correct_predictions))
                                self.lblStatusTrainLoss.setText("Ошибка обучения: {}"
                                                                .format(str(round(train_loss, 7))))
                                # Заполнение списка с координатами Y
                                self.tr_y.append(train_loss)

                                # Значение progress bar
                                value = int(100 * (e + 1) / float(epochs))

                                self.prgBarTrain.setValue(value)

                            self.statusbar.addWidget(self.lblStatusTrainLoss)

                            # Обучение на тестовом множестве
                            self.lblTrainSet.setText("Тестовое множество")
                            self.train_loss = None
                            self.row_count_train = int(train_set)
                            self.row_count_test = int(test_set) + int(train_set)

                            for e in range(int(epochs)):
                                inputs_ = []
                                correct_predictions = []
                                for input_stat, correct_predict in data[self.row_count_train:self.row_count_test]:
                                    self.network.train(np.array(input_stat), correct_predict)
                                    inputs_.append(np.array(input_stat))
                                    correct_predictions.append(np.array(correct_predict))

                                self.train_loss = self.network.mse(self.network.predict(np.array(inputs_).T),
                                                                   np.array(correct_predictions))

                                # Заполнение списка с координатами Y
                                self.tst_y.append(self.train_loss)

                                # Значение progress bar
                                value = int(100 * (e + 1) / float(epochs))

                                # Установка значения прогрессбара
                                self.prgBarTrain.setValue(value)

                            self.lblStatusTrainLoss.setText(self.lblStatusTrainLoss.text() + ", "
                                                            + str(round(self.train_loss, 7)))

                            i = 0  # Переменная для подсчета точности нейронной сети

                            for input_stat, correct_predict in data[self.row_count_test:]:
                                a = correct_predict == 1
                                b = self.network.predict(np.array(input_stat)) > .5
                                if (a and b) or (not a and not b):
                                    i = i + 1

                            self.lblAccuracyNN.setText("Точность нейронной сети: {}%".format(
                                str(round(i / (len(data[self.row_count_test:])) * 100, 1))))

                            self.statusbar.addWidget(self.lblAccuracyNN)

                            # Смена заголовка окна с графиками
                            fig = plt.gcf()
                            fig.canvas.set_window_title('Графики')
                            fig.set_size_inches(8, 8)

                            # Очищаем окно с графиками
                            fig.clear()

                            # Подграфик, первое число - количество графиков по вертикали,
                            # второе - по горизонтали, третье - номер графика
                            plt.subplot(211)
                            plt.title('Сигмоида')  # Заголовок графика
                            x = np.linspace(-10, 10, 1000)
                            y = self.network.sigmoid(x)
                            plt.plot(x, y)
                            plt.grid(True)  # Показываем сетку

                            # Отрисовка графика обучения
                            plt.subplot(212)
                            plt.title('Обучение нейронной сети')  # Заголовок графика
                            plt.xlabel('Эпоха')  # Название оси X
                            plt.ylabel('Ошибка')  # Название оси Y
                            # Рисуем график для обучающего множества
                            plt.plot(self.t_x, self.tr_y, label='Обучающее множество')
                            plt.subplot(212)
                            # Рисуем график для тестового множества
                            plt.plot(self.t_x, self.tst_y, label='Тестовое множество')
                            plt.legend()  # Показываем легенду
                            plt.grid(True)  # Показываем сетку
                            plt.show()  # Показываем график
                        except Exception:
                            train_error_msg = QMessageBox()
                            train_error_msg.setIcon(QMessageBox.Critical)
                            train_error_msg.setWindowTitle("Ошибка сети")
                            train_error_msg.setText("Обучение или построение графиков невозможно!")
                            train_error_msg.exec()

        # Обработка нажатия кнопки обучения нейронной сети
        self.btnTrain.clicked.connect(train_nn)

        def predict_nn():
            if self.network is not None and self.tableWidgetInput.rowCount() != 0:
                data = []  # Список с входными значениями
                line = []  # Список элементов строки таблицы
                result = []  # Список с результатом предсказания

                # Считываем данные с входной таблицы в список
                for i in range(self.tableWidgetInput.rowCount()):
                    for j in range(1, self.tableWidgetInput.columnCount()):
                        line.append(float(self.tableWidgetInput.item(i, j).text()))
                    data.append(line.copy())
                    line.clear()

                # Число строк результирующей таблицы
                self.tableWidgetResult.setRowCount(len(data))

                # Заполняем результирующую таблицу
                for row in range(len(data)):
                    item = QTableWidgetItem(self.tableWidgetInput.item(row, 0).text())
                    item.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
                    self.tableWidgetResult.setItem(row, 0, QTableWidgetItem(item))

                # Предсказываем кредитоспособность предприятия
                for input_stat in data:
                    if self.network.predict(np.array(input_stat)) > .5:
                        result.append("Кредитоспособно")
                    else:
                        result.append("Некредитоспособно")

                # Заполняем результирующую таблицу данными о кредитоспособности
                for row in range(len(data)):
                    item = QTableWidgetItem(str(result[row]))
                    item.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
                    self.tableWidgetResult.setItem(row, 1, QTableWidgetItem(item))
            else:
                predict_error_msg = QMessageBox()
                predict_error_msg.setIcon(QMessageBox.Critical)
                predict_error_msg.setWindowTitle("Ошибка предсказания")
                predict_error_msg.setText("Сеть не создана или нет данных для предсказания!")
                predict_error_msg.exec()

        # Обработка нажатия кнопки "Результат"
        self.btnResultPredict.clicked.connect(predict_nn)

        # Функция сохранения состояния нейронной сети
        def save_nn():
            if self.network is not None:
                path = QFileDialog.getSaveFileName(None, 'Выберите файл', 'c:\\', "Файлы конфигурации (*.ini)")[0]

                if path != "":
                    # Сохраняем веса в переменные
                    weights1 = self.network.get_weights()[0]
                    weights2 = self.network.get_weights()[1]

                    # Создаем файл конфигурации с сохранением параметров обучения сети
                    config = cp.ConfigParser()
                    config.add_section("Settings")
                    config.set("Settings", "input_neurons", self.tableWidgetLayersNetwork.item(0, 0).text())
                    config.set("Settings", "hidden_neurons", self.tableWidgetLayersNetwork.item(1, 0).text())
                    config.set("Settings", "slope", str(slope()))
                    config.set("Settings", "learning_set", self.txtLearningSet.text())
                    config.set("Settings", "test_set", self.txtTestSet.text())
                    config.set("Settings", "epochs", self.txtEpochs.text())
                    config.set("Settings", "learning_rate", self.txtLearningRate.text())
                    config.add_section("Weights")

                    it = 0

                    for line in weights1:
                        for item in line:
                            config.set("Weights", "weights_input_{}".format(str(it)), str(item))
                            it += 1

                    it = 0

                    for line in weights2:
                        for item in line:
                            config.set("Weights", "weights_output_{}".format(str(it)), str(item))
                            it += 1

                    # Запись в файл
                    with open(path, "w") as config_file:
                        config.write(config_file)

            else:
                save_error_msg = QMessageBox()
                save_error_msg.setIcon(QMessageBox.Critical)
                save_error_msg.setWindowTitle("Ошибка сохранения")
                save_error_msg.setText("Нет данных для сохранения!")
                save_error_msg.exec()

        # Cигнал на сохранения нейронной сети
        self.actionNetworkSave.triggered.connect(save_nn)

        # Функция для чтения файла конфигурации
        def get_config(path):
            config = cp.ConfigParser()
            config.read(path)
            return config

        # Функция для получения настроек из файла конфигурации
        def get_setting(path, section, setting):
            config = get_config(path)
            value = config.get(section, setting)
            return value

        # Загрузка весов нейронной сети
        def load_nn():
            # Получаем название выбранного файла
            path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Файлы конфигурации (*.ini)")[0]

            if path != "":
                # Получение значений из файла конфигурации
                input_neurons = get_setting(path, "Settings", "input_neurons")
                hidden_neurons = get_setting(path, "Settings", "hidden_neurons")
                slope = get_setting(path, "Settings", "slope")
                learning_set = get_setting(path, "Settings", "learning_set")
                test_set = get_setting(path, "Settings", "test_set")
                epochs = get_setting(path, "Settings", "epochs")
                learning_rate = get_setting(path, "Settings", "learning_rate")

                # Количество весов
                weights1_count = int(input_neurons) * int(hidden_neurons)
                weights2_count = int(hidden_neurons)

                items = []  # Список элементов из файла конфигурации

                # Считываем значения весов из файла конфигурации
                for item in range(weights1_count):
                    items.append(float(get_setting(path, "Weights", "weights_input_{}".format(str(item)))))

                # Разбиваем список считанных значений из файла конфигураций на списки
                weights1 = [items[d:d + int(input_neurons)] for d in range(0, len(items), int(input_neurons))]

                # чищаем список элементов
                items.clear()

                # Считываем значения весов из файла конфигурации
                for item in range(weights2_count):
                    items.append(float(get_setting(path, "Weights", "weights_output_{}".format(str(item)))))

                # Разбиваем список считанных значений из файла конфигураций на списки
                weights2 = [items[d:d + int(weights2_count)] for d in range(0, len(items), int(weights2_count))]

                # Установка значений из файла конфигурации
                self.tableWidgetLayersNetwork.setRowCount(3)
                self.tableWidgetLayersNetwork.setItem(0, 0, QTableWidgetItem(input_neurons))
                self.tableWidgetLayersNetwork.setItem(1, 0, QTableWidgetItem(hidden_neurons))
                self.tableWidgetLayersNetwork.setItem(2, 0, QTableWidgetItem("1"))
                self.spboxInputLayer.setValue(int(input_neurons))
                self.spboxHiddenLayers.setValue(int(hidden_neurons))
                self.sliderSlope.setValue(int(float(slope) * 1000))
                self.lblSlopeValue.setText(slope)
                self.txtLearningSet.setText(learning_set)
                self.txtTestSet.setText(test_set)
                self.txtEpochs.setText(epochs)
                self.txtLearningRate.setText(learning_rate)

                # Список слоев
                layer = []

                # Заполнение списка слоев
                for row in range(self.tableWidgetLayersNetwork.rowCount()):
                    layer.append(int(self.tableWidgetLayersNetwork.item(row, 0).text()))

                # Отрисовка графа нейронной сети
                gn = graph_neuron.Graph(layer)
                self.graphicsView.setScene(gn.g_scene())
                self.graphicsView.setRenderHint(QPainter.Antialiasing)

                # Создаем экземпляр класса нейронной сети
                self.network = neuron_network.NN(slope=float(slope),
                                                 input_neurons=layer[0],
                                                 hidden_neurons=layer[1],
                                                 learning_rate=float(learning_rate))

                # Установка новых весов сети
                self.network.set_weights(weights1, weights2)

        # Cигнал на загрузку нейронной сети
        self.actionNetworkLoad.triggered.connect(load_nn)

        # Функция записи информации в CSV
        def csv_writer(data, path):
            with open(path, "w", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                for line in data:
                    writer.writerow(line)

        # Функция сохранения результатов в файл CSV
        def save_results():
            if self.tableWidgetResult.rowCount() != 0:
                path = QFileDialog.getSaveFileName(None, 'Выберите файл', 'c:\\', "Excel файлы (*.csv)")[0]

                if path != "":
                    data = []
                    line = []

                    for i in range(self.tableWidgetResult.rowCount()):
                        for j in range(2):
                            line.append(self.tableWidgetResult.item(i, j).text())
                        data.append(line.copy())
                        line.clear()

                    csv_writer(data, path)
            else:
                save_error_msg = QMessageBox()
                save_error_msg.setIcon(QMessageBox.Critical)
                save_error_msg.setWindowTitle("Ошибка сохранения")
                save_error_msg.setText("Нет результатов для сохранения!")
                save_error_msg.exec()

        # Cигнал на сохранения нейронной сети
        self.actionResultsSave.triggered.connect(save_results)

        # Вызов окна о программе
        def abt():
            self.about = main.About()
            self.about.setWindowFlags(Qt.Window | Qt.MSWindowsFixedSizeDialogHint)
            self.about.show()

        self.actionAbout.triggered.connect(abt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кредитный скоринг"))
        self.lblCompany.setText(_translate("MainWindow", "Предприятие"))
        self.lblCash.setText(_translate("MainWindow", "Денежные средства"))
        self.lblQuickSellingSecurities.setText(_translate("MainWindow", "Быстрореализуемые ценные бумаги"))
        self.lblTotalAssets.setText(_translate("MainWindow", "Совокупные активы"))
        self.lblNetSales.setText(_translate("MainWindow", "Нетто - продажи"))
        self.lblGrossIncome.setText(_translate("MainWindow", "Бруто - доходы"))
        self.lblTotalDebt.setText(_translate("MainWindow", "Совокупная задолженность"))
        self.lblMainCapital.setText(_translate("MainWindow", "Основной капитал"))
        self.lblNetAssets.setText(_translate("MainWindow", "Чистые активы"))
        self.lblWorkingCapital.setText(_translate("MainWindow", "Оборотный капитал"))
        self.btnAddTableInput.setText(_translate("MainWindow", "Добавить в таблицу"))
        self.btnResultPredict.setText(_translate("MainWindow", "Результат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Исходные данные"))
        self.grpBoxNetworkStruct.setTitle(_translate("MainWindow", "Структура нейронной сети"))
        self.grpBoxNeuronLayers.setTitle(_translate("MainWindow", "Нейроны в слоях"))
        self.lblInputNeurons.setText(_translate("MainWindow", "Входной слой"))
        self.lblHiddenLayers.setText(_translate("MainWindow", "Скрытый слой"))
        self.btnCreateNetwork.setText(_translate("MainWindow", "Создать сеть"))
        self.grpBoxActivation.setTitle(_translate("MainWindow", "Сигмоида"))
        self.lblSlope.setText(_translate("MainWindow", "Крутизна функции"))
        self.lblSlopeValue.setText(_translate("MainWindow", "1.0"))
        self.grpBoxTrain.setTitle(_translate("MainWindow", "Обучение нейронной сети"))
        self.lblLearningSet.setText(_translate("MainWindow", "Обучающее множество"))
        self.lblTestSet.setText(_translate("MainWindow", "Тестовое множество"))
        self.lblEpochs.setText(_translate("MainWindow", "Количество эпох"))
        self.lblLearningRate.setText(_translate("MainWindow", "Скорость обучения"))
        self.btnTrain.setText(_translate("MainWindow", "Обучить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNetwork), _translate("MainWindow", "Нейронная сеть"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraph), _translate("MainWindow", "Граф нейросети"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResult), _translate("MainWindow", "Результат"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuLoadInitialData.setTitle(_translate("MainWindow", "Загрузить исходные данные..."))
        self.menuLoadTrainData.setTitle(_translate("MainWindow", "Загрузить данные для обучения..."))
        self.actionLoadTxt.setText(_translate("MainWindow", "Загрузить из текстового файла"))
        self.actionLoadCSV.setText(_translate("MainWindow", "Загрузить из CSV файла"))
        self.actionLoadTxtTrain.setText(_translate("MainWindow", "Загрузить из текстового файла"))
        self.actionLoadCSVTrain.setText(_translate("MainWindow", "Загрузить из CSV файла"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.menuNetwork.setTitle(_translate("MainWindow", "Нейронная сеть"))
        self.actionNetworkSave.setText(_translate("MainWindow", "Сохранить сеть"))
        self.actionNetworkLoad.setText(_translate("MainWindow", "Загрузить сеть"))
        self.menuResults.setTitle(_translate("MainWindow", "Результаты"))
        self.actionResultsSave.setText(_translate("MainWindow", "Сохранить"))
        self.menuAbout.setTitle(_translate("MainWindow", "Справка"))
        self.actionHelp.setText(_translate("MainWindow", "Просмотреть справку"))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))


