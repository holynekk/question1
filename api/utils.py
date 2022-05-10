import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

def create_random_plate():
    N1 = random.choice(numbers)
    N2 = random.choice(numbers)
    #generate 4 randomly chosen numbers, N1, N2, N3, N4
    L1 = random.choice(letters)
    L2 = random.choice(letters)
    L3 = random.choice(letters)

    N3 = random.choice(numbers)
    N4 = random.choice(numbers)

    return N1+N2+' '+L1+L2+L3+' '+N3+N4