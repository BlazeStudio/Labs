#include <iostream> 
#include <string> 
using namespace std; 
 
class Pair { 
private: 
    int x, y; 
 
public: 
    // Конструктор по умолчанию 
    Pair() : x(0), y(0) {} 
 
    // Конструктор с параметрами 
    Pair(int a, int b) { 
        if (a >= 0 && b >= 0) { 
            x = a; 
            y = b; 
        } 
        else { 
            cout << "Ошибка! Числа должны быть неотрицательными!" << endl; 
            exit(1); 
        } 
    } 
 
    // Методы установки значений полей 
    void setX(int num) { 
        if (num >= 0) { 
            x = num; 
        } 
        else { 
            cout << "Ошибка! Число должно быть неотрицательным!" << endl; 
        } 
    } 
 
    void setY(int num) { 
        if (num >= 0) { 
            y = num; 
        } 
        else { 
            cout << "Ошибка! Число должно быть неотрицательным!" << endl; 
        } 
    } 
 
    // Методы получения значений полей 
    int getX() { 
        return x; 
    } 
 
    int getY() { 
        return y; 
    } 
 
    int Proizvidenie() { 
        return x * y; 
    } 
 
    string toString() { 
        return "(" + to_string(x) + ", " + to_string(y) + ")"; 
    } 
}; 
 
class Rectangle : public Pair { 
public: 
    // Конструктор по умолчанию 
    Rectangle() : Pair() {} 
 
    // Конструктор с параметрами 
    Rectangle(int a, int b) : Pair(a, b) {} 
 
    int getPerimeter() { 
        return 2 * (getX() + getY()); 
    } 
 
    int getPloshad() { 
        return getX() * getY(); 
    } 
 
    string toString() { 
        return "Прямоугольник со сторонами " + Pair::toString(); 
    } 
}; 
 
int main() { 
    setlocale(LC_ALL, "Russian"); 
    Pair p(6, 8); 
    Rectangle r(4, 12); 
 
    cout << "Значения полей объекта \"Пара чисел\": " << p.getX() << ", " << p.getY() << endl; 
    cout << "Произведение чисел: " << p.Proizvidenie() << endl; 
    cout << "Строковое представление объекта: " << p.toString() << endl; 
 
    cout << endl; 
 
    cout << "Значения полей объекта \"Прямоугольник\": " << r.getX() << ", " << r.getY() << endl; 
    cout << "Периметр: " << r.getPerimeter() << endl; 
    cout << "Площадь: " << r.getPloshad() << endl; 
    cout << "Строковое представление объекта: " << r.toString() << endl; 
 
    return 0; 
} 