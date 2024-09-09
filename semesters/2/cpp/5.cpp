//Код «без спецификации исключений»  (C++)

#include <iostream> 

using namespace  std; 

 

int TimeToSeconds(int hours, int minutes) { 

    if (hours < 0 || minutes < 0) { 

        cout << "Неверный формат времени!" << endl; 

    } 

    return hours * 3600 + minutes * 60; 

} 

 

int main() { 

    setlocale(LC_ALL, "Russian"); 

    int result = TimeToSeconds(-1, 20); 

    cout << "Время в секундах = " << result << endl; 

} 


//Код «со спецификацией throw» (C++) 

 

#include <iostream> 

 

using namespace  std; 

 

int TimeToSeconds(int hours, int minutes) throw() { 

    if (hours < 0 || minutes < 0) { 

        throw "Неверный формат времени!"; 

    } 

    return hours * 3600 + minutes * 60; 

} 

 

int main() { 

    int result; 

    setlocale(LC_ALL, "Russian"); 

    try { 

        result = TimeToSeconds(-1, 20); 

    } 

    catch (const char* message) { 

        cerr << message << endl; 

        return 0; 

    } 

    cout << "Время в секундах = " << result << endl; 

} 


//Код «с конкретной спецификацией с подходящим стандартным исключением»  (C++) 

 

#include <iostream> 

 

using namespace  std; 

 

int TimeToSeconds(int hours, int minutes) { 

    if (hours < 0 || minutes < 0) { 

        throw runtime_error("Неверный формат времени!"); 

    } 

    return hours * 3600 + minutes * 60; 

} 

 

int main() { 

    int result; 

    setlocale(LC_ALL, "Russian"); 

    try { 

        result = TimeToSeconds(-1, 20); 

    } 

    catch (exception& e) { 

        cerr << e.what() << endl; 

        return 0; 

    } 

    cout << "Время в секундах = " << result << endl; 

}  



//Код «с спецификацией с собственным реализованным исключением» (C++) 

#include <iostream> 

 

using namespace std; 

 

class EmptyException {}; 

 

// Класс-исключение с полями-параметрами функции 

class ParamException { 

public: 

    ParamException(int h, int m) : hours(h), minutes(m) {} 

    int hours; 

    int minutes; 

}; 

 

// Наследник стандартного класса исключения 

class TimeFormatException : public std::runtime_error { 

public: 

    TimeFormatException(const std::string& message) : std::runtime_error(message) {} 

}; 

 

// Функция, переводящая часы и минуты в секунды 

int TimeToSeconds(int hours, int minutes) { 

    if (hours < 0 || minutes < 0) { 

        // Выброс пустого исключения 

        throw EmptyException(); 

    } 

    if (hours == 0 && minutes == 0) { 

        // Выброс исключения с параметрами 

        throw ParamException(hours, minutes); 

    } 

    if (hours > 24) { 

        // Выброс исключения-наследника стандартного класса исключения 

        throw TimeFormatException("Некорректный формат времени: часы должны быть меньше или равны 23."); 

    } 

    return (hours * 3600) + (minutes * 60); 

} 

 

int main() { 

    setlocale(LC_ALL, "Russian"); 

    int result; 

    try { 

        result = TimeToSeconds(0, 0); 

        std::cout << "Это составляет " << result << " секунд." << std::endl; 

    } 

    catch (EmptyException e) { 

        std::cout << "Неверный ввод. Пожалуйста, введите корректные данные." << std::endl; 

    } 

    catch (ParamException e) { 

        std::cout << "Неверный ввод. Введены нулевые значения." << std::endl; 

    } 

    catch (TimeFormatException e) { 

        cerr << e.what() << endl; 

    } 

    return 0; 

}