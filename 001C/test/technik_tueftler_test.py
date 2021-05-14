import unittest
from ..technik_tueftler import *
import random

import cProfile, pstats, io
from pstats import SortKey


class MyTestCase(unittest.TestCase):

    def test_technik_tueftler_speed(self):
        expected_list = []
        for secrets in range(10):
            for playtime in range(10):
                for kills in range(100):
                    expected_list.append(
                        Player((str(len(expected_list))), MAX_SECRETS - secrets, playtime, MAX_KILLS - kills))

        self.assertEqual(len(expected_list), 10000)

        to_be_sorted_list = list(expected_list)

        # check if both lists are equal in terms of object value equality, not object address equality
        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        for index in range(len(to_be_sorted_list)):
            self.assertEqual(to_be_sorted_list[index].name, expected_list[index].name)
            self.assertEqual(to_be_sorted_list[index].secrets, expected_list[index].secrets)
            self.assertEqual(to_be_sorted_list[index].playtime_s, expected_list[index].playtime_s)
            self.assertEqual(to_be_sorted_list[index].kills, expected_list[index].kills)

        # Shuffle the new list 'to_be_sorted_list'
        random.shuffle(to_be_sorted_list)
        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        self.assertNotEqual(to_be_sorted_list[0].name, expected_list[0].name)
        self.assertNotEqual(to_be_sorted_list[-1].name, expected_list[-1].name)

        pr = cProfile.Profile()
        pr.enable()
        to_be_sorted_list = sort_highscore_list_concept_5(to_be_sorted_list)
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        for index in range(len(to_be_sorted_list)):
            self.assertEqual(to_be_sorted_list[index].name, expected_list[index].name)


if __name__ == '__main__':
    unittest.main()
