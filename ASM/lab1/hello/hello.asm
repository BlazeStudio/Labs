;Лабораторная работа №1
;Выполнил ст. гр. УИС-311 XXXXXXX
;Программа 1 (HELLO.ASM) Вариант №1
.486
.model flat, stdcall ;Тип используемой модели памяти
option casemap: none
.stack 100h ;Определяется сегмент стека размером 256 байт
;Подключение необходимых системных модулей и библиотек
include c:\masm32\include\windows.inc
include c:\masm32\include\user32.inc
include c:\masm32\include\kernel32.inc
includelib c:\masm32\lib\user32.lib
includelib c:\masm32\lib\kernel32.lib
.data ;Начало сегмента данных
tit db 'Привет, мир',0 ;Переменная - заголовок окна
hello db'Здравствуйте, я XXXXXX!',0;Резервируется память
 ;для переменной Hello
.code ;Начало сегмента кода
main: ;Метка, обозначающая точку входа в программу
push 0 ;Дескриптор окна
push offset tit ;Заголовок окна
push offset hello ;Текст для вывода
push 0 ;Стиль окна (0 – окно с кнопкой ОК)
call MessageBox ;Вызов функции вывода на экран
push 0 ;Код завершения
call ExitProcess ;Завершаем работу программы
end main