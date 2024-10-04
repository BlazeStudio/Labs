; Лабораторная работа №2
; Выполнил: студент группы XXX-311 XXXXXXXXXXX YYYYYYYY
; Вариант: 1234
; Функция: Y = x / 5 - 1, если x <= 30
;           Y = 3 * x - 80, если 30 < x <= 80
;           Y = 150 + x, если x > 80
.486
.model flat, stdcall
option casemap:none
.stack 100h

;=========================================
include c:\masm32\include\windows.inc
include c:\masm32\include\user32.inc
include c:\masm32\include\kernel32.inc
includelib c:\masm32\lib\user32.lib
includelib c:\masm32\lib\kernel32.lib
;=========================================
.data
x db 25         ; Входное значение X
y db ?           ; Результат Y
myerr db 0       ; Переменная для ошибки (0 - нет ошибки, 1 - ошибка)
;=========================================
.code
main:
    cmp x, 30         ; Сравниваем X с 30
    jbe calc1         ; Если X <= 30, перейти к calc1
    cmp x, 80         ; Сравниваем X с 80
    jbe calc2         ; Если 30 < X <= 80, перейти к calc2

    mov al, x         ; Загружаем X в AL
    add al, 150       ; Y = 150 + X
    jc error          ; Если есть перенос, перейти на ошибку
    jmp save_result   ; Переход к сохранению результата

;-----------------------------------------
; Вычисление Y = 3 * x - 80, если 30 < X <= 80
calc2:
    mov al, x         ; Загружаем X в AL
    mov bl, 3         ; Умножаем на 3
    mul bl            ; AL = 3 * X
    sub al, 80        ; Y = 3 * X - 80
    jc error          ; Если есть перенос, перейти на ошибку
    jmp save_result   ; Переход к сохранению результата

;-----------------------------------------
; Вычисление Y = X / 5 - 1, если X <= 30
calc1:
    mov al, x         ; Загружаем X в AL
	mov ah, 0
    mov bl, 5         ; Делим на 5
    div bl            ; AL = X / 5
    dec al            ; Y = AL - 1
    jmp save_result   ; Переход к сохранению результата

;-----------------------------------------
; Сохранение результата в Y
save_result:
    mov y, al         ; Сохраняем результат в Y
    jmp exit          ; Переход к выходу

;-----------------------------------------
; Обработка ошибки переполнения
error:
mov myerr, 1      ; Устанавливаем код ошибки

;-----------------------------------------
exit: mov al, myerr     ; Загружаем код ошибки в AL

invoke ExitProcess, al

end main
