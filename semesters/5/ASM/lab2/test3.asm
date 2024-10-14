;Лабораторная работа №2 
;Выполнил ст. гр. УXX-311 XXXXXXXXXX YYYYYYY 
;Вариант 1234 
; 220-8*x, x<30 
; y= 800/x-10, 30<=x<75 
; x+145, x>=75 
.486 
.model flat, stdcall 
option casemap: none 
.stack 100h 
;========================================= 
include <\masm32\include\kernel32.inc> 
includelib <\masm32\lib\kernel32.lib> 
;========================================= 
.data 
x db 35 
y db ? 
myerr db 0 
;========================================= 
.code 
main: 
cmp x, 30 ; х-30 ? 
jae int2 ; если x>=30 перейти к метке int2 
; вычисление 220-8*x 
mov al, 8 
mul x ; ax:=8*x 
 ; дальше учитываем, что произведение целиком находится в al 
 ; поскольку x<30 и 8*30=240<255 
mov bl, 220 
sub bl, al ; bl:=220-8*x 
jc osh ; если есть перенос - ошибка, перейти к метке osh 
mov al, bl ; результат сохраняем в al 
jmp fin ; перейти к метке fin 
;-------------------------------- 
int2: 
cmp x, 75 ; х-75 ? 
jae int3 ; если x>=75 перейти к метке int3 
; вычисление 800/x-10 
mov ax, 800 
div x ; al:=ax/x=800/x 
sub al, 10 ; al:=800/x-10 
jmp fin ; перейти к метке fin 
;-------------------------------- 
; вычисление x+145 
int3: 
mov al, x 
add al, 145 ; al:=x+145 
jnc fin ; если флаг переноса не установлен перейти к fin 
osh: mov myerr, 1 ; установить код ошибки 
jmp exit ; перейти к метке exit 
;-------------------------------- 
fin: mov y, al ; сформировать результат в переменной y 
exit: mov al, myerr ; код завершения программы 
invoke ExitProcess, al 
end main