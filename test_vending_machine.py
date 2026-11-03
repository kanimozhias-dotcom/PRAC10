"""Unit tests for Vending Machine Restocking System."""

import unittest

import vending_machine as vm


class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        vm.inventory = {
            "Water Bottle": {
                "quantity": 5,
                "threshold": 10
            },
            "Chips": {
                "quantity": 20,
                "threshold": 5
            }
        }

    def test_low_stock(self):
        self.assertEqual(
            vm.check_stock("Water Bottle"),
            "Low Stock"
        )

    def test_sufficient_stock(self):
        self.assertEqual(
            vm.check_stock("Chips"),
            "Stock Sufficient"
        )

    def test_product_not_found(self):
        self.assertEqual(
            vm.check_stock("Biscuits"),
            "Product Not Found"
        )

    def test_generate_alerts(self):
        self.assertEqual(
            vm.generate_alerts(),
            ["Water Bottle"]
        )

    def test_restock_product(self):
        result = vm.restock_product(
            "Water Bottle", 10
        )

        self.assertEqual(
            result, "Restocking Successful"
        )

        self.assertEqual(
            vm.inventory["Water Bottle"]["quantity"],
            15
        )

    def test_invalid_restock(self):
        self.assertEqual(
            vm.restock_product("Chips", 0),
            "Invalid Quantity"
        )


if __name__ == "__main__":
    unittest.main()