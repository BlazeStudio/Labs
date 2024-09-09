#include <iostream>  

#include <vector>  

 

using namespace std; 

 

int main() { 

    setlocale(LC_CTYPE, "Russian"); 

    int size = 10, counted = 0, otriz = 0, i = 0; 

    double x2; 

    vector <double> one_vector; 

    cout << "Введите 10 чисел(Как минимум одно отрицательно)" << " \n"; 

    while (one_vector.size() != size) { 

        cin >> x2; 

        one_vector.push_back(x2); 

        if (one_vector[i] < 0)  

            otriz = 1; 

        if ((0 <= one_vector[i]) && (one_vector[i] <= 0.5) && (otriz == 0)) 

            counted++; 

        i++; 

    } 

    if (otriz == 1) 

        cout << "Ответ - " << counted << " \n"; 

    else 

        cout << "Нет отрицательного числа" << " \n"; 

}