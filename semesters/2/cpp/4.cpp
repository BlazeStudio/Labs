#include <iostream> 
const int max_size = 100; 
using namespace std; 
 
class Array { 
public: 
    unsigned char arr[max_size]; 
    int size; 
    Array(int n, unsigned char val = 0) { 
        size = n; 
        for (int i = 0; i < size; i++) { 
            arr[i] = val; 
        } 
    } 
 
    unsigned char& operator[](int index) { 
        if (index < 0 || index >= size) { 
            cerr << "Неверный индекс" << endl; 
            exit(1); 
        } 
        return arr[index]; 
    } 
 
    virtual Array operator+(Array& other) { 
        if (size != other.size) { 
            cerr << "У класса Array другие размеры" << endl; 
            exit(1); 
        } 
 
        Array result(size); 
        for (int i = 0; i < size; i++) { 
            result[i] = arr[i] + other[i]; 
        } 
        return result; 
    } 
}; 
 
class Money : protected Array { 
private: 
    long rubles; 
    unsigned int kop; 
public: 
    Money(long r = 0, unsigned int k = 0) : Array(2) { 
        rubles = r; 
        kop = k; } 
    virtual Money operator+(const Money& other) { 
        Money result; 
        result.rubles = rubles + other.rubles; 
        result.kop = kop + other.kop; 
        if (result.kop >= 100) { 
            result.kop -= 100; 
            result.rubles++;} 
        result.arr[0] = (unsigned char)result.rubles; 
        result.arr[1] = (unsigned char)result.kop; 
        return result; 
    } 
    friend ostream& operator<<(ostream& os, const Money& m) { 
        os << m.rubles << " руб " << m.kop << " коп"; 
        return os; 
    } 
}; 
 
class BitString : protected Array { 
public: 
    BitString(int size) : Array(size) {} 
 
    BitString(const char* str) : Array(strlen(str)) { 
        for (int i = 0; i < size; i++) 
            arr[i] = (str[i] == '0' ? 0 : 1); 
    } 
 
   virtual BitString operator+(const BitString& other) { 
        BitString result(size); 
        for (int i = 0; i < size; i++) { 
            result[i] = arr[i] + other.arr[i]; 
            if (result[i] > 1) result[i] = 1; 
        } 
        return result; 
    } 
    friend ostream& operator<<( ostream& os, const BitString& bits) { 
        for (int i = 0; i < bits.size; i++) 
            os << static_cast<int>(bits.arr[i]); 
        return os; 
    } 
}; 
 
 
int main() { 
    setlocale(LC_ALL, "Russian"); 
    Array a1(5, 3); 
    Array a2(5, 5); 
    cout << "Array a1: "; 
    for (int i = 0; i < a1.size; i++) 
        cout << (int)a1[i] << " "; 
    cout <<  endl; 
    cout << "Array a2: "; 
    for (int i = 0; i < a2.size; i++) 
        cout << (int)a2[i] << " "; 
    cout <<  endl; 
    Array a3 = a1 + a2; 
    cout << "Array a3 = a1 + a2: "; 
    for (int i = 0; i < a3.size; i++) 
        cout << static_cast<int>(a3[i]) << " "; 
    cout <<  endl; 
 
    Money m1(12, 24); 
    Money m2(5, 76); 
    cout << "Money m1: " << m1 <<  endl; 
    cout << "Money m2: " << m2 <<  endl; 
    Money m3 = m1 + m2; 
    cout << "Money m3 = m1 + m2: " << m3 <<  endl; 
    BitString b1("11100"); 
    BitString b2("01010"); 
    cout << "Bit string b1: " << b1 <<  endl; 
    cout << "Bit string b2: " << b2 <<  endl; 
    BitString b3 = b1 + b2; 
    cout << "Bit string b3 = b1 + b2: " << b3 <<  endl; 
 
return 0;}