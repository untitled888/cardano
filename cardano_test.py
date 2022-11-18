import cardano
import unittest
import numpy as np

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
cardano.size = 8

class Test(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(cardano.decrypt(text, key, "CW"), "собраниеделегатоврайонаотменитеполициякемтопредупрежденаантонабв")
    def test_ccw(self):
        self.assertEqual(cardano.decrypt(text, key, "CCW"), "собраниеделегатопрежденаантонабволициякемтопредуврайонаотменитеп")
    def test_plusOne(self):
        self.assertEqual(cardano.plusOne('00000110', -1), '00000111')
    def test_plusOne2(self):
        self.assertEqual(cardano.plusOne('00000111', -1), '00001000')
    def test_hack(self):
        self.assertEqual(cardano.hack(text, '0'*int(8**2/4*3) + '1'*int(8**2/4)), ("собраниеделегатоврайонаотменитеполициякемтопредупрежденаантонабв", key))

if __name__ == '__main__':
    unittest.main()