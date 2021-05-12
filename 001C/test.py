# -*- coding: utf-8 -*-
# pylint 001C/technik_tueftler.py
import timeit
test_code = '''
import technik_tueftler
technik_tueftler.sort_highscore_list_concept_5(technik_tueftler.get_testlist(100))
'''
test_code2 = '''
import technik_tueftler
technik_tueftler.sort_highscore_list_concept_5(technik_tueftler.get_testlist(1000))
'''
laufzeit = timeit.Timer(test_code)
test = laufzeit.repeat(repeat=10, number=1)
sum = 0
for element in test:
    sum = sum + element
print(f'100  Player: {sum/len(test)}')

laufzeit = timeit.Timer(test_code2)
test = laufzeit.repeat(repeat=10, number=1)
sum = 0
for element in test:
    sum = sum + element
print(f'1000 Player: {sum/len(test)}')
