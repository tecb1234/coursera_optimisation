print('blah')

def greedy_knapsack(item_count: int, capacity: int, items: object, approach: str) -> object:
    # a function to apply a simple greedy algorithm to the Knapsack problem
    #

    """

    :rtype: int
    """
    if approach == "value":
        # choose the most valuable items first
        # sort items by value

        x = 1


    else:
        if approach == "smallest":
            # choose the smallest items first
            x = 2

        else:
            if approach == "value_to_weight":
                # choose the items with best value to weight ratio first
                x = 3
            else:
                # something has gone wrong
                x = 4
    return x


print(greedy_knapsack(1, 1, 1, "value"))
