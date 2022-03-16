# DEVELOPMENT ONGOING
def dont_give_me_five(start, end):
    # Try a Positional Notation loop
    array_length = (end - start)
    if 5 in [int(d) for d in str(abs(start))] or 5 in [int(d) for d in str(abs(end))]:
        array_length -= 1
    digits = [int(d) for d in str(array_length)]
    print(f'Count = {array_length}')
    print(f'Digits = {len(digits)}')
    fives = 0
    if start >= -4 and end <= 4:
        return 0
    if array_length <= 10 and array_length >= 5:
        return 1
    for i in range(len(digits)-1,-1,-1):
        print(i)
        print(digits[::-1][i] * (10 ** i))
        fives += digits[::-1][i]*(10**i-9**i)
    print(f'Fives = {fives}')
    return array_length - fives
