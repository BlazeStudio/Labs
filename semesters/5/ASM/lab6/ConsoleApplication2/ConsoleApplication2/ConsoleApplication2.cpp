#include <iostream>
#include <ctime>
#include <windows.h>
#include <iomanip>
#include <stack>
using namespace std;

// ASM обработка одного элемента
extern "C" long processElement(long value);

// Основная функция расчета среднего значения
long calculateAverageWithComplexCalculations(long inputarray[], int inputsize) {
    long sum = 0; // Используем long для предотвращения переполнения
    long array_elem = 0;
    for (int i = 0; i < inputsize; ++i) {
        array_elem = inputarray[i];
        long result = processElement(array_elem); // Вызов функции для обработки элемента
        //cout << result << endl;
        sum += result; // добавляем результат в общую сумму
    }

    return sum; // возвращаем среднее значение
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    stack<std::string> stack;
    const int ARRAY_SIZE = 100;

    long array[ARRAY_SIZE]; // Массив теперь с long вместо int
    srand(time(nullptr));

    for (int i = 0; i < ARRAY_SIZE; ++i) {
        array[i] = 25;
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
    cout << "stack size: " << stack.size() << std::endl;
    long averageAsm = calculateAverageWithComplexCalculations(array, ARRAY_SIZE);
    clock_t end = clock();

    double duration = static_cast<double>(end - start) / CLOCKS_PER_SEC;

    cout << "Результат расчёта: " << averageAsm << endl;
    cout << "Время выполнения программы: " << fixed << setprecision(3) << duration << " секунд" << endl;

    return 0;
}
