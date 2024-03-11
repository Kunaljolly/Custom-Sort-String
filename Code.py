class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # Create a dictionary to store the position of each character in order
        order_dict = {char: i for i, char in enumerate(order)}

        # Custom sorting function based on order_dict
        def custom_sort(char):
            return order_dict.get(char, float('inf'))

        # Sort the string using the custom sorting function
        sorted_s = sorted(s, key=custom_sort)

        # Convert the sorted list back to a string
        result = ''.join(sorted_s)

        return result
