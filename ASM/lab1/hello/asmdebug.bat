@echo off
rem ��������� ���� ��� ���������������, ����������, �������� � ������� EXE ��������
rem �����������: XXXXXXX

rem �������� ������ ������ ������� � ������������ �����, ���� ��� ����������
if exist "%1.obj" del "%1.obj"
if exist "%1.exe" del "%1.exe"

rem ��������������� ���������
c:\masm32\bin\ml /c /coff /Sn /Fl"%1.lst" "%1.asm"
if errorlevel 1 goto errasm

rem �������� ���������
c:\masm32\bin\PoLink /SUBSYSTEM:WINDOWS "%1.obj"
if errorlevel 1 goto errlink

rem ����� ������, ��������� � ����������
dir "%1.*"

rem ������ ���������
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
