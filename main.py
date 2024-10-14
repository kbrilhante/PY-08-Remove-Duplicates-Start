import random


def remove_duplicates(lst):
    """ removes any duplicate numbers in the list. 
    it changes the original list """
    # your function goes here
    pass

# this generates a list with a length of 10 with random numbers from 1 to 20
potato = [random.randint(1, 20) for i in range(0, 10)]
print(potato)
remove_duplicates(potato)
print(potato)
