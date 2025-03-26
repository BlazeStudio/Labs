// Лабораторная работа 2
// Васильев Антон УИС-311
// Вариант 7 
//
#include <windows.h>
#include <conio.h>
#include <iostream>
#include <vector>
#include <ctime>
#include <thread>
#include <chrono>
#include <iomanip>
#include <sstream>

using namespace std;
using namespace chrono;

char sharedString[] = "ABCDE";
char backupString[] = "ABCDE";
int delay = 0;

struct LogEntry {
    int key;
    DWORD threadID;
    system_clock::time_point startTime;
    system_clock::time_point endTime;
    string sharedState;
    string backupState;
};

vector<LogEntry> logEntries;

string formatTime(system_clock::time_point timePoint) {
    auto timeT = system_clock::to_time_t(timePoint);
    auto ms = duration_cast<milliseconds>(timePoint.time_since_epoch()) % 1000;

    struct tm timeInfo;
    localtime_s(&timeInfo, &timeT);

    stringstream ss;
    ss << put_time(&timeInfo, "%H:%M:%S") << "." << setw(3) << setfill('0') << ms.count();
    return ss.str();
}

void ModifyChar(int index) {
    auto startTime = system_clock::now();
    cout << "Поток " << index + 1 << " создан; ID= " << this_thread::get_id() << endl;

    this_thread::sleep_for(milliseconds(delay));
    sharedString[index] = ' ';

    this_thread::sleep_for(milliseconds(delay / 2));
    backupString[index] = ' ';

    auto endTime = system_clock::now();
    cout << "Поток " << index + 1 << " завершен" << endl;
    logEntries.push_back({ index + 1, GetCurrentThreadId(), startTime, endTime, sharedString, backupString });
}

void RestoreChar(int index) {
    auto startTime = system_clock::now();
    cout << "Поток " << index + 1 << " создан; ID= " << this_thread::get_id() << endl;

    this_thread::sleep_for(milliseconds(delay));
    sharedString[index] = "ABCDE"[index];

    this_thread::sleep_for(milliseconds(delay / 2));
    backupString[index] = "ABCDE"[index];

    auto endTime = system_clock::now();
    cout << "Поток " << index + 1 << " завершен" << endl;
    logEntries.push_back({ index + 6, GetCurrentThreadId(), startTime, endTime, sharedString, backupString });
}

int main(int argc, char* argv[]) {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    if (argc > 1) delay = atoi(argv[1]);

    cout << "Начальная строка: " << sharedString << endl;

    while (true) {
        int key = _getch();
        if (key >= '1' && key <= '5') {
            int index = key - '0' - 1;
            thread(ModifyChar, index).detach();
        }
        else if (key == 0) {
            key = _getch();
            if (key >= 59 && key <= 63) { // F1-F5
                int index = key - 59;
                thread(RestoreChar, index).detach();
            }
        }
        else if (key == 27) {
            break;
        }
    }

    cout << "\nЖурнал операций:" << endl;
    cout << "Клавиша | Поток  | Время начала   | Время окончания | Строка | Дублер" << endl;
    for (const auto& entry : logEntries) {
        cout << "  " << entry.key << "  | " << entry.threadID << " | "
            << formatTime(entry.startTime) << " | " << formatTime(entry.endTime) << " | "
            << entry.sharedState << " | " << entry.backupState << endl;
    }

    return 0;
}
