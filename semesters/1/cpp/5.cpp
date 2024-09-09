#include <iostream> 

#include <string> 

 

class Data 

{ 

    private: 

        std::string address; 

        std::string full_list[12][50]; 

 

        int offset_count, file_pick; 

        int one_offset[2] = {0, 0}, all_offset[2] = {0, 0}, no_offset[2] = {0, 0}; 

        int score; int exam1; int exam2; int exam3; int exam4; 

        int num = 0, num2 = 0, i; 

        int str_cnt = 0, count = 0; 

        int strings_summ; 

 

    public: 

        void Input_numbers(); 

        void Obrabotka(); 

        void Output(); 

        void Input_file(); 

 

}; 

#include "class.h" 

#include <fstream> 

#include <string> 

#include <iomanip> 

 

 

 

 

void Data::Input_numbers() 

{ 

if (file_pick == 1) str_cnt = 0; 

std::cout << "Введите фамилию студента\n"; 

std::cin >> full_list[num][str_cnt]; 

std::cout << "Введите вступительный балл\n"; 

std::cin >> full_list[num + 1][str_cnt]; 

std::cout << "Введите оценку за четыре экзамена (от 2 до 5)\n"; 

std::cin >> exam1 >> exam2 >> exam3 >> exam4; 

std::string exam1_c = std::to_string(exam1); std::string exam2_c = std::to_string(exam2); std::string exam3_c = std::to_string(exam3); std::string exam4_c = std::to_string(exam4); 

full_list[num + 2][str_cnt] = exam1_c; full_list[num + 3][str_cnt] = exam2_c; full_list[num + 4][str_cnt] = exam3_c; full_list[num + 5][str_cnt] = exam4_c; 

std::cout << "Введите оценку за первый, второй и третий зачет (зачет или незачет)\n"; 

std::cin >> full_list[num + 6][str_cnt]; 

while ((full_list[num + 6][str_cnt] != "зачет") && (full_list[num + 6][str_cnt] != "незачет")) { 

std::cout << "Вы ввели неверное значение. Введите зачет или незачет\n"; 

std::cin >> full_list[num + 6][str_cnt]; 

} 

std::cin >> full_list[num + 7][str_cnt]; 

while ((full_list[num + 7][str_cnt] != "зачет") && (full_list[num + 7][str_cnt] != "незачет")) { 

std::cout << "Вы ввели неверное значение. Введите зачет или незачет\n"; 

std::cin >> full_list[num + 7][str_cnt]; 

} 

std::cin >> full_list[num + 8][str_cnt]; 

while ((full_list[num + 8][str_cnt] != "зачет") && (full_list[num + 8][str_cnt] != "незачет")) { 

std::cout << "Вы ввели неверное значение. Введите зачет или незачет\n"; 

std::cin >> full_list[num + 8][str_cnt]; 

} 

std::cout << "Введите примечание (Если командирован - напишите К)\n"; 

std::cin >> full_list[num + 9][str_cnt]; 

while ((full_list[num + 9][str_cnt] != "К") && (full_list[num + 9][str_cnt] != "-")) { 

std::cout << "Вы ввели неверное значение. Введите К или -\n"; 

std::cin >> full_list[num + 9][str_cnt]; 

} 

num = 0; 

str_cnt++; 

} 

 

void Data::Output() { 

strings_summ = str_cnt; str_cnt = 0; 

std::cout << "+---+----------------+---------------+-------------------+--------------------------------+------------+\n"; 

std::cout << "| № |    Фамилия     | Вступит. балл |     Экзамены      |             Зачеты             | Примечание |\n"; 

std::cout << "+---|                |               |-------------------|--------------------------------|------------+\n"; 

std::cout << "|   |                |               | Д1 | Д2 | Д3 | Д4 |    Д1    |    Д2    |    Д3    |            |\n"; 

std::cout << "+---|----------------|---------------|-------------------|--------------------------------|------------+\n"; 

for (i = 1; i < strings_summ + 1; i++) { 

std::cout << std::left << std::setw(1) << "|" << std::setw(3) << i << "|" << std::setw(16) << full_list[num2][str_cnt] << std::setw(7) << "|"; 

std::cout << std::setw(9) << full_list[num2 + 1][str_cnt] << std::setw(3) << "|"; 

std::cout << std::setw(2) << full_list[num2 + 2][str_cnt] << std::setw(3) << "|" << std::setw(2) << full_list[num2 + 3][str_cnt] << std::setw(3) << "|" << std::setw(2) << full_list[num2 + 4][str_cnt] << std::setw(3) << "|" << std::setw(2) << full_list[num2 + 5][str_cnt] << std::setw(3) << "|"; 

std::cout << std::setw(8) << full_list[num2 + 6][str_cnt] << std::setw(3) << "|"; 

std::cout << std::setw(8) << full_list[num2 + 7][str_cnt] << std::setw(3) << "|" << std::setw(8) << full_list[num2 + 8][str_cnt] << std::setw(7) << "|" << std::setw(6) << full_list[num2 + 9][str_cnt] << "|" << "\n"; 

std::cout << "+---+----------------+---------------+----+----+----+----+----------+----------+----------+------------+\n"; 

num2 = 0; 

str_cnt++; 

} 

num2 = 0; 

} 

 

 

