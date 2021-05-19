import unittest
from ..korbi_korb import *
import random

import cProfile, pstats, io
from pstats import SortKey

class RankPlayerTestCase(unittest.TestCase):
    def test_simple_player_list(self):
        to_be_sorted_list = [Player("Max", 3, 50, 10), Player("Moritz", 2, 20, 30), Player("Witwe Bolte", 3, 49, 9),
                             Player("Mecke", 1, 10, 79), Player("Lämpel", 3, 49, 10), Player("Fritz", 2, 20, 31),
                             Player("Böck", 1, 10, 80)]

        sort_player_list(to_be_sorted_list)

        expected_list = [Player("Lämpel", 3, 49, 10), Player("Witwe Bolte", 3, 49, 9), Player("Max", 3, 50, 10),
                         Player("Fritz", 2, 20, 31), Player("Moritz", 2, 20, 30), Player("Böck", 1, 10, 80),
                         Player("Mecke", 1, 10, 79)]

        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        for index in range(len(to_be_sorted_list)):
            self.assertEqual(to_be_sorted_list[index].name, expected_list[index].name)

    def test_1k_player_list(self):
        # Create a sorted list 'expected_list' with 1000 entries.
        expected_list = []
        for secrets in range(10):
            for playtime in range(10):
                for kills in range(10):
                    expected_list.append(
                        Player((str(len(expected_list))), MAX_SECRETS - secrets, playtime, MAX_KILLS - kills))

        self.assertEqual(len(expected_list), 1000)

        # Make a deep copy of 'expected_list' to new list 'to_be_sorted_list' with different objects but same values
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

        # Sort the 'to_be_sorted_list' and check if is equal to the 'expected_list'
        sort_player_list(to_be_sorted_list)
        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        for index in range(len(to_be_sorted_list)):
            self.assertEqual(to_be_sorted_list[index].name, expected_list[index].name)
            self.assertEqual(to_be_sorted_list[index].secrets, expected_list[index].secrets)
            self.assertEqual(to_be_sorted_list[index].playtime_s, expected_list[index].playtime_s)
            self.assertEqual(to_be_sorted_list[index].kills, expected_list[index].kills)

    def test_100k_player_list_high_value(self):
        # Create a sorted list 'expected_list' with 1000 entries.
        expected_list = []
        for secrets in range(MAX_SECRETS - 10, MAX_SECRETS, 1):
            for playtime in range(MAX_PLAYTIME - 100, MAX_PLAYTIME, 1):
                for kills in range(MAX_KILLS - 100, MAX_KILLS, 1):
                    expected_list.append(
                        Player((str(len(expected_list))), MAX_SECRETS - secrets, playtime, MAX_KILLS - kills))

        self.assertEqual(len(expected_list), 100000)

        # Make a deep copy of 'expected_list' to new list 'to_be_sorted_list' with different objects but same values
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

        # Sort the 'to_be_sorted_list' and check if is equal to the 'expected_list'
        sort_player_list(to_be_sorted_list)
        self.assertEqual(len(to_be_sorted_list), len(expected_list))
        for index in range(len(to_be_sorted_list)):
            self.assertEqual(to_be_sorted_list[index].name, expected_list[index].name)
            self.assertEqual(to_be_sorted_list[index].secrets, expected_list[index].secrets)
            self.assertEqual(to_be_sorted_list[index].playtime_s, expected_list[index].playtime_s)
            self.assertEqual(to_be_sorted_list[index].kills, expected_list[index].kills)

    def test_bit_fields_secrets(self):
        max_kills_player = Player("Max_secrets", MAX_SECRETS, 0, 0)
        gamerscore = max_kills_player.gamer_score
        bit_mask = (MAX_SECRETS << (len(bin(MAX_PLAYTIME)) + len(bin(MAX_KILLS)) - 4))
        self.assertNotEqual(bin(gamerscore), bin(bit_mask))
        result = (bit_mask & gamerscore)
        self.assertEqual(bin(result), bin(bit_mask))

    def test_bit_fields_playtime(self):
        max_kills_player = Player("Max_playtime", 0, 0, 0)
        gamerscore = max_kills_player.gamer_score
        bit_mask = (MAX_PLAYTIME << (len(bin(MAX_KILLS)) - 2))
        self.assertEqual(bin(gamerscore), bin(bit_mask))
        result = (bit_mask & gamerscore)
        self.assertEqual(bin(result), bin(bit_mask))

    def test_bit_fields_kills(self):
        max_kills_player = Player("Max_kills", 0, 0, MAX_KILLS)
        gamerscore = max_kills_player.gamer_score
        bit_mask = MAX_KILLS
        self.assertNotEqual(bin(gamerscore), bin(bit_mask))
        result = (bit_mask & gamerscore)
        self.assertEqual(bin(result), bin(bit_mask))

    def test_korib_korb_speed(self):
        expected_list = []
        for secrets in range(10):
            for playtime in range(10):
                for kills in range(100):
                    expected_list.append(
                        Player((str(len(expected_list))), MAX_SECRETS - secrets, playtime+1, MAX_KILLS - kills))

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
        sort_player_list(to_be_sorted_list)
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
