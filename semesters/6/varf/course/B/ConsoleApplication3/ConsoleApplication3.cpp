// Курсовая работа
// Выполнил ст.гр.УИС - 311 Зубков Сергей 
// Вариант 15

#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <iomanip>
#include <vector>
#include <thread>
#include <windows.h>
#include <algorithm>

using namespace std;
using namespace chrono;

struct FileStats {
    string filename;
    int sentenceCount;
    system_clock::time_point startTime;
    system_clock::time_point endTime;
    double durationMs;
};

int countSentences(const string& text) {
    return count_if(text.begin(), text.end(), [](char c) {
        return c == '.' || c == '!' || c == '?';
        });
}

string formatTime(const system_clock::time_point& tp) {
    time_t time = system_clock::to_time_t(tp);
    tm local_tm;
    localtime_s(&local_tm, &time);
    char buffer[100];
    strftime(buffer, sizeof(buffer), "%H:%M:%S", &local_tm);
    return string(buffer);
}

DWORD WINAPI processFileThread(LPVOID lpParam) {
    FileStats* stats = (FileStats*)lpParam;
    stats->startTime = system_clock::now();

    ifstream inputFile(stats->filename);
    if (!inputFile) {
        cerr << "Ошибка: не удалось открыть файл " << stats->filename << endl;
        return 1;
    }

    string outputFilename = stats->filename;
    size_t dotPos = outputFilename.rfind('.');
    if (dotPos != string::npos) {
        outputFilename = outputFilename.substr(0, dotPos) + "_out.txt";
    }
    else {
        outputFilename += "_out.txt";
    }

    ofstream outputFile(outputFilename);
    if (!outputFile) {
        cerr << "Ошибка: не удалось создать файл " << outputFilename << endl;
        return 1;
    }

    string line;
    int totalSentences = 0;
    while (getline(inputFile, line)) {
        totalSentences += countSentences(line);
    }

    stats->endTime = system_clock::now();
    stats->sentenceCount = totalSentences;
    stats->durationMs = duration<double, milli>(stats->endTime - stats->startTime).count();

    outputFile << "Количество предложений: " << totalSentences << endl;

    cout << "Файл: " << stats->filename << endl;
    cout << "  Предложений: " << stats->sentenceCount << endl;
    cout << "  Время начала:    " << formatTime(stats->startTime) << endl;
    cout << "  Время окончания: " << formatTime(stats->endTime) << endl;
    cout << "  Длительность:    " << fixed << setprecision(3) << stats->durationMs << " мс\n\n";

    return 0;
}

int main(int argc, char* argv[]) {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    if (argc < 2) {
        cerr << "Использование: " << argv[0] << " <файл1> <файл2> ..." << endl;
        return 1;
    }

    auto totalStart = high_resolution_clock::now();

    vector<HANDLE> threads;
    vector<FileStats> stats(argc - 1);

    for (int i = 1; i < argc; ++i) {
        stats[i - 1].filename = argv[i];
        HANDLE hThread = CreateThread(nullptr, 0, processFileThread, &stats[i - 1], 0, nullptr);
        if (hThread) {
            threads.push_back(hThread);
        }
        else {
            cerr << "Ошибка при создании потока для файла " << argv[i] << endl;
        }
    }

    WaitForMultipleObjects(threads.size(), threads.data(), TRUE, INFINITE);
    for (HANDLE h : threads) CloseHandle(h);

    auto totalEnd = high_resolution_clock::now();
    cout << "Общее время обработки: " << duration<double>(totalEnd - totalStart).count() << " секунд.\n";

    return 0;
}
