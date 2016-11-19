

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

    elif approach == "smallest":
        # choose the smallest items first
        x = 2

    elif approach == "value_to_weight":
        # choose the items with best value to weight ratio first
        x = 3
    else:
        # something has gone wrong
        x = 4

    return x
