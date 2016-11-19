
from operator import attrgetter
from collections import namedtuple

def greedy_knapsack(item_count: int, capacity: int, items: list, approach: str) -> object:
    # a function to apply a simple greedy algorithm to the Knapsack problem
    #

    """

    :rtype: str
    """
    if approach == "value":
        # choose the most valuable items first
        # sort items by value

        sorted_items = sorted(items, key = attrgetter('value'), reverse = True)

        x = items

    elif approach == "smallest":
        # choose the smallest items first

        sorted_items = sorted(items, key = attrgetter('weight'))
        x = sorted_items

    elif approach == "value_to_weight":
        # choose the items with best value to weight ratio first

        item1 = namedtuple("Item", ['index', 'value', 'weight', 'value_to_weight'])
        for item in items:
            value_to_weight = item.value / item.weight
            items[item.index] = item1(item.index, item.value, item.weight, value_to_weight)

        sorted_items = sorted(items, key = attrgetter('value_to_weight'), reverse = True)


        x = items[3]
    else:
        # something has gone wrong
        x = items[4]

    # now do something with the sorted_items
    value = 0
    weight = 0
    taken = [0]*len(items)
    sorted_taken = [0]*len(items)

    for item in sorted_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            weight += item.weight
            value += item.value

    # for index in sorted_items:
    #     taken[item.index] = sorted_taken[index]

    # make the output
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))

    return output_data
