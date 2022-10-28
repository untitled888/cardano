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
print(words)