def next_number(num_arr):
    """Given a list of digits, generate the next increment
    of the number formed by these digits. E.g. [4, 0, 0, 0]
    would return [4, 1, 0, 0]"""

    start_index = len(num_arr) - 1

    result_arr = list(num_arr)

    while result_arr[start_index] == 9:
        result_arr[start_index] = 0

        if start_index > 0:
            start_index -= 1

    if all(v == 0 for v in result_arr) and num_arr[0] > 0:
        result_arr.insert(0, 1)
    else:
        result_arr[start_index] += 1

    return result_arr
