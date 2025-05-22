// Программа A: Однопоточная обработка текстов (подсчет предложений)
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>
#include <sstream>
#include <iomanip>
#include <windows.h>

using namespace std;

struct FileStats {
    string filename;
    chrono::system_clock::time_point startTime;
    chrono::system_clock::time_point endTime;
    int sentenceCount = 0;
    double durationMs = 0.0;
};

bool isSentenceEnd(char ch) {
    return ch == '.' || ch == '!' || ch == '?';
}

string formatTime(const chrono::system_clock::time_point& tp) {
    time_t timeT = chrono::system_clock::to_time_t(tp);
    tm localTm;
    localtime_s(&localTm, &timeT);
    auto ms = chrono::duration_cast<chrono::milliseconds>(tp.time_since_epoch()) % 1000;

    ostringstream oss;
    oss << put_time(&localTm, "%H:%M:%S") << '.' << setfill('0') << setw(3) << ms.count();
    return oss.str();
}

void processFile(const string& filename, FileStats& stats) {
    stats.filename = filename;
    ifstream inputFile(filename);
    if (!inputFile) {
        cerr << "Ошибка: не удалось открыть файл " << filename << endl;
        return;
    }

    string baseName = filename.substr(0, filename.find_last_of('.'));
    string outputFilename = baseName + "_out.txt";
    ofstream outputFile(outputFilename);
    if (!outputFile) {
        cerr << "Ошибка: не удалось создать файл " << outputFilename << endl;
        return;
    }

    stats.startTime = chrono::system_clock::now();
    auto start = chrono::high_resolution_clock::now();

    string line;
    while (getline(inputFile, line)) {
        int count = count_if(line.begin(), line.end(), isSentenceEnd);
        stats.sentenceCount += count;
    }

    auto end = chrono::high_resolution_clock::now();
    stats.endTime = chrono::system_clock::now();
    stats.durationMs = chrono::duration<double, milli>(end - start).count();

    outputFile << "Количество предложений: " << stats.sentenceCount << endl;
}

int main(int argc, char* argv[]) {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    if (argc < 2 || argc > 11) {
        cerr << "Использование: " << argv[0] << " <файл1> <файл2> ... (до 10 файлов)" << endl;
        return 1;
    }

    vector<string> filenames;
    set<string> seen;
    for (int i = 1; i < argc; ++i) {
        if (seen.count(argv[i])) {
            cerr << "Повторяющийся файл: " << argv[i] << endl;
            return 1;
        }
        ifstream f(argv[i]);
        if (!f) {
            cerr << "Файл не найден: " << argv[i] << endl;
            return 1;
        }
        filenames.push_back(argv[i]);
        seen.insert(argv[i]);
    }

    auto totalStart = chrono::high_resolution_clock::now();
    vector<FileStats> statsList;

    for (const string& filename : filenames) {
        FileStats stats;
        processFile(filename, stats);
        statsList.push_back(stats);
    }

    auto totalEnd = chrono::high_resolution_clock::now();
    double totalDuration = chrono::duration<double, milli>(totalEnd - totalStart).count();

    cout << "\nРезультаты обработки:\n";
    for (const auto& stats : statsList) {
        cout << "Файл: " << stats.filename << endl;
        cout << "  Предложений: " << stats.sentenceCount << endl;
        cout << "  Время начала:    " << formatTime(stats.startTime) << endl;
        cout << "  Время окончания: " << formatTime(stats.endTime) << endl;
        cout << "  Длительность:    " << fixed << setprecision(3) << stats.durationMs << " мс\n\n";
    }

    cout << "Общее время обработки: " << fixed << setprecision(3) << totalDuration << " мс" << endl;
    return 0;
}
