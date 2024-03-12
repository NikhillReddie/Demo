def check_even_list(num_list):
    # Go through each and every number
    for number in num_list:
        # Once we get an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass