def cipher(message, key):
    dictionary = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя., '
    print("Алфавит -'", dictionary, "'")
    result = ''
    for i in message:
            result += dictionary[(dictionary.index(i) + key) % len(dictionary)]
    return result

print("Выберите действие:\n1. Зашифровать сообщение\n2. Расшифровать сообщение")
deistv = int(input())
match deistv:
    case 1:
        msg = input("Введите сообщение ")
        number = int(input("Введите сдвиг "))
        encrypted_msg = cipher(msg, number)
        print('Зашифрованное сообщение: "' + encrypted_msg + '"\nРасшифровать данное сообщение?')
        d2 = input()
        if (d2.lower() == "да"):
            decrypted_msg = cipher(encrypted_msg, -number)
            print('Расшифрованное сообщение: "' + decrypted_msg + '"')
    case 2:
        msg = input("Введите сообщение ")
        number = int(input("Введите сдвиг "))
        encrypted_msg = cipher(msg, -number)
        print('Расшифрованное сообщение: "' + encrypted_msg + '"') 
