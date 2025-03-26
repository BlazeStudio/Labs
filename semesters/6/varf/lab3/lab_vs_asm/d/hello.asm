.686
.model flat, stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

.data
    buffer db MAX_PATH dup(0)  ; Буфер для хранения пути к каталогу Windows
    successMsg db "Каталог Windows: ", 0
    errorMsg db "Ошибка при получении пути к каталогу Windows.", 0
    unknownErrorMsg db "Неизвестная ошибка. Код ошибки: ", 0
    errorCode dd 0

.code
start:
    ; Вызов функции GetWindowsDirectoryA
    invoke GetWindowsDirectoryA, addr buffer, MAX_PATH

    ; Проверка результата
    cmp eax, 0
    je error

    ; Успешное выполнение
    invoke MessageBoxA, 0, addr buffer, addr successMsg, MB_OK
    jmp exit

error:
    ; Получение кода ошибки
    invoke GetLastError
    mov errorCode, eax

    ; Вывод сообщения об ошибке
    cmp errorCode, ERROR_BAD_LENGTH
    je bad_length_error

    ; Неизвестная ошибка
    invoke MessageBoxA, 0, addr unknownErrorMsg, addr errorMsg, MB_OK
    jmp exit

bad_length_error:
    ; Ошибка: Неверная длина буфера
    invoke MessageBoxA, 0, addr errorMsg, addr errorMsg, MB_OK

exit:
    ; Завершение программы
    invoke ExitProcess, 0

end start