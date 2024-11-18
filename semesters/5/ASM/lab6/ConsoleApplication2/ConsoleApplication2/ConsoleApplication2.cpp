#include <iostream>
#include <ctime>
#include <windows.h>
#include <iomanip>
#include <cmath>
#include <stdexcept>
#include <cstdlib>

using namespace std;

int processElement(int value) {
    if (value == 0) {
        throw std::invalid_argument("Division by zero is not allowed.");
    }

    int result = value; // Начальное значение
    const int iterations = 100000;

    for (int i = 0; i < iterations; ++i) {
        result = (pow(result, 2)) / value;               // Первый квадрат и деление
        result = (result * 2) / value;                   // Умножение на 2 и деление
        result = (pow(result, 2)) / value;              // Второй квадрат и деление
        result = (result + value) / 2;                   // Среднее арифметическое
        result = (result + abs(result - value)) / 2; // Учитываем модуль разности
        result = static_cast<int>(fmod(result, value));       // Остаток от деления
    }

    return result;
}




extern "C" long processElement(long value);


long calculateAverageWithComplexCalculations(long inputarray[], int inputsize) {
    long sum = 0;
    long array_elem = 0;
    for (int i = 0; i < inputsize; ++i) {
        array_elem = inputarray[i];
        long result = processElement(array_elem);
        //cout << result << endl;
        sum += result;
    }

    return sum;
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    const int ARRAY_SIZE = 1000;

    long array[ARRAY_SIZE]; // Массив теперь с long вместо int
    srand(time(nullptr));

    for (int i = 0; i < ARRAY_SIZE; ++i) {
        array[i] = 1337;
    }

    cout << "Исходный массив:" << endl;
    for (int i = 0; i < 20; ++i) {
        cout << array[i] << " ";
    }
    cout << endl;

    clock_t start = clock();
    if (array == nullptr) {
        cout << "Ошибка: массив пустой!" << endl;
        return -1;
    }
    long averageAsm = calculateAverageWithComplexCalculations(array, ARRAY_SIZE);
    clock_t end = clock();

    double duration = static_cast<double>(end - start) / CLOCKS_PER_SEC;

    cout << "Результат расчёта: " << averageAsm << endl;
    cout << "Время выполнения программы: " << fixed << setprecision(3) << duration << " секунд" << endl;

    return 0;
}
