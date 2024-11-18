.MODEL FLAT, C
.STACK 4096

.DATA
    zeroValue DWORD 0          ; Константа для проверки на ноль

.CODE
processElement PROC
    ; Входной параметр: value в регистре EAX
    ; Проверка на ноль
    cmp eax, zeroValue         ; Сравниваем значение с нулем
    je zero_case               ; Если равно нулю, переходим в zero_case

    ; Если значение не ноль, продолжаем обработку
    mov ebx, eax               ; Сохраняем значение в EBX

    mov ecx, 100000            ; Устанавливаем счетчик повторений
loop_start:
    imul eax, eax              ; Возводим EAX в квадрат
    cdq                        ; Расширяем EAX в EDX:EAX для IDIV
    idiv ebx                   ; Делим EAX на EBX

    mov edx, 0                 ; Сбрасываем EDX для следующей операции
    imul eax, 2                ; Умножаем EAX на 2
    cdq                        ; Расширяем для IDIV
    idiv ebx                   ; Делим EAX на EBX

    mov edx, 0                 ; Сбрасываем EDX
    imul eax, eax              ; Второй раз возводим в квадрат
    cdq                        ; Расширяем для IDIV
    idiv ebx                   ; Делим EAX на EBX

    add eax, ebx               ; Складываем EAX с исходным значением (EBX)
    shr eax, 1                 ; Делим на 2 (усредняем)

    ; Учитываем модуль разности
    mov edx, eax               ; Сохраняем результат в EDX
    sub edx, ebx               ; Вычисляем разность result - value
    jns skip_abs               ; Если результат положительный, пропускаем модуль
    neg edx                    ; Берём модуль (инвертируем знак)
skip_abs:
    add eax, edx               ; Складываем result с модулем разности
    shr eax, 1                 ; Делим на 2 (усредняем)

    ; Остаток от деления
    mov edx, 0                 ; Сбрасываем EDX
    div ebx                    ; Делим EAX на EBX, результат в EAX, остаток в EDX
    mov eax, edx               ; Перемещаем остаток в EAX

    ; Удалены операции с FPU для вычисления квадратного корня
    loop loop_start            ; Повторяем 100000 раз

    ret                        ; Возвращаем результат в EAX
zero_case:
    mov eax, 0                 ; Если значение было 0, возвращаем 0
    ret
processElement ENDP

END
