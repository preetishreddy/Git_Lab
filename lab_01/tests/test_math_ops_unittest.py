import unittest
from mypkg.math_ops import add, sub, mul, div, is_prime


class TestMathOps(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-3, -5), 2)

    def test_mul(self):
        self.assertEqual(mul(3, 7), 21)
        self.assertEqual(mul(-2, 5), -10)

    def test_div(self):
        self.assertEqual(div(12, 3), 4)
        self.assertEqual(div(7, 2), 3.5)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))


if __name__ == "__main__":
    unittest.main()
