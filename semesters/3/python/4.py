alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя., '

def cryp(message, key):
    result = ''
    k_key = []
    num = 0
    for i in key:
        new_alph = ''
        new_alph += alphabet[alphabet.index(i)]
        for g in range (alphabet.index(i) + 1, len(alphabet) + alphabet.index(i)):
            new_alph += alphabet[g % len(alphabet)]
        k_key.append(new_alph)
    print("Исходный - ", alphabet)
    for i in range (len(k_key)): print (f"Алфавит{i+1} - ".format(i), k_key[i])
    print("\n")
    for i in message:
        result += k_key[num%len(key)][alphabet.index(i)]
        num += 1

    return result

def encryp(message, key):
    result, k_key, num = '', [], 0
    for i in key:
        new_alph = ''
        new_alph += alphabet[alphabet.index(i)]
        for g in range (alphabet.index(i) + 1, len(alphabet) + alphabet.index(i)):
            new_alph += alphabet[g % len(alphabet)]
        k_key.append(new_alph)
    print("Исходный - ", alphabet)
    for i in range (len(k_key)): print (f"Алфавит{i+1} - ".format(i), k_key[i])
    print("\n")
    for i in message:
        result += alphabet[k_key[num%len(key)].index(i)]
        num += 1

    return result
print("Выберите действие:\n1. Зашифровать сообщение\n2. Расшифровать сообщение")
deistv = int(input())

match deistv:
    case 1:
        msg = input("Введите сообщение ")
        key = input("Введите ключ ")
        encrypted_msg = cryp(msg, key)
        print('Зашифрованное сообщение: "' + encrypted_msg + '"\nРасшифровать данное сообщение?')
        d2 = input()
        if (d2.lower() == "да"):
            decrypted_msg = encryp(encrypted_msg, key)
            print('Расшифрованное сообщение: "' + decrypted_msg + '"')
    case 2:
        msg = input("Введите сообщение ")
        key = input("Введите ключ ")
        encrypted_msg = encryp(msg, key)
        print('Расшифрованное сообщение: "' + encrypted_msg + '"') 
