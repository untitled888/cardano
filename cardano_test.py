import cardano
import unittest
import numpy as np

start = []
temp = []
for i in range(8):
    temp.append(0)
for i in range(8-1):
    start.append(temp)
temp = []
for i in range(8):
    temp.append(1)
start.append(temp)
start = np.array(start)
del temp

key = np.array([
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1]
])

text = ["осволрбп", "риеарцжй", "аонидния", "аекеонет", "адмамеен", "лттнеооп", "нигратае", "пебтдвуо"]

class CardanoTest(unittest.TestCase):
    def decryptCW(self):
        cardano.size = 8
        self.assertEqual(cardano.decrypt(text, key, "CW"), "собраниеделегатоврайонаотменитеполициякемтопредупрежденаантонабв")
    def decryptCCW(self):
        cardano.size = 8
        self.assertEqual(cardano.decrypt(text, key, "CCW"), "собраниеделегатопрежденаантонабволициякемтопредуврайонаотменитеп")
    def plusOne(self):
        cardano.size = 2
        self.assertEqual(cardano.plusOne(np.array([0,1,1,0]).reshape(2,2), -1).tolist(), np.array([0,1,1,1]).reshape(2,2).tolist())
    def plusOne2(self):
        cardano.size = 2
        self.assertEqual(cardano.plusOne(np.array([0,1,1,1]).reshape(2,2), -1).tolist(), np.array([1,0,0,0]).reshape(2,2).tolist())
    def hack(self):
        cardano.size = 8
        self.assertEqual(cardano.hack(text, start), ("собраниеделегатоврайонаотменитеполициякемтопредупрежденаантонабв", key))

if __name__ == '__main__':
    unittest.main()