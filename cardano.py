import numpy as np

#Ключ пока известен
testKey = np.array([
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1]
], int)

#Тестовый словарь
words = {'собрание', 'хлеб', 'делегат', 'полиция', 'слово', 'вход'}

#Поворачиваем сетку на 90 градусов
def rotateCW(key):
    newKey = np.array(range(size**2), int).reshape(size, size)
    for i in range(size):
        k = 0
        for j in range(-1, 0-(size+1), -1):
            newKey[i,k] = key[j][i]
            k += 1
    return newKey

def rotateCCW(key):
    newKey = np.array(range(size**2), int).reshape(size, size)
    for i in range(size):
        k = 0
        for j in range(size):
            newKey[i,k] = key[j][-1-i]
            k += 1
    return newKey

#Расшифровка при знании ключа
def decrypt(text, key, rotate):
    decrypted = ''
    encryptedText = ''
    for i in text:
        encryptedText += i
    usedKey = key
    for i in range(4):
        for j in range(size**2):
            if usedKey.flatten()[j] == 1:
                decrypted += encryptedText[j]
        if rotate == "CW":
            usedKey = rotateCW(usedKey)
        elif rotate == "CCW":
            usedKey = rotateCCW(usedKey)
    return decrypted

#Прибавление 1 к двоичному числу
def plusOne(key, index):
    newKey = list(key)
    Return = ''
    if newKey[index] == '0':
        newKey[index] = '1'
        for i in newKey:
            Return += i
        return Return
    else:
        newKey[index] = '0'
        return plusOne(newKey, index-1)

def convert_list(key):
    newKey = np.array(int)
    for i in range(size):
            newKey.append([])
    for i in range(size):
        for j in range(size):
            newKey[i].append(int(key[size*i + j]))
    return newKey

def convert_str(key):
    newKey = ''
    for i in key:
        for j in i:
            newKey += str(j)
    return newKey

def hack(text, start):
    key = start
    while key != '1'*(size**2//4) + '0'*(size**2//4*3):
        if key.count('1') != size**2//4:
            key = plusOne(key, -1)
            continue
        key = convert_list(key)
        for attempt in range(4):
            for i in ('CW', 'CCW'):
                decrypted = decrypt(text, key, i)
                counter = 0
                for word in words:
                    if word in decrypted:
                        counter += 1
                if counter > 2:
                    return (decrypted, key)
            key = rotateCW(key)
        key = plusOne(convert_str(key), -1)

if __name__ == '__main__':
    encrypted = []

    size = int(input('Введите количество строк:\n'))
    for i in range(size):
        while True:
            string = input('Введите ' + str(i+1) + ' строку:\n')
            if len(string) == size:
                encrypted.append(string.lower())
                break
            else:
                print('Введено неверное количество символов')

    print(decrypt(encrypted, testKey, 'CW'))