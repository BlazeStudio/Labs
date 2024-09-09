alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя., '
alphabet1 = 'КЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯклмнопрстуфхцчшщъыьэюя., АБВГДЕЁЖЗИЙабвгдеёжзий'
alphabet2 = 'УФХЦЧШЩЪЫуфхцчшщъы., КЛМНОПРСТЬЭЮЯАБВГДЕЁЖЗИЙклмнопрстьэюяабвгдеёжзий'
alphabet3 = 'РСТЬЭЮЯАБВрстьэюяабв., УФХЦГДЕЁЖЗИЙЧШЩЪЫКЛМНОПуфхцгдеёжзийчшщъыклмноп'
alphabet4 = 'УПлкмЯьпМФОЮюяШтЛошЧцРнЩЫТНКЭущЬХЪысЦэфъСхрч., ЁЙёезиЗАИгйГЕВвбБжаЖДд'
alphabet5 = 'шШыхЩЦуУЪфцФъЧщчЫХ., едЕвЭКРЖпМБАкняДиэЁотьрСИмжбзОНЗТЬсагёГЛПйВЯЮюлЙ'
alphabet6 = 'юТРАВьэЮтвсЬарЭСЯБяб., нЙзЦжгЫДщшФуоЪехЁЩмНъпУКОыкЕчХфПдёЗШйЛцИиЧЖГлМ'
alphabet7 = 'НШтмЯХърьщЫпюсхЦЭЬПшяСоТЩфчЪМУРнуЧцЮФкЛлэКОы., зБДдиГбЗегйвёИжЙВАЁаЕЖ'
alphabet8 = 'чЧШушЦЫщЩфхХФЪцъыУ., бвРпЗОнДьБЭЖТмСсйагдкКПМИЮзтиеЕНВАёжюоЛляЯЙЁГЬрэ'
alphabet9 = 'аьСсВТвРэюяЮтЯЬБрАЭб., МзъщЪОфейИШЫЖоУЦЕПГЧкуДЛимЁёХхНжЗдшнплЙыКчгцЩФ'
kontur1 = [alphabet1, alphabet2, alphabet3]
kontur2 = [alphabet4, alphabet5, alphabet6]
kontur3 = [alphabet7, alphabet8, alphabet9]
def cryp(message, key):
    print("Исходный - ", alphabet)
    print("КОНТУР 1\nАлфавит1 - ", alphabet1, "\nАлфавит2 - ", alphabet2, "\nАлфавит3 - ", alphabet3, "\n")
    print("КОНТУР 2\nАлфавит4 - ", alphabet4, "\nАлфавит5 - ", alphabet5, "\nАлфавит6 - ", alphabet6, "\n")
    print("КОНТУР 3\nАлфавит7 - ", alphabet7, "\nАлфавит8 - ", alphabet8, "\nАлфавит9 - ", alphabet9, "\n")
    num, countr = 0, 0
    result = ''
    k1, k2 = True, True
    for i in message:
        if ((((key - (key % 100)) // 100) * 3 != countr) and k1 == True):
            result += kontur1[num % 3][alphabet.index(i)]
            num += 1
            countr += 1
            if (((key - (key % 100)) // 100) * 3 == countr): k1, countr = False, 0
        elif ((((key % 100 - (key % 10)) // 10) * 3 != countr) and k2 == True):
            result += kontur2[num % 3][alphabet.index(i)]
            num += 1
            countr += 1
            if ((((key % 100 - (key % 10)) // 10) * 3 == countr)): k2, countr = False, 0
        elif ((key % 10) * 3 != countr):
            result += kontur3[num % 3][alphabet.index(i)]
            num += 1
            countr += 1
            if ((key % 10) * 3 == countr): k1, k2, countr = True, True, 0
    return result
def encryp(message, key):
    print("Исходный - ", alphabet)
    print("КОНТУР 1\nАлфавит1 - ", alphabet1, "\nАлфавит2 - ", alphabet2, "\nАлфавит3 - ", alphabet3, "\n")
    print("КОНТУР 2\nАлфавит4 - ", alphabet4, "\nАлфавит5 - ", alphabet5, "\nАлфавит6 - ", alphabet6, "\n")
    print("КОНТУР 3\nАлфавит7 - ", alphabet7, "\nАлфавит8 - ", alphabet8, "\nАлфавит9 - ", alphabet9, "\n")
    num, countr = 0, 0
    result = ''
    k1, k2 = True, True
    for i in message:
        if ((((key - (key % 100)) // 100) * 3 != countr) and k1 == True):
            result += alphabet[kontur1[num % 3].index(i)]
            num += 1
            countr += 1
            if (((key - (key % 100)) // 100) * 3 == countr): k1, countr = False, 0
        elif ((((key % 100 - (key % 10)) // 10) * 3 != countr) and k2 == True):
            result += alphabet[kontur2[num % 3].index(i)]
            num += 1
            countr += 1
            if ((((key % 100 - (key % 10)) // 10) * 3 == countr)): k2, countr = False, 0
        elif ((key % 10) * 3 != countr):
            result += alphabet[kontur3[num % 3].index(i)]
            num += 1
            countr += 1
            if ((key % 10) * 3 == countr): k1, k2, countr = True, True, 0
    return result
print("Выберите действие:\n1. Зашифровать сообщение\n2. Расшифровать сообщение")
deistv = int(input())

match deistv:
    case 1:
        msg = input("Введите сообщение ")
        key = int(input("Введите ключ "))
        encrypted_msg = cryp(msg, key)
        print('Зашифрованное сообщение: "' + encrypted_msg + '"\nРасшифровать данное сообщение?')
        d2 = input()
        if (d2.lower() == "да"):
            decrypted_msg = encryp(encrypted_msg, key)
            print('Расшифрованное сообщение: "' + decrypted_msg + '"')
    case 2:
        msg = input("Введите сообщение ")
        key = int(input("Введите ключ "))
        encrypted_msg = encryp(msg, key)
        print('Расшифрованное сообщение: "' + encrypted_msg + '"') 
