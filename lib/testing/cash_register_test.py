#!/usr/bin/env python3

import unittest
import io
import sys
from lib.cash_register import CashRegister  # Adjusted import path

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(20)

    def test_initialization(self):
        register = CashRegister()
        self.assertEqual(register.total, 0.0)
        self.assertEqual(register.discount, 0)
        self.assertEqual(register.get_items(), [])

    def test_add_item(self):
        register = CashRegister()
        register.add_item("apple", 1.0, 3)
        self.assertEqual(register.total, 3.0)
        self.assertEqual(register.get_items(), ["apple", "apple", "apple"])

    def test_apply_discount(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register_with_discount.add_item("apple", 1.0, 3)
        self.cash_register_with_discount.apply_discount()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "After the discount, the total comes to $2.40.")
        self.assertEqual(self.cash_register_with_discount.total, 2.40)

    def test_apply_discount_no_discount(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register.apply_discount()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "There is no discount to apply.")
        self.assertEqual(self.cash_register.total, 0.0)

    def test_remove_item(self):
        register = CashRegister()
        register.add_item("apple", 1.0, 3)
        register.remove_item("apple", 1.0)
        self.assertEqual(register.total, 2.0)
        self.assertEqual(register.get_items(), ["apple", "apple"])

    def test_void_last_transaction(self):
        register = CashRegister()
        register.add_item("apple", 1.0, 3)
        register.void_last_transaction()
        self.assertEqual(register.total, 0.0)
        self.assertEqual(register.get_items(), [])

    def test_void_partial_transactions(self):
        register = CashRegister()
        register.add_item("apple", 1.0, 2)
        register.add_item("banana", 2.0, 1)
        register.void_last_transaction()
        self.assertEqual(register.total, 2.0)
        self.assertEqual(register.get_items(), ["apple", "apple"])

if __name__ == '__main__':
    unittest.main()
