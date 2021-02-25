import unittest
import fibonacci

class TestCalculator(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonacci.fib(1), 0)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(5), 3)
        self.assertEqual(fibonacci.fib(-1), False)
        self.assertEqual(fibonacci.fib('a'), False)
    def test_factorial(self):
        self.assertEqual(fibonacci.factorial(-1), False)
        self.assertEqual(fibonacci.factorial(0), 1)
        self.assertEqual(fibonacci.factorial(5), 120)
        self.assertEqual(fibonacci.factorial('a'), False)

if __name__ == '__main__':
    unittest.main()
    test_answer()

def func(x):
    return fibonacci.fib(x)

def func_2(x):
    return fibonacci.factorial(x)

def test_answer():
    assert func(3) == 1
    assert func(5) == 3
    assert func('a') == False
    assert func(-1) == False
    assert func_2(-1) == False
    assert func_2('a') == False
    assert func_2(5) == 120