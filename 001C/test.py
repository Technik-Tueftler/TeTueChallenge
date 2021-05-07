# -*- coding: utf-8 -*-
# pylint 001C/technik_tueftler.py
import timeit
test_code = '''
import technik_tueftler
technik_tueftler.sort_highscore_list_concept_1(technik_tueftler.get_testlist(1000))
'''
laufzeit = timeit.Timer(test_code)
test = laufzeit.repeat(repeat=10, number=1)
sum = 0
for element in test:
    sum = sum + element
print(sum/len(test))