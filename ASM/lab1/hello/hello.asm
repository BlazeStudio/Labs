;������������ ������ �1
;�������� ��. ��. ���-311 XXXXXXX
;��������� 1 (HELLO.ASM) ������� �1
.486
.model flat, stdcall ;��� ������������ ������ ������
option casemap: none
.stack 100h ;������������ ������� ����� �������� 256 ����
;����������� ����������� ��������� ������� � ���������
include c:\masm32\include\windows.inc
include c:\masm32\include\user32.inc
include c:\masm32\include\kernel32.inc
includelib c:\masm32\lib\user32.lib
includelib c:\masm32\lib\kernel32.lib
.data ;������ �������� ������
tit db '������, ���',0 ;���������� - ��������� ����
hello db'������������, � XXXXXX!',0;������������� ������
 ;��� ���������� Hello
.code ;������ �������� ����
main: ;�����, ������������ ����� ����� � ���������
push 0 ;���������� ����
push offset tit ;��������� ����
push offset hello ;����� ��� ������
push 0 ;����� ���� (0 � ���� � ������� ��)
call MessageBox ;����� ������� ������ �� �����
push 0 ;��� ����������
call ExitProcess ;��������� ������ ���������
end main