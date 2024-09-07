@echo off
rem Командный файл для ассемблирования, компиляции, линковки и отладки EXE программ
rem Программист: XXXXXXX

rem Удаление старых файлов объекта и исполняемого файла, если они существуют
if exist "%1.obj" del "%1.obj"
if exist "%1.exe" del "%1.exe"

rem Ассемблирование программы
c:\masm32\bin\ml /c /coff /Sn /Fl"%1.lst" "%1.asm"
if errorlevel 1 goto errasm

rem Линковка программы
c:\masm32\bin\PoLink /SUBSYSTEM:WINDOWS "%1.obj"
if errorlevel 1 goto errlink

rem Показ файлов, связанных с программой
dir "%1.*"

rem Запуск отладчика
c:\odbg\ollydbg "%1.exe"
goto TheEnd

:errlink
echo _
echo Link error
goto TheEnd

:errasm
echo _
echo Assembly Error
goto TheEnd

:TheEnd
