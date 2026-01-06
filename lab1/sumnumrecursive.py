def recursive_sum(n_list):
    if len(n_list) == 0:
        return 0
    return n_list[0] + recursive_sum(n_list[1:])

print(recursive_sum([1, 2, 3, 4, 5]))