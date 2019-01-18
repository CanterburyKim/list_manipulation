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


    def test_make_a_times2_list(self):
        """
        """
        # set up the test matrix
        test_row = [1,3,2,4]
        expected_result_row = [2,6,4,8]
        ml.make_a_times2_list(test_row)

        self.assertEqual(test_row, expected_result_row)


    def test_get_half_list(self):
        """
        """
        # set up the test matrix
        test_row = [1,2,3,4,5,6,7,8]
        expected_result_row = [1,2,3,4]
        ml.get_half_list(test_row)

        self.assertEqual(test_row, expected_result_row)

    def test_get_half_list2(self):
        """
        """
        # set up the test matrix
        test_row = [1,2,3,4,5,6,7]
        expected_result_row = [1,2,3]
        ml.get_half_list(test_row)

        self.assertEqual(test_row, expected_result_row)


    def test_rotate_list_right(self):
        """
        """
        test_row = [1,7,3,9]
        expected_result_row = [9,1,7,3]

        ml.rotate_list_right(test_row)

        self.assertEqual(test_row,expected_result_row)

    def test_rotate_list_left(self):
        """
        """
        test_row = [1,7,3,9]
        expected_result_row = [7,3,9,1]

        ml.rotate_list_left(test_row)

        self.assertEqual(test_row,expected_result_row)


    def test_swap_spots_opp_list(self):
        test_row = [1, 3, 5, 7, 11]
        expected_result_row = [11, 7, 5, 3, 1]

        ml.swap_spots_opp_list(test_row)

        self.assertEqual(test_row,expected_result_row)

    def test_swap_spots_opp_list2(self):
        test_row = [1, 3, 5, 7]
        expected_result_row = [7, 5, 3, 1]

        ml.swap_spots_opp_list(test_row)

        self.assertEqual(test_row,expected_result_row)


    def test_swap_spots_adj_list(self):
        test_row = [1,2,3,4,5,6]
        expected_result_row = [2,1,4,3,6,5]

        ml.swap_spots_adj_list(test_row)

        self.assertEqual(test_row,expected_result_row)

    def test_swap_spots_adj_list2(self):
        test_row = [1,2,3,4,5]
        expected_result_row = [2,1,4,3,5]

        ml.swap_spots_adj_list(test_row)

        self.assertEqual(test_row,expected_result_row)

    def test_bubble_swap_list(self):
        test_row = [7,5,6,3,2,1]
        expected_result_row = [5,6,3,2,1,7]

        ml.bubble_swap_list(test_row)

        self.assertEqual(test_row,expected_result_row)
        pass



if __name__ == '__main__':
    unittest.main()
