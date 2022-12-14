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
def rotateCW(key, size):
    newKey = np.array(range(size**2), int).reshape(size, size)
    for i in range(size):
        k = 0
        for j in range(-1, 0-(size+1), -1):
            newKey[i,k] = key[j,i]
            k += 1
    return newKey

def rotateCCW(key, size):
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
        for j in range(netSize**2):
            if usedKey.flatten()[j] == 1:
                decrypted += encryptedText[j]
        if rotate == "CW":
            usedKey = rotateCW(usedKey, netSize)
        elif rotate == "CCW":
            usedKey = rotateCCW(usedKey, netSize)
    return decrypted

#Создание ключа по маске
def maskToKey(mask):
    quaters = np.zeros(netSize**2, int).reshape(4, quaterSize**2)
    for i in range(len(mask)):
        quaters[mask[i], i] = 1
    q1 = quaters[0].reshape(quaterSize, quaterSize)

    q2 = quaters[1].reshape(quaterSize, quaterSize)
    q2 = rotateCW(q2, quaterSize)

    q3 = quaters[2].reshape(quaterSize, quaterSize)
    for i in range(2):
        q3 = rotateCW(q3, quaterSize)

    q4 = quaters[3].reshape(quaterSize, quaterSize)
    for i in range(3):
        q4 = rotateCW(q4, quaterSize)

    half1 = np.concatenate((q1,q2), axis=1)
    half2 = np.concatenate((q4,q3), axis=1)
    key = np.concatenate((half1, half2))
    return key

def hack(text):
    for i in range(quantity):
        key = maskToKey(masks[i])
        for attempt in range(4):
            for i in ('CW', 'CCW'):
                decrypted = decrypt(text, key, i)
                counter = 0
                for word in words:
                    if word in decrypted:
                        counter += 1
                if counter > 2:
                    return (decrypted, key)
            key = rotateCW(key, netSize)
        

if __name__ == '__main__':
    encrypted = []

    netSize = int(input('Введите количество строк:\n'))
    quaterSize = netSize//2
    for i in range(netSize):
        while True:
            string = input('Введите ' + str(i+1) + ' строку:\n')
            if len(string) == netSize:
                encrypted.append(string.lower())
                break
            else:
                print('Введено неверное количество символов')
    
    maskFileName = input('Введите имя файла с масками:\n')
    exec(f'from {maskFileName} import quantity')
    masks = np.memmap(maskFileName, shape=(quantity, quaterSize**2))

    #print(decrypt(encrypted, testKey, 'CW'))
    a = hack(encrypted)
    print(a)