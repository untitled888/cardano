import numpy as np
import os
symbols = '0123'

#Функция поворота
def rotateCW(key):
    newKey = np.array(range(quaterSize**2), int).reshape(quaterSize, quaterSize)
    for i in range(quaterSize):
        k = 0
        for j in range(-1, 0-(quaterSize+1), -1):
            newKey[i,k] = key[j,i]
            k += 1
    return newKey

#Прибавление 1 к четверичному числу
def plusOne(mask, index):
    new = mask
    if new[index] == 3:
        new[index] = 0
        return plusOne(new, index-1)
    else:
        new[index] += 1
        return new

#Создание ключа по маске
def maskToKey(mask):
    quaters = np.zeros(size**2, int).reshape(4, quaterSize**2)
    for i in range(len(mask)):
        quaters[mask[i], i] = 1
    q1 = quaters[0].reshape(quaterSize, quaterSize)

    q2 = quaters[1].reshape(quaterSize, quaterSize)
    q2 = rotateCW(q2)

    q3 = quaters[2].reshape(quaterSize, quaterSize)
    for i in range(2):
        q3 = rotateCW(q3)

    q4 = quaters[3].reshape(quaterSize, quaterSize)
    for i in range(3):
        q4 = rotateCW(q4)
    half1 = np.concatenate((q1,q2), axis=1)
    half2 = np.concatenate((q3,q4), axis=1)
    key = np.concatenate((half1, half2))
    return key

def maskToNumber(mask):
    number = 0
    for i in range(len(mask)):
        number += 3**i * int(mask[-1-i])
    return number


if __name__ == '__main__':
    #Запрос данных
    size = int(input('Введите размер сетки:\n'))
    quaterSize = size//2
    while True:
        startStr = input('Введите стартовую маску:\n')
        Continue = False
        if len(startStr) != quaterSize**2:
            print('Неверная длина маски')
            Continue = True
        for i in startStr:
            if not i in symbols:
                print('Неверные символы')
                Continue = True
        if Continue:
            Continue = False
            continue  
        break
    while True:
        stopStr = input('Введите маску для окончания:\n')
        Continue = False
        if len(stopStr) != quaterSize**2:
            print('Неверная длина маски')
            Continue = True
        for i in stopStr:
            if not i in symbols:
                print('Неверные символы')
                Continue = True
        if Continue:
            Continue = False
            continue  
        break

    #Подготовка
    start = np.arange(quaterSize**2)
    for i in range(len(startStr)):
        start[i] = int(startStr[i])

    stop = np.arange(quaterSize**2)
    for i in range(len(stopStr)):
        stop[i] = int(stopStr[i])
    
    currentMask = start.copy()

    k = maskToNumber(startStr)
    stopNumber = maskToNumber(stopStr)
    
    try:
        os.mkdir(f'keys{size}')
    except:
        pass
    os.chdir(f'keys{size}')

    #Перебираем маски, создаём по ним ключи и кладём в файл
    while k != stopNumber + 1:
        currentKey = maskToKey(currentMask)
        f = []
        if not f'{k}.npy' in os.listdir():
            np.save(f'{k}.npy', currentKey)
        currentMask = plusOne(currentMask, -1)
        k += 1