; process_element.asm
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
    imul eax, eax              ; Умножаем EAX на EAX
    cdq                        ; Расширяем EAX в EDX:EAX для IDIV
    idiv ebx                   ; EAX = EAX / EBX
    loop loop_start            ; Повторяем 100000 раз

    ret                        ; Возвращаем результат в EAX
zero_case:
    mov eax, 0                 ; Если значение было 0, возвращаем 0
    ret
processElement ENDP

END