void Data::Obrabotka() { 

strings_summ = str_cnt; str_cnt = 0; 

for (i = 0; i < strings_summ; i++) { //(6 7 8) - зачеты (9 - примечание) 

if (full_list[count + 6][str_cnt] == "зачет") offset_count = 1; else offset_count = -1; 

if (full_list[count + 7][str_cnt] == "зачет") offset_count++; else offset_count--; 

if (full_list[count + 8][str_cnt] == "зачет") offset_count++; else offset_count--; 

if (offset_count == 3) { 

if (full_list[count + 9][str_cnt] == "К") all_offset[1] += 1; all_offset[0] += 1; 

} 

else if (offset_count == -3) { 

if (full_list[count + 9][str_cnt] == "К") no_offset[1] += 1; no_offset[0] += 1; 

} 

else if (offset_count == 1) { 

if (full_list[count + 9][str_cnt] == "К") one_offset[1] += 1; one_offset[0] += 1; 

} count = 0; str_cnt++; 

} 

std::cout << "+------------------------------------------------------------------------------------------------+\n"; 

std::cout << "|          Один незачет          |          Без зачетов          |        Сдали все зачеты       |\n"; 

std::cout << "+--------------------------------|-------------------------------|-------------------------------+\n"; 

std::cout << "|  Всего  |   Командированных    |  Всего  |   Командированных   |  Всего  |   Командированных   |\n"; 

std::cout << "+--------------------------------|-------------------------------|-------------------------------+\n"; 

std::cout << "| " << std::right << std::setw(4)  << one_offset[0] << std::setw(5) << "|" << std::setw(11) << one_offset[1] << std::setw(12) << "|" << std::setw(5) << no_offset[0] << std::setw(5) << "|" << std::setw(10) << no_offset[1] << std::setw(12) << "|" << std::setw(5) << all_offset[0] << std::setw(5) << "|" << std::setw(11) << all_offset[1] << std::setw(12) << "|\n"; 

std::cout << "+------------------------------------------------------------------------------------------------+\n"; 

} 

 

 

void Data::Input_file() { 

file_pick = 1; str_cnt = 0; 

 

std::cout << "Введите название файла с расширением - "; 

std::cin >> address; 

address += ".txt"; 

std::ifstream in(address); 

if (!in) { 

std::cout << "В каталоге программы нет файла с именем " << address << "\n"; 

} 

else { 

while (!in.eof()) { 

getline(in, full_list[num][str_cnt], '\t'); 

if (full_list[num][str_cnt] == "\n") { 

num = 0; str_cnt++;} 

else num++; 

} 

num = 0; 

std::cout << "Программа завершена" << std::endl; 

} 

system("pause"); 

}


#include "class.h" 

#include <iostream> 

 

 

int main() 

{ 

    Data _Data; 

    int variant, variant2; 

 

    while (true) { 

        system("chcp 1251"); 

        system("cls"); 

        setlocale(LC_CTYPE, "Russian"); 

        std::cout << "Выберите вариант\n" << std::endl; 

        std::cout << "1. Ввод информации\n" 

            << "2. Обработка информации\n" 

            << "3. Вывод информации\n" 

            << "4. Выход\n" << std::endl; 

        std::cout << ">>> "; 

        std::cin >> variant; 

 

        switch (variant) { 

        case 1: 

            do 

            { 

                system("cls"); 

                std::cout << "Откуда вводить исходные данные?\n" << std::endl; 

                std::cout << "1. Клавиатура\n" << "2. Файл\n" << "3. Выход\n" << std::endl; 

                std::cout << ">>> "; 

                std::cin >> variant2; 

                switch (variant2) 

                { 

                case 1: 

                    _Data.Input_numbers(); 

                    variant2 = 0; 

                    break; 

                case 2: 

                    _Data.Input_file(); 

                    variant2 = 0; 

                    break; 

                case 3: 

                    variant2 = 0; 

                default: 

                    break; 

                } 

            } while (variant2 != 0); 

            break; 

        case 2: 

            _Data.Obrabotka(); 

            system("pause"); 

            break; 

        case 3: 

            _Data.Output(); 

            system("pause"); 

            break; 

        case 4: 

            std::cout << "Выход из программы..." << std::endl; 

            exit(0); 

        } 

    } 
