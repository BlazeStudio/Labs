#include <iostream> 

#include <math.h> 

using namespace std; 

int i, numl; 

double x, y, d, P; 

 

void slau(double values[2][3]) { 

    double delta = values[0][0] * values[1][1] - values[0][1] * values[1][0]; 

    double delta_x1 = values[0][1] * values[1][2] - values[1][1] * values[0][2]; 

    double delta_x2 = values[0][0] * values[1][2] - values[1][0] * values[0][2]; 

    x = (delta_x1 / delta); 

    y = (delta_x2 / delta); 

} 

 

void lenght(double **dot) { 

    for (i = 0; i < numl - 1; i++) { 

        d = sqrt(pow((dot[i + 1][0] - dot[i][0]), 2) + pow((dot[i + 1][1] - dot[i][1]), 2)); 

        P += d; 

    } 

    d = sqrt(pow((dot[i][0] - dot[0][0]), 2) - pow((dot[i][1] - dot[0][1]), 2)); 

    P += d; 

} 

 

void main() { 

    setlocale(LC_CTYPE, "Russian"); 

    cout << "Введите количество линий\n"; 

    cin >> numl; 

    double *a = new double[numl]; 

    double *b = new double[numl]; 

    double *c = new double[numl]; 

    double **dot; 

    dot = new double *[numl]; 

    for (int i = 0; i < numl; i++) 

        dot[i] = new double[2]; 

    for (i = 0; i < numl; i++) { 

        cout << "Дана формула ax+by=c\nВведите a\n"; 

        cin >> a[i]; 

        cout << "Введите b\n"; 

        cin >> b[i]; 

        cout << "Введите c\n"; 

        cin >> c[i]; 

    } 

    for (i = 0; i < numl - 1; i++) { 

        double values[2][3] = { { a[i], b[i], c[i] }, { a[i + 1], b[i + 1], c[i + 1] } }; 

        slau(values); 

        dot[i][0] = x; 

        dot[i][1] = y; 

    } 

    double values[2][3] = { { a[i], b[i], c[i] }, { a[0], b[0], c[0] } }; 

    slau(values); 

    dot[i][0] = x; 

    dot[i][1] = y; 

    lenght(dot); 

    cout << "Периметр = " << P << endl;} 