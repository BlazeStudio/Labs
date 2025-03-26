.686
.model flat, stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

.data
    buffer db MAX_PATH dup(0)  ; ����� ��� �������� ���� � �������� Windows
    successMsg db "������� Windows: ", 0
    errorMsg db "������ ��� ��������� ���� � �������� Windows.", 0
    unknownErrorMsg db "����������� ������. ��� ������: ", 0
    errorCode dd 0

.code
start:
    ; ����� ������� GetWindowsDirectoryA
    invoke GetWindowsDirectoryA, addr buffer, MAX_PATH

    ; �������� ����������
    cmp eax, 0
    je error

    ; �������� ����������
    invoke MessageBoxA, 0, addr buffer, addr successMsg, MB_OK
    jmp exit

error:
    ; ��������� ���� ������
    invoke GetLastError
    mov errorCode, eax

    ; ����� ��������� �� ������
    cmp errorCode, ERROR_BAD_LENGTH
    je bad_length_error

    ; ����������� ������
    invoke MessageBoxA, 0, addr unknownErrorMsg, addr errorMsg, MB_OK
    jmp exit

bad_length_error:
    ; ������: �������� ����� ������
    invoke MessageBoxA, 0, addr errorMsg, addr errorMsg, MB_OK

exit:
    ; ���������� ���������
    invoke ExitProcess, 0

end start