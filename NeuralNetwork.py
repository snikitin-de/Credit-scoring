"""
Тема ВКР: "Разработка аналитической системы на основе плоскостной нейронной сети прямого распространения"
Студент: Никитин С.А., номер специальности: 230100, номер группы: 446
Руководитель проекта: к.т.н., доцент Орешков Вячеслав Игоревич
Средство разработки: PyCharm
Назначение данной части программы: предсказание кредитоспособности предприятия
Дата разработки: 21.12.2017
"""

# Импорт модуля
import numpy as np


# Класс нейронной сети
class NN:
    # Инициализация класса, в конструктор которого передается learning rate по умолчанию
    def __init__(self, slope=1, input_neurons=6, hidden_neurons=12, output_neurons=1, learning_rate=0.1):
        # Заполняем случайыми значениями веса дуг между нейронами
        self.weights_0_1 = np.random.normal(0.0, 1, (hidden_neurons, input_neurons))  # Входной слой - скрытый слой
        self.weights_1_2 = np.random.normal(0.0, 1, (output_neurons, hidden_neurons))  # Скрытый слой - выходной слой
        # Проходим по вектору и к каждому его элементу применяем функцию сигмоид
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        # Конвертируем learning rate в массив numpy
        self.learning_rate = np.array([learning_rate])
        # Кривизна сигмоиды
        self.slope = slope

    # Получение весов нейронной сети
    def get_weights(self):
        return self.weights_0_1, self.weights_1_2

    # Установка весов связей сети
    def set_weights(self, weights_1, weights_2):
        self.weights_0_1 = weights_1
        self.weights_1_2 = weights_2

    # Активационная функция
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-self.slope*x))

    # Метод предсказания нейронной сети
    def predict(self, inputs):  # inputs - массив с входными данными
        inputs_1 = np.dot(self.weights_0_1, inputs)  # Умножаем веса входного слоя - скрытого слоя на входные значения
        outputs_1 = self.sigmoid_mapper(inputs_1)  # Применяем к выходным значениям сигмоид

        # Умножаем веса скрытого слоя - выходного слоя на входные значения
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)  # Применяем к выходным значениям сигмоид
        return outputs_2  # Результат предсказания

    # Метод обучения по алгоритму обратного распространения ошибки, на вход передается массив входных значений и
    # ожидаемый прогноз
    def train(self, inputs, expected_predict):
        # Аналогично методу predict
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        actual_predict = outputs_2[0]  # Результат предсказания

        error_layer_2 = np.array([actual_predict - expected_predict])  # Рассчитываем ошибку
        gradient_layer_2 = actual_predict * (1 - actual_predict)  # Рассчитываем градиент
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2  # Рассчитываем дельту весов

        # Рассчитываем изменения весов от скрытого слоя к выходному слою
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_1.reshape(1, len(outputs_1)))) * self.learning_rate

        # Методом обратного распространения ошибки для входного - скрытого слоя делаем тоже самое, что и
        # для скрытого - выходного слоя
        error_layer_1 = weights_delta_layer_2 * self.weights_1_2
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T * self.learning_rate

    # Метод, рассчитывающий минимальное квадратичное отклонение
    def mse(self, x, y):
        return np.mean((x-y)**2)