#Ключ пока известен
from ast import Return


key = [
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1]
]

#Поворачиваем сетку на 90 градусов
def rotateCW(key):
    newKey = []
    for i in range(len(key[0])):
        newKey.append([])
    for i in range(len(key[0])):
        for j in range(-1, 0-(len(key[0])+1), -1):
            newKey[i].append(key[j][i])
    return newKey

def rotateCCW(key):
    newKey = []
    for i in range(len(key[0])):
        newKey.append([])
    for i in range(len(key[0])):
        for j in range(len(key[0])):
            newKey[i].append(key[j][-1-i])
    return newKey

#Расшифровка при знании ключа
def decrypt(text, key, rotate):
    decrypted = ''
    usedKey = key
    for i in range(4):
        for i in range(len(text)):
            for j in range(len(text[i])):
                if usedKey[i][j]:
                    decrypted += text[i][j]
        if rotate == "CW":
            usedKey = rotateCW(usedKey)
        elif rotate == "CCW":
            usedKey = rotateCCW(usedKey)
    return decrypted

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

#def hack(text, start):
    

if __name__ == "__main__":
    encrypted = []

    size = int(input('Введите количество строк:\n'))
    for i in range(size):
        while True:
            string = input('Введите ' + str(i+1) + " строку:\n")
            if len(string) == size:
                encrypted.append(string.lower())
                break
            else:
                print("Введено неверное количество символов")

    print(decrypt(encrypted, key, "CW"))