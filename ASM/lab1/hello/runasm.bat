rem ��������� ���� ��� �������� � ���������� ���������
rem ����������� XXXXXXXX
@echo off
 if exist "%1.obj" del "%1.obj"
 if exist "%1.exe" del "%1.exe"
rem ���������������
c:\masm32\bin\ml /c /coff /Sn /Fl"%1.lst" "%1.asm"
 if errorlevel 1 goto errasm
rem �������������� ������
c:\masm32\bin\PoLink /SUBSYSTEM:WINDOWS "%1.obj"
 if errorlevel 1 goto errlink
 dir "%1.*"
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
rem ����������
"%1.exe"