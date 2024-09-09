alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя., '
alphabet1 = 'КЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯклмнопрстуфхцчшщъыьэюя., АБВГДЕЁЖЗИЙабвгдеёжзий'
alphabet2 = 'УФХЦЧШЩЪЫуфхцчшщъы., КЛМНОПРСТЬЭЮЯАБВГДЕЁЖЗИЙклмнопрстьэюяабвгдеёжзий'
alphabet3 = 'РСТЬЭЮЯАБВрстьэюяабв., УФХЦГДЕЁЖЗИЙЧШЩЪЫКЛМНОПуфхцгдеёжзийчшщъыклмноп'

def cryp(message):
    print("Исходный - ", alphabet)
    print("Алфавит1 - ", alphabet1, "\nАлфавит2 - ", alphabet2, "\nАлфавит3 - ", alphabet3, "\n")
    num = 0
    result = ''
    for i in message:
        if (num % 3) == 0:
            result += alphabet1[alphabet.index(i) % len(alphabet1)]
        if (num % 3) == 1:
            result += alphabet2[alphabet.index(i) % len(alphabet2)]
        if (num % 3) == 2:
            result += alphabet3[alphabet.index(i) % len(alphabet3)]
        num += 1
    return result

def decryp(message):
    print("Исходный - ", alphabet)
    print("Алфавит1 - ", alphabet1, "\nАлфавит2 - ", alphabet2, "\nАлфавит3 - ", alphabet3, "\n")
    num = 0
    result = ''
    for i in message:
        if (num % 3) == 0:
            result += alphabet[alphabet1.index(i) % len(alphabet)]
        if (num % 3) == 1:
            result += alphabet[alphabet2.index(i) % len(alphabet)]
        if (num % 3) == 2:
            result += alphabet[alphabet3.index(i) % len(alphabet)]
        num += 1
    return result

print("Выберите действие:\n1. Зашифровать сообщение\n2. Расшифровать сообщение")
deistv = int(input())

match deistv:
    case 1:
        msg = input("Введите сообщение ")
        encrypted_msg = cryp(msg)
        print('Зашифрованное сообщение: "' + encrypted_msg + '"\nРасшифровать данное сообщение?')
        d2 = input()
        if (d2.lower() == "да"):
            decrypted_msg = decryp(encrypted_msg)
            print('Расшифрованное сообщение: "' + decrypted_msg + '"')
    case 2:
        msg = input("Введите сообщение ")
        encrypted_msg = decryp(msg)
        print('Расшифрованное сообщение: "' + encrypted_msg + '"')
