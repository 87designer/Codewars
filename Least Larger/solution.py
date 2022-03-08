def least_larger(a, i):
    try:
        initial_number = a[i]
        unique_array = sorted(set(a))
        initial_number_index = unique_array.index(initial_number)
        larger_number = unique_array[initial_number_index + 1]
        desired_index = a.index(larger_number)
        return desired_index
    except:
        return -1
