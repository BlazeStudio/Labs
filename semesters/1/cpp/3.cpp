#include <iostream> 
#include <string> 
#include <iomanip> 
 
using namespace std; 
 
int main() 
 
{ 
    setlocale(LC_CTYPE, "Russian"); 
    int M, A, B; 
    string line1, line2; 
    cout << "Введите длину строки" << " \n"; 
    cin >> M; 
    cout << "Введите строку" << " \n"; 
    cin >> setw(M) >> line1; 
    cout << "Введите значения A и B(A < B и B < M)" << " \n"; 
    cin >> A >> B; 
    if ((A > B) || (B > M)) { 
        cout << "Значения не соответствуют условию" << " \n"; 
        exit(0); 
    } 
    for (int i = A; i <= B; i++) 
        line2.push_back(line1[i]); 
    cout << "Ответ - " << line2 << " \n"; 
 
     
    system("pause"); 
 
}