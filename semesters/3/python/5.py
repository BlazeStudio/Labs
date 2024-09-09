def cryp(message, strok, stolb, key):
    b = []
    while key > 0:
        b.append(key % 10)
        key = key // 10
    b = b[::-1]
    result = ''
    d = 0
    matr = [[' ' for j in range(0, stolb)] for i in range(0, strok)]
    while (d != len(message)):
        for i in range(0, strok):
            for g in range(0, stolb):
                if (d == len(message)): matr[i][g] = ""
                else:
                    matr[i][g] = message[d]
                    d += 1
        for i in b: print(i, end = "  ") #Печать ключа и строк
        print("")
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in matr]))
        print("\n")
        for f in range(0, len(b)):
            for i in range(0, strok):
                result += matr[i][b.index(f+1)]
    return result
def encryp(message, strok, stolb, key):
    b = []
    while key > 0:
        b.append(key % 10)
        key = key // 10
    b = b[::-1]
    result = ''
    m = 0
    matr = [[' ' for j in range(0, stolb)] for i in range(0, strok)]
    while (m != len(message)):
        yes = len(message) - m
        for i in range(0, stolb):
            for g in range(0, strok):
                if (yes < (stolb*(g) + b.index(i+1)+1)): matr[g][b.index(i+1)] = ""
                elif (m == len(message)): matr[g][b.index(i+1)] = ""
                else:
                    matr[g][b.index(i+1)] = message[m]
                    m = m + 1
        for i in b: print(i, end = "  ") #Печать ключа и строк
        print("")
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in matr]))
        print("\n")
        for d in range(0, strok):
            for i in range(0, stolb):
                result += matr[d][i]

    return result
print("Выберите действие:\n1. Зашифровать сообщение\n2. Расшифровать сообщение")
deistv = int(input())
match deistv:
    case 1:
        msg = input("Введите сообщение ")
        strok = int(input("Введите количество строк\n"))
        stolb = int(input("Введите количество столбцов\n"))
        key = int(input("Введите ключ "))
        encrypted_msg = cryp(msg, strok, stolb, key)
        print('Зашифрованное сообщение: "' + encrypted_msg + '"\nРасшифровать данное сообщение?')
        d2 = input()
        if (d2.lower() == "да"):
            decrypted_msg = encryp(encrypted_msg, strok, stolb, key)
            print('Расшифрованное сообщение: "' + decrypted_msg + '"')
    case 2:
        msg = input("Введите сообщение ")
        strok = int(input("Введите количество строк"))
        stolb = int(input("Введите количество столбцов"))
        key = int(input("Введите ключ "))
        encrypted_msg = encryp(msg, strok, stolb, key)
        print('Расшифрованное сообщение: "' + encrypted_msg + '"')
