import math

# DEVELOPMENT ONGOING
def dont_give_me_five(start, end):
    count = end - start
    fives = math.floor(count / 10)
    return count - fives
