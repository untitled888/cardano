text = ''
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя \n'
processedText = ''

while True:
    part = input('Введите часть текста:\n')
    if part.lower() == "стоп":
        break
    text += part.lower()
    text += ' '

for i in text:
    if i in alphabet:
        processedText += i

processedText = processedText.replace('\n', ' ')
splitText = processedText.split()
del processedText

words = []

for i in splitText:
    if len(i) > 4:
        words.append(i)

words = set(words)

file = open(input('Введите имя файла:\n'), 'w', encoding='utf-8')
file.write('words = {')

for i in words:
    file.write("'" + i + "',\n")

file.write('}')
file.close()