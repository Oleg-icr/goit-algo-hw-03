import random

def get_numbers_ticket(min, max, quantity):
    # creating set
    random_set = set()
    # checks if numbers amount random_set equal quantity
    if (max-min) == quantity :
        print (f"Result: a sequence of digits from {min} to {max}  ")
        return random_set
    # checks if numbers amount random_set less than quantity
    elif quantity > (max-min) :
        print (f"Result: a sequence of digits from {min} to {max}  ")
        return random_set
    # checks prescribed limits
    elif min < 1 or max > 1000 :
        print ("FROM should be higher or equal 1 , and TO should be lower or equal 1000")
        return random_set
    else:
        # generates random_set
        while len(random_set)  < quantity:
            random_set.add( random.randrange(min, max) )
        return sorted(random_set)

print ( get_numbers_ticket(2, 11, 10) )
