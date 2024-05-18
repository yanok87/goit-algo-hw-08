"""Module that calculates the minimum sum of numbers in a heap"""

import heapq


def min_connection_cost(numbers):
    """
    Calculates the minimum connection cost for a list of numbers.

    Args:
        numbers: A list of numbers (not necessarily sorted).

    Returns:
        The minimum connection cost.
    """
    if len(numbers) <= 1:
        return 0

    # Create a min-heap from the input list
    heap = numbers[:]
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        # Extract the two smallest numbers from the heap
        first_num = heapq.heappop(heap)
        second_num = heapq.heappop(heap)

        # Update the total cost
        total_cost += first_num + second_num

        # Insert the sum of the extracted numbers back into the heap
        heapq.heappush(heap, first_num + second_num)

    return total_cost


# Example usage
numbers = [1, 3, 4, 2]
min_cost = min_connection_cost(numbers)
print("Minimum connection cost:", min_cost)
