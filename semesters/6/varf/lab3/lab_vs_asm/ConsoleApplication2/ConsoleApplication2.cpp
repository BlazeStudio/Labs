#include <windows.h>
#include <conio.h>
#include <iostream>
#include <vector>
#include <thread>
#include <string>
#include <iomanip>
#include <chrono>

using namespace std;
using namespace chrono;

string sharedString = "ABCDE";
string backupString = "ABCDE";
int delay = 0;

CRITICAL_SECTION cs;

struct LogEntry {
    char key;
    DWORD threadID;
    system_clock::time_point startTime;
    system_clock::time_point critEntryTime;
    system_clock::time_point endTime;
    string sharedState;
    string backupState;
};
vector<LogEntry> logEntries;

string formatTimeWithMillis(system_clock::time_point tp) {
    auto ms = duration_cast<milliseconds>(tp.time_since_epoch()) % 1000;
    time_t rawTime = system_clock::to_time_t(tp);
    struct tm timeInfo;
    localtime_s(&timeInfo, &rawTime);
    char buffer[20];
    strftime(buffer, sizeof(buffer), "%H:%M:%S", &timeInfo);
    return string(buffer) + "." + to_string(ms.count());
}

void ModifyChar(int index) {
    auto startTime = system_clock::now();
    cout << "Поток " << index + 1 << " создан; ID= " << this_thread::get_id() << endl;

    EnterCriticalSection(&cs);
    auto critEntryTime = system_clock::now();
    cout << "[!!!] Поток " << this_thread::get_id() << " вошёл в критический участок в " << formatTimeWithMillis(critEntryTime) << endl;

    this_thread::sleep_for(milliseconds(delay));
    sharedString[index] = ' ';
    backupString[index] = ' '; // Теперь изменяется в критическом участке

    LeaveCriticalSection(&cs);
    auto endTime = system_clock::now();

    cout << "Поток " << index + 1 << " завершен" << endl;
    logEntries.push_back({ static_cast<char>('1' + index), GetCurrentThreadId(), startTime, critEntryTime, endTime, sharedString, backupString });
}

void RestoreChar(int index) {
    auto startTime = system_clock::now();
    cout << "Поток " << index + 1 << " создан; ID= " << this_thread::get_id() << endl;

    EnterCriticalSection(&cs);
    auto critEntryTime = system_clock::now();
    cout << "[!!!] Поток " << this_thread::get_id() << " вошёл в критический участок в " << formatTimeWithMillis(critEntryTime) << endl;

    this_thread::sleep_for(milliseconds(delay));
    sharedString[index] = "ABCDE"[index];
    backupString[index] = "ABCDE"[index]; // Теперь изменяется в критическом участке

    LeaveCriticalSection(&cs);
    auto endTime = system_clock::now();

    cout << "Поток " << index + 1 << " завершен" << endl;
    logEntries.push_back({ static_cast<char>('F' + index), GetCurrentThreadId(), startTime, critEntryTime, endTime, sharedString, backupString });
}

int main(int argc, char* argv[]) {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    if (argc > 1) delay = atoi(argv[1]);

    InitializeCriticalSection(&cs);

    cout << "Начальная строка: " << sharedString << endl;

    while (true) {
        int key = _getch();
        if (key >= '1' && key <= '5') {
            int index = key - '0' - 1;
            thread(ModifyChar, index).detach();
        }
        else if (key == 0) {
            key = _getch();
            if (key >= 59 && key <= 63) {
                int index = key - 59;
                thread(RestoreChar, index).detach();
            }
        }
        else if (key == 27) {
            break;
        }
    }

    cout << "\nЖурнал операций:" << endl;
    cout << "Клавиша | Поток  | Время начала   | Крит. вход  | Время окончания | Строка | Дублер" << endl;
    for (const auto& entry : logEntries) {
        cout << "  " << entry.key << "  | " << entry.threadID << " | "
            << formatTimeWithMillis(entry.startTime) << " | " << formatTimeWithMillis(entry.critEntryTime) << " | "
            << formatTimeWithMillis(entry.endTime) << " | "
            << entry.sharedState << " | " << entry.backupState << endl;
    }

    DeleteCriticalSection(&cs);
    return 0;
}
