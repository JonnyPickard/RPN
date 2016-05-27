from rusty import answer
import unittest

class TestMyFunctions(unittest.TestCase):
    # def test_returns_correct_string(self):
    #     self.assertEqual(answer("2+3*2"),"232*+")

    def test_returns_correct_string(self):
        self.assertEqual(answer("2*4*3+9*3+5"),"243**93*5++")

if __name__ == '__main__':
    unittest.main(exit=False)
