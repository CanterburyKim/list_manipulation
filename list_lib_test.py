"""
Test case file to test the transpose functions
"""
import unittest
import list_lib as ml


class TestList(unittest.TestCase):
    """
    test class
    """
    def test_create_empty(self):
        test_row = ml.create_an_empty_list(6)
        expected_result_row = [0, 0, 0, 0, 0, 0]

        self.assertEqual(test_row, expected_result_row)


    def test_find_min(self):
        """
        """
        # set up the test matrix
        test_row = [3,2,4, 1000]
        expected_min = 2
        min = ml.find_min(test_row)

        self.assertEqual(expected_min, min)

    def test_find_max(self):
        test_row = [3,1000, 2,4]
        expected_max= 1000
        max=ml.find_max(test_row)

        self.assertEqual(max, expected_max)

    def test_smallest_bot(self):
        """
        """
        # set up the test matrix
        test_row = [5,7, 1, 3,22]
        expected_result_row = [1,7,5,3,22]
        ml.smallest_bot(test_row)

        self.assertEqual(test_row, expected_result_row)

    def test_largest_top(self):
        """
        """
        # set up the test matrix
        test_row = [11, 2, 99, 3, 12]
        expected_result_row = [11, 2, 12, 3, 99]
        ml.largest_top(test_row)

        self.assertEqual(test_row, expected_result_row)

    def test_find_min_in_range(self):
        """
        """
        # set up the test matrix
        test_row = [2,7,4,1, -1]
        expected_min = 2
        mini = ml.find_min_in_range(test_row, 0,3)

        self.assertEqual(mini, expected_min)

    def test_find_max_in_range(self):
        """
        """
        # set up the test matrix
        test_row = [99, 7, 22, 11, 5, 2]
        expected_max = 22
        maxi = ml.find_max_in_range(test_row, 1, len(test_row))

        self.assertEqual(maxi, expected_max)




if __name__ == '__main__':
    unittest.main()
