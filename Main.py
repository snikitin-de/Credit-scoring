# Импорт модулей
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog, QProgressBar
from PyQt5.QtGui import QPainter

import csv
import sys
import numpy as np
import configparser as cp
import matplotlib.pyplot as plt
import MainUi
import GraphNeural
import NeuralNetwork
import About


# Главный класс программы
class Main(QtWidgets.QMainWindow):
    # Ловим событие на изменения формы
    resized = QtCore.pyqtSignal()

    # Список слоев с нейронами
    lay = []

    # Переменнная для объекта нейроной сети
    network = None

    # Добавить пустую строку
    def add_row(self):
        self.gui.tableWidgetInput.insertRow(self.gui.tableWidgetInput.rowCount())

    # Очистить строку
    def clr_row(self):
        index = self.gui.tableWidgetInput.currentIndex().row()
        self.gui.tableWidgetInput.removeRow(index)
        self.gui.tableWidgetInput.insertRow(index)

    # Удалить выделенную строку
    def del_row(self):
        self.gui.tableWidgetInput.removeRow(self.gui.tableWidgetInput.currentIndex().row())

    # Очистить таблицу
    def clr_alt(self):
        self.gui.tableWidgetInput.clear()
        self.gui.tableWidgetInput.setRowCount(0)
        self.gui.tableWidgetInput.setHorizontalHeaderLabels(self.gui.headers_input)

    # Сохранить таблицу
    def sv_alt(self):
        if self.gui.tableWidgetInput.rowCount() > 0:
            # Диалог сохранения таблицы с исходными данными
            path = QFileDialog.getSaveFileName(None, 'Сохранить таблицу',
                                               'c:\\', "CSV (*.csv)")[0]

            # Если путь не пустой
            if path != "":
                data = []

                for i in range(self.gui.tableWidgetInput.rowCount()):

                    line = []

                    for j in range(self.gui.tableWidgetInput.columnCount()):
                        item = self.gui.tableWidgetInput.item(i, j)
                        if item is not None:
                            line.append(self.gui.tableWidgetInput.item(i, j).text())
                    data.append(line)

                # Записываем данные в CSV файл
                self.csv_writer(data, path)
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

    # Результат предсказания для строки
    def rslt_alt(self):
        # Инициализируем переменную для определения пустых ячеек значением True
        empty_value = True

        # Индекс выделенной строки
        row = self.gui.tableWidgetTrain.currentIndex().row() + 1

        # Проходим циклом по столбцам выделенной строки
        for j in range(self.gui.tableWidgetInput.columnCount() - 1):
            # Если найдена пустая ячейка, то меняем значение переменной empty_value на False и выходим из цикла
            if self.gui.tableWidgetInput.item(row, j) is None:
                empty_value = False
                break

        # Если найдена пустая ячейка, то выводим ошибку, иначе предсказываем результат
        if empty_value is False:
            # Вывод ошибки
            empty_input_msg = QMessageBox()
            empty_input_msg.setIcon(QMessageBox.Critical)
            empty_input_msg.setWindowTitle("Ошибка обработки таблицы")
            empty_input_msg.setText("Строка имеет одну или несколько пустых ячеек!")
            empty_input_msg.exec()
        else:
            self.predict_nn(False)

    # Результат предсказания для таблицы
    def rslt_all_alt(self):
        # Инициализируем переменную для определения пустых ячеек значением True
        empty_value = True

        # Проходим циклом по таблице
        for i in range(self.gui.tableWidgetInput.rowCount()):
            for j in range(self.gui.tableWidgetInput.columnCount() - 1):
                # Если найдена пустая ячейка, то меняем значение переменной empty_value на False и выходим из цикла
                if self.gui.tableWidgetInput.item(i, j) is None:
                    empty_value = False
                    break

        # Если найдена пустая ячейка, то выводим ошибку, иначе предсказываем результат
        if empty_value is False:
            # Вывод ошибки
            empty_input_msg = QMessageBox()
            empty_input_msg.setIcon(QMessageBox.Critical)
            empty_input_msg.setWindowTitle("Ошибка обработки таблицы")
            empty_input_msg.setText("Таблица имеет одну или несколько пустых ячеек!")
            empty_input_msg.exec()
        else:
            self.predict_nn(True)

    # Добавить пустую строку
    def add_row_train(self):
        self.gui.tableWidgetTrain.insertRow(self.gui.tableWidgetTrain.rowCount())

    # Очистить строку
    def clr_row_train(self):
        index = self.gui.tableWidgetTrain.currentIndex().row()
        self.gui.tableWidgetTrain.removeRow(index)
        self.gui.tableWidgetTrain.insertRow(index)

    # Удалить выделенную строку
    def del_row_train(self):
        self.gui.tableWidgetTrain.removeRow(self.gui.tableWidgetTrain.currentIndex().row())

    # Очистить таблицу
    def clr_alt_train(self):
        self.gui.tableWidgetTrain.clear()
        self.gui.tableWidgetTrain.setRowCount(0)
        self.gui.tableWidgetTrain.setHorizontalHeaderLabels(self.gui.headers_train)

    # Функция добавления числа скрытых нейроннов в список
    def hidden_layers_count(self):
        self.gui.tableWidgetLayersNetwork.setRowCount(3)
        item = QTableWidgetItem(str(6))
        item.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
        self.gui.tableWidgetLayersNetwork.setItem(0, 0, item)
        item2 = QTableWidgetItem(str(self.gui.spboxHiddenLayers.value()))
        item2.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
        self.gui.tableWidgetLayersNetwork.setItem(1, 0, item2)
        item3 = QTableWidgetItem(str(1))
        item3.setFlags(Qt.ItemIsEnabled)  # Запрет редактирования ячейки
        self.gui.tableWidgetLayersNetwork.setItem(2, 0, item3)

    # Загрузка данных из текстового файла в таблицу с данными для обучения
    def load_txt_train(self):
        path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Текстовые файлы (*.txt)")[0]

        data_txt = []  # Список, в котором хранятся данные из файла

        if path != "":
            f = open(path)  # Открываем файл с данными
            for line in f.readlines():  # Построчно считываем файл
                # Добавляем в список строку из файла в виде кортежа ([входные_даннные], результат)
                data_txt.append(line.replace("\n", "").split(" "))

            # Количество строк в таблице
            row_count = self.gui.tableWidgetTrain.rowCount() - 1

            # Установка числа строк таблицы
            self.gui.tableWidgetTrain.setRowCount(row_count + len(data_txt) - 1)

            # Заполнение таблицы
            for i in range(len(data_txt)):
                for j in range(7):
                    self.gui.tableWidgetTrain.setItem(row_count + i, j, QTableWidgetItem(str(data_txt[i][j])))

    # Функция чтения CSV файла
    @staticmethod
    def csv_reader(file_obj):
        reader = csv.reader(file_obj)

        data_csv = []  # Список, в котором хранятся данные из CSV файла

        for row in reader:
            data_csv.append(" ".join(row).split(';'))

        return data_csv  # Возвращаем список с данными

    # Функция записи информации в CSV
    @staticmethod
    def csv_writer(data, path):
        with open(path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerow(line)

    # Загрузка CSV файла в таблицу с данными для обучения
    def load_csv_train(self):
        # Диалог выбора файла
        csv_path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Файды Excel (*.csv)")[0]

        if csv_path != "":
            # Читаем CSV файл
            with open(csv_path, 'r', newline='') as f_obj:

                data_csv = self.csv_reader(f_obj)

                # Количество строк в таблице
                row_count = self.gui.tableWidgetTrain.rowCount()

                # Установка числа строк таблицы
                self.gui.tableWidgetTrain.setRowCount(row_count + len(data_csv))

                # Заполнение таблицы
                for i in range(len(data_csv)):
                    for j in range(self.gui.tableWidgetTrain.columnCount()):
                        self.gui.tableWidgetTrain.setItem(row_count + i, j, QTableWidgetItem(str(data_csv[i][j])))

    # Изменение кривизны функции
    def slope(self):
        self.gui.lblSlopeValue.setText(str(self.gui.sliderSlope.value() / 1000))
        return int(self.gui.sliderSlope.value()) / 1000

    # Функция создания нейронной сети и ее графа
    def create_nn(self):
        row_count = self.gui.tableWidgetLayersNetwork.rowCount()

        for item in range(0, row_count):
            try:
                it = int(self.gui.tableWidgetLayersNetwork.item(item, 0).text())
                self.lay.append(it)
            except Exception:
                create_error_msg = QMessageBox()
                create_error_msg.setIcon(QMessageBox.Critical)
                create_error_msg.setWindowTitle("Ошибка создания сети")
                create_error_msg.setText("Таблица слоев пустая!")
                create_error_msg.exec()

        # Проверяем число слоев
        if len(self.lay) != 0:
            # Рисуем граф
            gn = GraphNeural.Graph(self.lay)
            self.gui.graphicsView.setScene(gn.g_scene())
            self.gui.graphicsView.setRenderHint(QPainter.Antialiasing)

            learning_rate = self.gui.txtLearningRate.text()  # Считываем из поля скорость обучения нейронной сети

            if learning_rate == '':
                create_error_msg = QMessageBox()
                create_error_msg.setIcon(QMessageBox.Critical)
                create_error_msg.setWindowTitle("Ошибка создания сети")
                create_error_msg.setText("Скорость обучения сети не может быть пустым значением!")
                create_error_msg.exec()
            else:
                # Создаем экземпляр класса нейронной сети
                self.network = NeuralNetwork.NN(slope=self.slope(),
                                                hidden_neurons=self.lay[1],
                                                learning_rate=float(learning_rate))

        # Очищаем список слоев с нейронами
        self.lay.clear()

    # Функция обучения нейронной сети
    def train_nn(self):
        global value_error  # Ошибка преобразования

        data = []  # Список, в котором хранятся данные из таблицы с данными для обучения
        lines = []  # Список в котором хранятся строки из таблицы с данными для обучения
        line = ''  # Строка таблицы

        # Считываем таблицу в список строк
        for i in range(self.gui.tableWidgetTrain.rowCount()):
            for j in range(self.gui.tableWidgetTrain.columnCount()):
                line += self.gui.tableWidgetTrain.item(i, j).text() + ' '
            lines.append(line.strip())
            line = ''

        value_error = False

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
            value_error = True

        # Количество строк обучающего множества
        train_set = self.gui.tableWidgetTrain.rowCount() / 100 * float(self.gui.txtLearningSet.text())

        # Количество строк тестового множества
        test_set = self.gui.tableWidgetTrain.rowCount() / 100 * float(self.gui.txtTestSet.text())

        # Считываем количество эпох
        epochs = self.gui.txtEpochs.text()

        if value_error is not True:
            if epochs == '' or train_set == '' or test_set == '' or self.gui.tableWidgetTrain.rowCount() == 0:
                train_error_msg = QMessageBox()
                train_error_msg.setIcon(QMessageBox.Critical)
                train_error_msg.setWindowTitle("Ошибка обучения сети")
                train_error_msg.setText("Количество эпох обучения или количество строк обучающего или "
                                        "тестового набора сети не может быть пустым значением "
                                        "или таблица с данными для обучения пустая!")
                train_error_msg.exec()
            else:
                # Создаем поля для вывода прогресса обучения, ошибки и тип множества
                self.gui.lblStatusTrain = QtWidgets.QLabel(self.gui.statusbar)
                self.gui.lblStatusTrain.setObjectName("lblStatusTrain")
                self.gui.lblStatusTrain.setText("Прогресс обучения:")
                self.gui.lblStatusTrainLoss = QtWidgets.QLabel(self.gui.statusbar)
                self.gui.lblStatusTrainLoss.setObjectName("lblStatusTrainLoss")
                self.gui.lblTrainSet = QtWidgets.QLabel(self.gui.statusbar)
                self.gui.lblTrainSet.setObjectName("lblTrainSet")
                self.gui.lblAccuracyNN = QtWidgets.QLabel(self.gui.statusbar)
                self.gui.lblAccuracyNN.setObjectName("lblAccuracyNN")

                # Создаем progress bar
                self.gui.prgBarTrain = QProgressBar(self.gui.statusbar)

                # Удаление виджетов из status bar
                for i in range(3, 8, 1):
                    if self.gui.statusbar.childAt(2, i) is not None:
                        self.gui.statusbar.removeWidget(self.gui.statusbar.childAt(2, i))

                self.gui.lblTrainSet.setText("Обучающее множество")
                self.gui.statusbar.addWidget(self.gui.lblTrainSet)
                self.gui.statusbar.addWidget(self.gui.lblStatusTrain)
                self.gui.statusbar.addWidget(self.gui.prgBarTrain)

                if int(train_set) > self.gui.tableWidgetTrain.rowCount() or \
                        int(test_set) > self.gui.tableWidgetTrain.rowCount() \
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
                    for i in range(self.gui.tableWidgetTrain.rowCount()):
                        for j in range(7):
                            self.gui.tableWidgetTrain.item(i, j).setBackground(Qt.white)

                    # Обучающее множество
                    for i in range(0, int(train_set)):
                        for j in range(7):
                            self.gui.tableWidgetTrain.item(i, j).setBackground(Qt.green)

                    # Тестовое множество
                    for i in range(int(train_set), int(end)):
                        for j in range(7):
                            self.gui.tableWidgetTrain.item(i, j).setBackground(Qt.yellow)

                    # Создаем списки для построения графиков
                    t_x = [i for i in range(0, int(epochs))]  # Список X
                    tr_y = []  # Список Y обучающего множества
                    tst_y = []  # Список Y тестового множества

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
                            self.gui.lblStatusTrainLoss.setText("Ошибка обучения: {}"
                                                                .format(str(round(train_loss, 7))))
                            # Заполнение списка с координатами Y
                            tr_y.append(train_loss)

                            # Значение progress bar
                            value = int(100 * (e + 1) / float(epochs))

                            self.gui.prgBarTrain.setValue(value)

                        self.gui.statusbar.addWidget(self.gui.lblStatusTrainLoss)

                        # Обучение на тестовом множестве
                        self.gui.lblTrainSet.setText("Тестовое множество")
                        train_loss = None
                        row_count_train = int(train_set)
                        row_count_test = int(test_set) + int(train_set)

                        for e in range(int(epochs)):
                            inputs_ = []
                            correct_predictions = []
                            for input_stat, correct_predict in data[row_count_train:row_count_test]:
                                self.network.train(np.array(input_stat), correct_predict)
                                inputs_.append(np.array(input_stat))
                                correct_predictions.append(np.array(correct_predict))

                            train_loss = self.network.mse(self.network.predict(np.array(inputs_).T),
                                                          np.array(correct_predictions))

                            # Заполнение списка с координатами Y
                            tst_y.append(train_loss)

                            # Значение progress bar
                            value = int(100 * (e + 1) / float(epochs))

                            # Установка значения прогрессбара
                            self.gui.prgBarTrain.setValue(value)

                        self.gui.lblStatusTrainLoss.setText(self.gui.lblStatusTrainLoss.text() + ", "
                                                            + str(round(train_loss, 7)))

                        i = 0  # Переменная для подсчета точности нейронной сети

                        for input_stat, correct_predict in data[row_count_test:]:
                            a = correct_predict == 1
                            b = self.network.predict(np.array(input_stat)) > .5
                            if (a and b) or (not a and not b):
                                i = i + 1

                        self.gui.lblAccuracyNN.setText("Точность нейронной сети: {}%".format(
                                                       str(round(i / (len(data[row_count_test:])) * 100, 1))))

                        self.gui.statusbar.addWidget(self.gui.lblAccuracyNN)

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
                        plt.plot(t_x, tr_y, label='Обучающее множество')
                        plt.subplot(212)
                        # Рисуем график для тестового множества
                        plt.plot(t_x, tst_y, label='Тестовое множество')
                        plt.legend()  # Показываем легенду
                        plt.grid(True)  # Показываем сетку
                        plt.show()  # Показываем график
                    except Exception:
                        train_error_msg = QMessageBox()
                        train_error_msg.setIcon(QMessageBox.Critical)
                        train_error_msg.setWindowTitle("Ошибка сети")
                        train_error_msg.setText("Обучение или построение графиков невозможно!")
                        train_error_msg.exec()

    # Функция для определения коэффициентов модели Чессера
    def ratio(self, line):
        # Получаем значения ячеек в переменные
        cash = self.gui.tableWidgetInput.item(line, 0).text()
        quick_sell = self.gui.tableWidgetInput.item(line, 1).text()
        total_assets = self.gui.tableWidgetInput.item(line, 2).text()
        net_sales = self.gui.tableWidgetInput.item(line, 3).text()
        gross_income = self.gui.tableWidgetInput.item(line, 4).text()
        total_debt = self.gui.tableWidgetInput.item(line, 5).text()
        main_capital = self.gui.tableWidgetInput.item(line, 6).text()
        net_assets = self.gui.tableWidgetInput.item(line, 7).text()
        work_capital = self.gui.tableWidgetInput.item(line, 8).text()

        # Рассчет коэффициентов модели Чессера
        x1 = (float(cash) + float(quick_sell)) / float(total_assets)
        x2 = float(net_sales) / (float(cash) + float(quick_sell))
        x3 = float(gross_income) / float(total_assets)
        x4 = float(total_debt) / float(total_assets)
        x5 = float(main_capital) / float(net_assets)
        x6 = float(work_capital) / float(net_sales)

        # Возвращаем список с коэфициентами модели Чессера
        return [x1, x2, x3, x4, x5, x6]

    # Функция предсказания, где mode_line - режим предсказания для строчки с соответствующим номером,
    def predict_nn(self, mode_line):
        if self.network is not None and self.gui.tableWidgetInput.rowCount() != 0:

            if mode_line:
                for line in range(self.gui.tableWidgetInput.rowCount()):
                    # Предсказываем кредитоспособность предприятия
                    if self.network.predict(np.array(self.ratio(line))) > .5:
                        result = "Кредитоспособно"
                    else:
                        result = "Некредитоспособно"

                    # Выводим результат
                    self.gui.tableWidgetInput.setItem(line, 9, QTableWidgetItem(result))
            else:
                # Индекс выделенной строки
                row = self.gui.tableWidgetTrain.currentIndex().row() + 1

                # Предсказываем кредитоспособность предприятия
                if self.network.predict(np.array(self.ratio(row))) > .5:
                    result = "Кредитоспособно"
                else:
                    result = "Некредитоспособно"

                # Выводим результат
                self.gui.tableWidgetInput.setItem(row, 9, QTableWidgetItem(result))
        else:
            predict_error_msg = QMessageBox()
            predict_error_msg.setIcon(QMessageBox.Critical)
            predict_error_msg.setWindowTitle("Ошибка предсказания")
            predict_error_msg.setText("Сеть не создана или нет данных для предсказания!")
            predict_error_msg.exec()

    # Функция для чтения файла конфигурации
    @staticmethod
    def get_config(path):
        config = cp.ConfigParser()
        config.read(path)
        return config

    # Функция для получения настроек из файла конфигурации
    @staticmethod
    def get_setting(path, section, setting):
        config = Main.get_config(path)
        value = config.get(section, setting)
        return value

    # Функция сохранения состояния нейронной сети
    def save_nn(self):
        if self.network is not None:
            path = QFileDialog.getSaveFileName(None, 'Выберите файл', 'c:\\', "Файлы конфигурации (*.ini)")[0]

            if path != "":
                # Сохраняем веса в переменные
                weights1 = self.network.get_weights()[0]
                weights2 = self.network.get_weights()[1]

                # Создаем файл конфигурации с сохранением параметров обучения сети
                config = cp.ConfigParser()
                config.add_section("Settings")
                config.set("Settings", "hidden_neurons", self.gui.tableWidgetLayersNetwork.item(1, 0).text())
                config.set("Settings", "slope", str(self.slope()))
                config.set("Settings", "learning_set", self.gui.txtLearningSet.text())
                config.set("Settings", "test_set", self.gui.txtTestSet.text())
                config.set("Settings", "epochs", self.gui.txtEpochs.text())
                config.set("Settings", "learning_rate", self.gui.txtLearningRate.text())
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

    # Загрузка весов нейронной сети
    def load_nn(self):
        # Получаем название выбранного файла
        path = QFileDialog.getOpenFileName(None, 'Выберите файл', 'c:\\', "Файлы конфигурации (*.ini)")[0]

        if path != "":
            # Получение значений из файла конфигурации
            hidden_neurons = Main.get_setting(path, "Settings", "hidden_neurons")
            slope = Main.get_setting(path, "Settings", "slope")
            learning_set = Main.get_setting(path, "Settings", "learning_set")
            test_set = Main.get_setting(path, "Settings", "test_set")
            epochs = Main.get_setting(path, "Settings", "epochs")
            learning_rate = Main.get_setting(path, "Settings", "learning_rate")

            # Количество весов
            weights1_count = 6 * int(hidden_neurons)
            weights2_count = int(hidden_neurons)

            items = []  # Список элементов из файла конфигурации

            # Считываем значения весов из файла конфигурации
            for item in range(weights1_count):
                items.append(float(Main.get_setting(path, "Weights", "weights_input_{}".format(str(item)))))

            # Разбиваем список считанных значений из файла конфигураций на списки
            weights1 = [items[d:d + 6] for d in range(0, len(items), 6)]

            # Очищаем список элементов
            items.clear()

            # Считываем значения весов из файла конфигурации
            for item in range(weights2_count):
                items.append(float(Main.get_setting(path, "Weights", "weights_output_{}".format(str(item)))))

            # Разбиваем список считанных значений из файла конфигураций на списки
            weights2 = [items[d:d + int(weights2_count)] for d in range(0, len(items), int(weights2_count))]

            # Установка значений из файла конфигурации
            self.gui.tableWidgetLayersNetwork.setRowCount(3)
            self.gui.tableWidgetLayersNetwork.setItem(0, 0, QTableWidgetItem("6"))
            self.gui.tableWidgetLayersNetwork.setItem(1, 0, QTableWidgetItem(hidden_neurons))
            self.gui.tableWidgetLayersNetwork.setItem(2, 0, QTableWidgetItem("1"))
            self.gui.spboxHiddenLayers.setValue(int(hidden_neurons))
            self.gui.sliderSlope.setValue(int(float(slope) * 1000))
            self.gui.lblSlopeValue.setText(slope)
            self.gui.txtLearningSet.setText(learning_set)
            self.gui.txtTestSet.setText(test_set)
            self.gui.txtEpochs.setText(epochs)
            self.gui.txtLearningRate.setText(learning_rate)

            # Список слоев
            layer = []

            # Заполнение списка слоев
            for row in range(self.gui.tableWidgetLayersNetwork.rowCount()):
                layer.append(int(self.gui.tableWidgetLayersNetwork.item(row, 0).text()))

            # Отрисовка графа нейронной сети
            gn = GraphNeural.Graph(layer)
            self.gui.graphicsView.setScene(gn.g_scene())
            self.gui.graphicsView.setRenderHint(QPainter.Antialiasing)

            # Создаем экземпляр класса нейронной сети
            self.network = NeuralNetwork.NN(slope=float(slope),
                                            hidden_neurons=layer[1],
                                            learning_rate=float(learning_rate))

            # Установка новых весов сети
            self.network.set_weights(weights1, weights2)

    # Вызов окна о программе
    def abt(self):
        self.about = About.About()
        self.about.setWindowFlags(Qt.Window | Qt.MSWindowsFixedSizeDialogHint)
        self.about.show()

    # Инициализация класса
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        # Установка ui
        self.gui = MainUi.MainUi()
        self.gui.setupUi(self)

        # Сигнал на закрытие окна программы
        self.gui.actionExit.triggered.connect(exit)

        # Сигнал на добавление строки
        self.gui.add_row_alt.triggered.connect(self.add_row)
        # Сигнал на очистку строки
        self.gui.clear_row_alt.triggered.connect(self.clr_row)
        # Сигнал на удаление строки
        self.gui.del_row_alt.triggered.connect(self.del_row)
        # Сигнал на очистку таблицы
        self.gui.clear_alt.triggered.connect(self.clr_alt)
        # Сигнал на cохранение таблицы
        self.gui.save_alt.triggered.connect(self.sv_alt)
        # Сигнал на показ результата для строки
        self.gui.result_alt.triggered.connect(self.rslt_alt)
        # Сигнал на показ результата для таблицы
        self.gui.result_all_alt.triggered.connect(self.rslt_all_alt)

        # Сигнал на добавление строки
        self.gui.add_row_alt_train.triggered.connect(self.add_row_train)
        # Сигнал на очистку строки
        self.gui.clear_row_alt_train.triggered.connect(self.clr_row_train)
        # Сигнал на удаление строки
        self.gui.del_row_alt_train.triggered.connect(self.del_row_train)
        # Сигнал на очистку таблицы
        self.gui.clear_alt_train.triggered.connect(self.clr_alt_train)

        # Обработка spinBox
        self.gui.spboxHiddenLayers.valueChanged.connect(self.hidden_layers_count)

        # Сигнал на загрузку TXT файла в таблицу с данными для обучения
        self.gui.actionLoadTxtTrain.triggered.connect(self.load_txt_train)
        # Сигнал на загрузку CSV файла в таблицу с данными для обучения
        self.gui.actionLoadCSVTrain.triggered.connect(self.load_csv_train)

        # Сигнал изменения положения слайдера
        self.gui.sliderSlope.valueChanged.connect(self.slope)

        # Обработка нажатия кнопки создания нейронной сети
        self.gui.btnCreateNetwork.clicked.connect(self.create_nn)

        # Обработка нажатия кнопки обучения нейронной сети
        self.gui.btnTrain.clicked.connect(self.train_nn)

        # Cигнал на сохранения нейронной сети
        self.gui.actionNetworkSave.triggered.connect(self.save_nn)

        # Cигнал на загрузку нейронной сети
        self.gui.actionNetworkLoad.triggered.connect(self.load_nn)

        # Сигнал на открытие окна "О программе"
        self.gui.actionAbout.triggered.connect(self.abt)

    # Переопределяем события изменения размера формы
    def resizeEvent(self, event):
        self.resized.emit()
        # Если размер вкладки меньше необходимого, то задаем размер graphicsView необходимые значения
        if self.gui.tabGraph.width() < 1280 and self.gui.tabGraph.height() < 650:
            self.gui.graphicsView.setGeometry(QtCore.QRect(0, 0, 1280, 650))
        # Иначе задаем размер graphicsView по размеру вкладки
        elif self.gui.tabGraph.width() >= 1280 and self.gui.tabGraph.height() >= 650:
            self.gui.graphicsView.setGeometry(QtCore.QRect(0, 0, self.gui.tabGraph.width(), self.gui.tabGraph.height()))
        return super(Main, self).resizeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Создаем объект класса Main
    m = Main()
    # Устанавливаем минимальную ширину и высоту окна
    m.setMinimumHeight(720)
    m.setMinimumWidth(1280)
    # Показываем окно
    m.show()
    sys.exit(app.exec_())
