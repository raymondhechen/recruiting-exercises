#!/usr/bin/env python3

"""
----------------------------------------------------------------------------
Raymond Chen, August, 2020
Deliverr Coding Challenge, Algorithm
----------------------------------------------------------------------------
"""

"""
ALGORITHM
The algorithm used to solve this challenge utilizes a greedy approach.
Since warehouses are ordered by cost in ascending order, we always want
to select items from earlier warehouses in the list in order to minimize
cost. So what we can do is iterate over each warehouse and always take out 
the most we can from a single warehouse's inventory for an order before 
moving to the next warehouse. This greedy approach guarantees that our costs 
will be at a minimum. In addition, we keep track of our orders across 
warehouses by directly subtracting from the order list any items that are 
fulfilled.

Assuming that the number of orders is n and the number of warehouses is m, 
then our algorithm will run in O(nm) time.
"""

"""
CONSIDERATIONS
This implementation allows for both partial and non-partial solutions. 
A partial solution is the best possible result with orders that are 
unfulfilled due to an unsolvable shortage. This only applies when a 
complete solution is not possible. Non-partial solutions don't allow this and 
return no solution if there are unfufilled items. This is designated by the
"partial" parameter.
Example: 
order = {'apple': 2}, inventory: [{name: 'a', inventory: {apple: 1}}, {name: 'b', inventory: {'apple': 0}}]
partial solution = [{'a': {'apple': 1}}]


In addition, this implementation allows for the choice of showing empty 
fulfillments from warehouses that either have insufficient inventory 
or do not need to supply due to an order being fulfilled already. This 
is designated by the "showEmpty" parameter.
Example: 
order = {'apple': 2}, inventory: [{name: 'a', inventory: {apple: 1}}, {name: 'b', inventory: {'apple': 0}}]
partial solution = [{'a': {'apple': 1}}, {'b': {'apple': 0}}]
"""


class Allocator():
    @staticmethod
    def allocate(orders, inventory, partial = False, showEmpty = False):
        """
        Returns list of warehouse order allocations
        param: orders -> dictionary of orders
        param: inventory -> list of dictionaries representing warehouse inventories
        param: partial -> boolean indiciating whether partial solutions allowed or not
        param: showEmpty -> boolean flag indicating whether to show empty fulfillments
        return: list of dictionaries representing allocations for each warehouse
        """

        solution = []

        # iterate warehouses in greedy fashion
        for warehouse in inventory:

            # initialize solution for a warehouse
            warehouse_allocation = {warehouse['name']: {}}

            # iterate over orders
            for order_name, order_count in orders.items():

                # if warehouse has inventory for order that is > 0 and remaining order count > 0
                if order_name in warehouse['inventory'] and warehouse['inventory'][order_name] > 0 and order_count > 0:

                    # get warehouse current quantity for shortage scenario
                    alloc_count = warehouse['inventory'][order_name]

                    # if warehouse inventory surplus
                    if alloc_count > order_count:
                        orders[order_name] = 0  # set remaining orders to 0
                        alloc_count = order_count  # set warehouse allocation for surplus
                    # if inventory shortage
                    else:
                        # calculate difference to get reamining orders
                        orders[order_name] = order_count - alloc_count

                    # set order allocation for warehouse
                    warehouse_allocation[warehouse['name']][order_name] = alloc_count

                # if warehouse doesn't have inventory for order or order completed
                elif showEmpty:
                    # show 0 for empty order fulfillment if showEmpty flag is true
                    warehouse_allocation[warehouse['name']][order_name] = 0

            # warehouse completed, add to solution list if warehouse has any shipments
            if warehouse_allocation[warehouse['name']]:
                solution.append(warehouse_allocation)

        # if partial solutions not allowed, return [] if no solution due to unfulfilled order
        if not partial and not all(i == 0 for i in orders.values()):
            return []

        return solution
