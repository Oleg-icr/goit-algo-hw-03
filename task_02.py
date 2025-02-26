import random

def get_numbers_ticket(min, max, quantity):
    random_set = set()
    if max == quantity :
        print (f"Result: a sequence of digits from {min} to {max}  ")
        return random_set
    elif quantity > max :
        print (f"Result: a sequence of digits from {min} to {max}  ")
        return random_set
    elif min < 1 or max > 1000 :
        print ("FROM should be higher or equal 1 , and TO should be lower or equal 1000")
        return random_set
    else:
        while len(random_set)  < quantity:
            random_set.add( random.randrange(min, max) )
            # print (random.randrange(min, max) )
        return sorted(random_set)

print ( get_numbers_ticket(1, 10, 8) )
