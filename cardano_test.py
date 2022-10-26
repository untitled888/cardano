import cardano
import unittest

text = ["осволрбп", "риеарцжй", "аонидния", "аекеонет", "адмамеен", "лттнеооп", "нигратае", "пебтдвуо"]
cardano.size = 8

class Test(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(cardano.decrypt(text, cardano.key, "CW"), "собраниеделегатоврайонаотменитеполициякемтопредупрежденаантонабв")
    def test_ccw(self):
        self.assertEqual(cardano.decrypt(text, cardano.key, "CCW"), "собраниеделегатопрежденаантонабволициякемтопредуврайонаотменитеп")

if __name__ == '__main__':
    unittest.main()