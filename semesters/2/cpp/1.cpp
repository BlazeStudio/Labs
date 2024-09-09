//Код с использованием класса (C++)
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
//Код с использованием структуры (C++) 
#include <iostream> 
#include <string> 
using namespace std; 
struct Money { 
    long roubles; 
    unsigned char copecks; 
    float wholeSum; 
    Money() { roubles = 0; copecks = 0; } 
    Money(double x, double y) { 
        this->roubles = roubles; 
        this->copecks = copecks; 
    } 
    void SplitUp(){ 
        roubles = (int)wholeSum; 
        copecks = (int)((wholeSum - (int)wholeSum) * 100);}; 
 
    void Init(long r, unsigned char k) { 
        if (k >= 100) { 
            cout << "Неверное значение копеек." << endl; 
            exit(1); 
        } 
        roubles = r; 
        copecks = k; 
    } 
 
    void Init(const string& s) { 
        long r = stol(s.substr(0, s.find('.'))); 
        unsigned char k = stoi(s.substr(s.find('.') + 1)); 
        Init(r, k); 
    } 
 
    void Init(const Money& m) { 
        roubles = m.roubles; 
        copecks = m.copecks; 
    } 
 
    void Read() 
    { 
        cout << "Введите количество рублей : "; 
        cin >> roubles; 
        cout << "Введите количество копеек : "; 
        cin >> copecks; 
        if (copecks >= 100) { 
            cout << "Ошибка! Число копеек не должно превышать 100 \n"; 
            Read(); 
        } 
    } 
    void Display() 
    { 
        if (int(copecks) < 10) 
            cout << roubles << ",0" << static_cast<int>(copecks) << " руб." "\n"; 
        else 
            cout << roubles << "," << static_cast<int>(copecks) << " руб." "\n"; 
    } 
    string toString() { 
        if (int(copecks) < 10) 
            return "(" + to_string(roubles) + ",0" + to_string(copecks) + " руб.)\n"; 
        else 
            return "(" + to_string(roubles) + "," + to_string(copecks) + " руб.)\n"; 
    } 
 
    void Summa(Money x, Money y) 
    { 
        roubles = x.roubles + y.roubles; 
        copecks = x.copecks + y.copecks; 
        if (copecks >= 100) { copecks -= 100; roubles++; } 
    } 
    void Raznost(Money x, Money y) 
    { 
        if (x.roubles < y.roubles) { cout << "Ошибка! Второе число больше первого."; exit; } 
        roubles = x.roubles - y.roubles; 
        if (int(x.copecks - y.copecks) < 0) { copecks = 100 + (x.copecks - y.copecks); roubles--; } 
        else copecks = x.copecks - y.copecks; 
    } 
     
    void Delenie(Money x, Money y, Money x2, Money y2) { 
        double chislo1 = (x.roubles * 100 + x.copecks) + (y.roubles * 100 + y.copecks); 
        double chislo2 = (x2.roubles * 100 + x2.copecks) + (y2.roubles * 100 + y2.copecks); 
        wholeSum = (chislo1 / chislo2); 
    } 
 
    void Delenie_na_drob(Money x, Money y) { 
        double chislo1 = (x.roubles * 100 + x.copecks) + (y.roubles * 100 + y.copecks); 
        double drob; 
        cout << "Введите дробь - "; 
        cin >> drob; 
        wholeSum = (chislo1 / drob) / 100; 
    } 
 
    void Umnozh_na_drob(Money x, Money y) { 
        double chislo1 = (x.roubles * 100 + x.copecks) + (y.roubles * 100 + y.copecks); 
        double drob; 
        cout << "Введите дробь - "; 
        cin >> drob; 
        wholeSum = (chislo1 * drob) / 100;; 
    } 
 
    void Sravnenie(Money x, Money y, Money x2, Money y2) { 
        double chislo1 = (x.roubles * 100 + x.copecks) + (y.roubles * 100 + y.copecks); 
        double chislo2 = (x2.roubles * 100 + x2.copecks) + (y2.roubles * 100 + y2.copecks); 
        if (chislo1 > chislo2) cout << (chislo1 / 100) << " руб. > " << (chislo2 / 100) << " руб.\n"; 
        else if (chislo1 < chislo2) cout << (chislo1 / 100) << " руб. < " << (chislo2 / 100) << " руб.\n"; 
        else  cout << (chislo1 / 100) << " руб. = " << (chislo2 / 100) << " руб.\n"; 
    } 
 
}; 
 
Money make_mun(long r, unsigned char k) { 
    Money m(r, k); 
    return m; 
} 
 
int main() 
{ 
    Money number1, number2, number3, number4, deistvie; 
    int variant; 
    while (true) { 
        system("cls"); 
        setlocale(0, "Russian"); 
        number1.Init(12, 14); cout << "ПЕРВОЕ ЧИСЛО - "; number1.Display(); 
        number2.Init(5, 06); cout << "ВТОРОЕ ЧИСЛО - "; number2.Display(); 
        number3.Init(1, 64); cout << "ТРЕТЬЕ ЧИСЛО - "; number3.Display(); 
        number4.Init(0, 78); cout << "ЧЕТВЁРТОЕ ЧИСЛО - "; number4.Display(); 
        std::cout << "\nВыберите вариант\n" << std::endl; 
        std::cout << "1. Сумма\n" 
            << "2. Разность\n" 
            << "3. Деление суммы на дробь\n" 
            << "4. Умножение суммы на дробь\n" << "5. Деление сумм\n" << "6. Сравнение\n--------------------------" << std::endl; 
        std::cout << ">>> "; 
        std::cin >> variant; 
 
        switch (variant) { 
        case 1: 
            deistvie.Summa(number1, number2); 
            std::cout << "СУММА - "; 
            deistvie.Display(); 
            system("pause"); 
            break; 
        case 2: 
            deistvie.Raznost(number1, number2); 
            std::cout << "РАЗНОСТЬ - "; 
            deistvie.Display(); 
            system("pause"); 
            break; 
        case 3: 
            deistvie.Delenie_na_drob(number1, number2); 
            deistvie.SplitUp(); 
            cout << "Результат деления суммы на дробь - "; 
            deistvie.Display(); 
            system("pause"); 
            break; 
        case 4: 
            deistvie.Umnozh_na_drob(number1, number2); 
            deistvie.SplitUp(); 
            cout << "Результат умножения суммы на дробь - "; 
            deistvie.Display(); 
            system("pause"); 
            break; 
        case 5: 
            deistvie.Delenie(number1, number2, number3, number4); 
            deistvie.SplitUp(); 
            cout << "Результат деления сумм - "; 
            deistvie.Display(); 
            system("pause"); 
            break; 
        case 6: 
            deistvie.Sravnenie(number1, number2, number3, number4); 
            system("pause"); 
            break; 
        default: 
            std::cerr << "Вы выбрали неверный вариант" << std::endl; 
            exit(EXIT_FAILURE); 
        } 
    }} 