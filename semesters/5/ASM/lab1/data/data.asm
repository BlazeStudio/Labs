;������������ ������ �1
;�������� ��. ��. XXXXXXXX
;��������� 2 (DATA.ASM) ������� �1
;============================================================
.486
.model flat, stdcall ;��������������� ��� ������������ ������ ������
option casemap: none
;============================================================
.stack 100h ;������������ ������� ����� �������� 256 ����
;============================================================
;����������� ����������� �������
include c:\masm32\include\windows.inc
include c:\masm32\include\user32.inc
include c:\masm32\include\kernel32.inc
includelib c:\masm32\lib\user32.lib
includelib c:\masm32\lib\kernel32.lib
;============================================================
.data ;������ �������� ������
A1 db 27 ;����������� ������������ ����������
A2 dw 0AE5h ;����������� ������������ ���������� (�����)
A3 dd 123456h ;����������� �������� ����� (4 �����)
A4 db -2 ;����������� ������������� ����� �� ������
A5 dd A4 ;����������� ���������������� ��������� �� ���������� A4
;============================================================
.code ;������ �������� ����
main: ;�����, ������������ ����� ����� � ���������
mov bl, A1 ;��������� � ������� BL �������� ���������� A1
mov bh, A4-2 ;��������� � ������� BH ���� ������ � ������� A4-2
mov ecx, offset A2 ;��������� � ������� ECX ����� ���������� A2
mov ax, A2 ;��������� � ������� AX �������� ���������� A2
mov si, A2+1 ;��������� � ������� SI ����� ������ �� ������ A2+1
invoke ExitProcess,0 ;����� ������� ���������� ���������
end main ;����� ��������� 
