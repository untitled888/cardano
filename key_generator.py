import numpy as np
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

    quantity = maskToNumber(stopStr) - maskToNumber(startStr)

    fileName = input('Введите имя файла:\n')
    quantityFile = open(fileName + '.py', 'w')
    quantityFile.write('quantity = ' + str(quantity))
    quantityFile.close()
    data = np.memmap(fileName, mode='w+', shape=(quantity, quaterSize**2))

    #Перебираем маски и кладём в файл
    from time import time
    startTime = time()
    for i in range(quantity):
        data[i] = currentMask
        data.flush()
        currentMask = plusOne(currentMask, -1)
    print(quantity)
    print(time() - startTime)