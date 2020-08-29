#!/usr/bin/env python3

"""
----------------------------------------------------------------------------
Raymond Chen, August, 2020
Deliverr Coding Challenge, Unit Tests
----------------------------------------------------------------------------
"""

import unittest
from Allocator import Allocator


class UnitTest(unittest.TestCase):
    """
    Unit Tests for Inventory Allocator
    """

    def test_simple(self):
        """
        Test 1 order with 1 warehouse with exact inventory match
        """

        order = {'apple': 1}
        inventory = [{'name': 'a', 'inventory': {'apple': 1}}]
        solution = [{'a': {'apple': 1}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_simple_split_inventory(self):
        """
        Test 1 order with split sufficient inventories
        """

        order = {'apple': 3}
        inventory = [{'name': 'a', 'inventory': {'apple': 1}},
                     {'name': 'b', 'inventory': {'apple': 3}}]
        solution = [{'a': {'apple': 1}}, {'b': {'apple': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_simple_split_fulfilled(self):
        """
        Test 1 order with split sufficient inventories that is fulfilled midway
        """

        order = {'apple': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 2}},
                     {'name': 'b', 'inventory': {'apple': 3}},
                     {'name': 'b', 'inventory': {'apple': 3}}]
        solution = [{'a': {'apple': 2}}, {'b': {'apple': 3}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_simple_insufficient(self):
        """
        Test 1 order with insufficient total inventory
        """

        order = {'apple': 3}
        inventory = [{'name': 'a', 'inventory': {'apple': 2}},
                     {'name': 'b', 'inventory': {'apple': 0}}]
        solution = []
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_simple_insufficient_partial(self):
        """
        Test 1 order with insufficient total inventory and return partial solution
        """

        order = {'apple': 3}
        inventory = [{'name': 'a', 'inventory': {'apple': 2}},
                     {'name': 'b', 'inventory': {'apple': 0}}]
        partial = True
        solution = [{'a': {'apple': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial), solution)

    def test_multiple(self):
        """
        Test multiple orders with sufficient inventory
        """

        order = {'apple': 1, 'orange': 2}
        inventory = [{'name': 'a', 'inventory': {'apple': 1, 'orange': 1}},
                     {'name': 'b', 'inventory': {'orange': 1}}]
        solution = [{'a': {'apple': 1, 'orange': 1}}, {'b': {'orange': 1}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_multiple_with_empty(self):
        """
        Test multiple orders with sufficient inventory split with empty inventories
        """

        order = {'apple': 1, 'orange': 2}
        inventory = [{'name': 'a', 'inventory': {'apple': 1, 'orange': 1}},
                     {'name': 'b', 'inventory': {'orange': 0}},
                     {'name': 'c', 'inventory': {'orange': 1}}]
        solution = [{'a': {'apple': 1, 'orange': 1}}, {'c': {'orange': 1}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_multiple_with_empty_show_empty(self):
        """
        Test multiple orders with sufficient inventory split with empty inventories and show empty shipments
        """

        order = {'apple': 1, 'orange': 2}
        inventory = [{'name': 'a', 'inventory': {'apple': 1, 'orange': 1}},
                     {'name': 'b', 'inventory': {'orange': 0}},
                     {'name': 'c', 'inventory': {'orange': 1}}]
        partial = False
        showEmpty = True
        solution = [{'a': {'apple': 1, 'orange': 1}},
                    {'b': {'apple': 0, 'orange': 0}},
                    {'c': {'apple': 0, 'orange': 1}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial, showEmpty), solution)

    def test_multiple_insufficient(self):
        """
        Test multiple orders with insufficient inventory
        """

        order = {'apple': 2, 'orange': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 1, 'orange': 1}},
                     {'name': 'b', 'inventory': {'apple': 1, 'orange': 2}}]
        partial = False
        solution = []
        self.assertEqual(Allocator.allocate(order, inventory, partial), solution)

    def test_multiple_insufficient_partial(self):
        """
        Test multiple orders with insufficient inventory, but return partial solution
        """

        order = {'apple': 2, 'orange': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 2, 'orange': 1}},
                     {'name': 'b', 'inventory': {'apple': 0, 'orange': 2}}]
        partial = True
        solution = [{'a': {'apple': 2, 'orange': 1}},
                    {'b': {'orange': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial), solution)

    def test_multiple_insufficient_partial_show_empty(self):
        """
        Test multiple orders with insufficient inventory, but return partial solution and empty values
        """

        order = {'apple': 2, 'orange': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 2, 'orange': 1}},
                     {'name': 'b', 'inventory': {'apple': 0, 'orange': 2}}]
        partial = True
        showEmpty = True
        solution = [{'a': {'apple': 2, 'orange': 1}},
                    {'b': {'apple': 0, 'orange': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial, showEmpty), solution)

    
    def test_comprehensive(self):
        """
        Test multiple orders and multiple sufficient inventory
        """

        order = {'apple': 25, 'orange': 10, 'banana': 7, 'grape': 20, 'watermelon': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                     {'name': 'b', 'inventory': {'apple': 15, 'orange': 5, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                     {'name': 'c', 'inventory': {'apple': 20, 'orange': 3, 'banana': 8, 'grape': 12, 'watermelon': 2}}]
        solution = [{'a': {'apple': 5, 'orange': 7, 'grape': 4, 'watermelon': 1}},
                    {'b': {'apple': 15, 'orange': 3, 'grape': 4, 'watermelon': 2}},
                    {'c': {'apple': 5, 'banana': 7, 'grape': 12, 'watermelon': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_comprehensive_show_empty(self):
        """
        Test multiple orders and multiple sufficient inventory and show empty values
        """

        order = {'apple': 25, 'orange': 10,
                 'banana': 7, 'grape': 20, 'watermelon': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                     {'name': 'b', 'inventory': {'apple': 15, 'orange': 5, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                     {'name': 'c', 'inventory': {'apple': 20, 'orange': 3, 'banana': 8, 'grape': 12, 'watermelon': 2}}]
        partial = False
        showEmpty = True
        solution = [{'a': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                    {'b': {'apple': 15, 'orange': 3, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                    {'c': {'apple': 5, 'orange': 0, 'banana': 7, 'grape': 12, 'watermelon': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial, showEmpty), solution)

    def test_comprehensive_insufficient(self):
        """
        Test multiple orders and insufficient inventory
        """

        order = {'apple': 25, 'orange': 10,
                 'banana': 7, 'grape': 20, 'watermelon': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                     {'name': 'b', 'inventory': {'apple': 15, 'orange': 5, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                     {'name': 'c', 'inventory': {'apple': 20, 'orange': 3, 'banana': 8, 'grape': 11, 'watermelon': 2}}]
        solution = []
        self.assertEqual(Allocator.allocate(order, inventory), solution)
    
    def test_comprehensive_insufficient_partial(self):
        """
        Test multiple orders and insufficient inventory but return partial solution
        """

        order = {'apple': 25, 'orange': 10,
                 'banana': 7, 'grape': 20, 'watermelon': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                     {'name': 'b', 'inventory': {'apple': 15, 'orange': 5, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                     {'name': 'c', 'inventory': {'apple': 20, 'orange': 3, 'banana': 8, 'grape': 11, 'watermelon': 2}}]
        partial = True
        solution = [{'a': {'apple': 5, 'orange': 7, 'grape': 4, 'watermelon': 1}},
                    {'b': {'apple': 15, 'orange': 3, 'grape': 4, 'watermelon': 2}},
                    {'c': {'apple': 5, 'banana': 7, 'grape': 11, 'watermelon': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial), solution)

    def test_comprehensive_insufficient_partial_show_empty(self):
        """
        Test multiple orders and insufficient inventory but return partial solution and empty values
        """

        order = {'apple': 25, 'orange': 10,
                 'banana': 7, 'grape': 20, 'watermelon': 5}
        inventory = [{'name': 'a', 'inventory': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                     {'name': 'b', 'inventory': {'apple': 15, 'orange': 5, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                     {'name': 'c', 'inventory': {'apple': 20, 'orange': 3, 'banana': 8, 'grape': 11, 'watermelon': 2}}]
        partial = True
        showEmpty = True
        solution = [{'a': {'apple': 5, 'orange': 7, 'banana': 0, 'grape': 4, 'watermelon': 1}},
                    {'b': {'apple': 15, 'orange': 3, 'banana': 0, 'grape': 4, 'watermelon': 2}},
                    {'c': {'apple': 5, 'orange': 0, 'banana': 7, 'grape': 11, 'watermelon': 2}}]
        self.assertEqual(Allocator.allocate(order, inventory, partial, showEmpty), solution)

    def test_edge_empty_order(self):
        """
        Test empty orders
        """

        order = {}
        inventory = [{'name': 'a', 'inventory': {'apple': 1}},
                     {'name': 'b', 'inventory': {'orange': 1}}]
        solution = []
        self.assertEqual(Allocator.allocate(order, inventory), solution)

    def test_edge_empty_inventory(self):
        """
        Test empty inventory
        """

        order = {'apple': 1, 'orange': 1}
        inventory = []
        solution = []
        self.assertEqual(Allocator.allocate(order, inventory), solution)

if __name__ == '__main__':
    unittest.main()
