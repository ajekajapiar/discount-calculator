
import unittest

from calculator import calculate_discount


class TestDiscountCalculator(unittest.TestCase):

    def test_normal_discount(self):
        result = calculate_discount(100_000, 20, 3)

        self.assertEqual(result["subtotal"], 300_000)
        self.assertEqual(result["discount_amount"], 60_000)
        self.assertEqual(result["final_total"], 240_000)

    def test_no_discount(self):
        result = calculate_discount(100_000, 0, 2)

        self.assertEqual(result["discount_amount"], 0)
        self.assertEqual(result["final_total"], 200_000)

    def test_full_discount(self):
        result = calculate_discount(100_000, 100, 2)

        self.assertEqual(result["discount_amount"], 200_000)
        self.assertEqual(result["final_total"], 0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-100_000, 10, 1)

    def test_invalid_discount_rate(self):
        with self.assertRaises(ValueError):
            calculate_discount(100_000, 110, 1)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            calculate_discount(100_000, 10, 0)


if __name__ == "__main__":
    unittest.main()
