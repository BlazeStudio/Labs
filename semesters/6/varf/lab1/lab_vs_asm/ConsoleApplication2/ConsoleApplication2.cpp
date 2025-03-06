// Лабораторная работа 1
// Васильев Антон УИС-311 Вариант 7
//Получить имя каталога размещения ОС Windows
//UINT GetWindowsDirectory(
//    LPTSTR lpBuffer,
//    UINT uSize);
//
//lpBuffer - [out]  буфер для имени;
//uSize - [out]  длина буфера.
//Функция возвращает 0 в случае ошибки, или
//длину имени каталога в противном случае.

#include <windows.h>
#include <iostream>
#include <vector>

void PrintError(DWORD errorCode) {
    switch (errorCode) {
    case ERROR_BAD_LENGTH:
        std::cout << "Ошибка: Неверная длина буфера." << std::endl;
        break;
    case ERROR_ACCESS_DENIED:
        std::cout << "Ошибка: Доступ запрещен." << std::endl;
        break;
    case ERROR_NOT_ENOUGH_MEMORY:
        std::cout << "Ошибка: Недостаточно памяти." << std::endl;
        break;
    default:
        std::cout << "Неизвестная ошибка. Код ошибки: " << errorCode << std::endl;
        break;
    }
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    UINT bufferSize = 0;  // Начальное значение
    std::vector<char> buffer(bufferSize);

    UINT result = GetWindowsDirectoryA(buffer.data(), bufferSize);

    if (result == 0) {
        DWORD error = GetLastError();
        std::cout << "Ошибка при получении пути к каталогу Windows." << std::endl;
        PrintError(error);
        return 1;
    }

    if (result > bufferSize) {
        std::cout << "Ошибка: Размер буфера слишком мал. Требуется " << result << " байт." << std::endl;
        return 1; 
    }

    std::cout << "Каталог Windows: " << buffer.data() << std::endl;
    return 0;
}


