#include <iostream> 

#include <string> 

using namespace std; 

 

class Money { 

private: 

    long roubles; 

    unsigned char copecks; 

public: 

    Money() : roubles(0), copecks(0) {} // конструктор без аргументов 

    Money(long r, unsigned char k) : roubles(r), copecks(k) {} // конструктор инициализации 

    Money(const Money& m) : roubles(m.roubles), copecks(m.copecks) {} // конструктор копирования 

 

    void Init(long r, unsigned char k) { // установка суммы 

        roubles = r; 

        copecks = k; 

    } 

    void Read() 

    { 

        cout << endl << "Введите количество рублей: "; 

        cin >> roubles; 

        cout << endl << "Введите количество копеек: "; 

        cin >> copecks; 

    } 

    void Display() const { 

        cout << roubles << "." << (int)copecks << " руб." << endl; 

    } 

 

    string toString() { 

        if (int(copecks) < 10) 

            return to_string(roubles) + ",0" + to_string(copecks) + " руб."; 

        else 

            return to_string(roubles) + "," + to_string(copecks) + " руб."; 

    } 

 

    Money operator+(const Money& m) const { 

        Money sum; 

        sum.roubles = roubles + m.roubles; 

        sum.copecks = copecks + m.copecks; 

        if (sum.copecks >= 100) { // если копейки больше 100, переводим в рубли 

            sum.roubles += sum.copecks / 100; 

            sum.copecks %= 100; 

        } 

        return sum; 

    } 

 

    Money operator-(const Money& m) const {  

        Money diff; 

        diff.roubles = roubles - m.roubles; 

        diff.copecks = copecks - m.copecks; 

        if (diff.copecks < 0) { // если копейки меньше 0, занимаем из рублей 

            diff.roubles -= 1; 

            diff.copecks += 100; 

        } 

        return diff; 

    } 

 

    Money operator/(const Money& m) const { 

        Money result; 

        double sum1 = roubles + (double)copecks / 100; 

        double sum2 = m.roubles + (double)m.copecks / 100; 

        double res = sum1 / sum2; 

        result.roubles = (long)res; 

        result.copecks = (res - result.roubles) * 100; 

        return result; 

    } 

 

    Money operator/(double x) const { 

        Money result; 

        double sum = roubles + (double)copecks / 100; 

        double res = sum / x; 

        result.roubles = (long)res; 

        result.copecks = (res - result.roubles) * 100; 

        return result; 

    } 

 

    Money operator*(double x) const { 

        Money result; 

        double sum = roubles + (double)copecks / 100; 

        double res = sum * x; 

        result.roubles = (long)res; 

        result.copecks = (res - result.roubles) * 100; 

        return result; 

    } 

 

    bool operator==(const Money& m) const { 

        return roubles == m.roubles && copecks == m.copecks; 

    } 

}; 

 

int main() { 

    setlocale(LC_ALL, "Russian"); 

    Money m1, m2(50, 30), m3(m2); // различные способы создания объектов 

    m1.Init(100, 50); 

    cout << "ПЕРВОЕ ЧИСЛО - "; m1.Display(); // вывод денежной суммы 

    cout << "ВТОРОЕ ЧИСЛО - "; m2.Display(); 

    cout << "ТРЕТЬЕ ЧИСЛО - "; m3.Display(); 

    Money m4 = m1 + m2; cout << "\nСУММА ПЕРВОГО И ВТОРОГО - "; m4.Display(); 

    Money m5 = m1 - m2; cout << "\nРАЗНОСТЬ ПЕРВОГО И ВТОРОГО - "; m5.Display(); 

    Money m6 = m1 / m2; cout << "\nДЕЛЕНИЕ НА СУММУ - "; m6.Display(); 

    Money m7 = m1 / 2.5; cout << "\nДЕЛЕНИЕ НА ДРОБЬ - ";m7.Display(); 

    Money m8 = m1 * 2.5; cout << "\nУМНОЖЕНИЕ НА ДРОБЬ - "; m8.Display(); 

    bool eq = m2 == m3; // операция сравнения 

    cout << "\nВторое" << (eq ? " = " : " != ") << "Третье" << endl; 

 

    return 0; 

} 