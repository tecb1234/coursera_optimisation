def dp_knapsack(item_count: int, capacity: int, items: object):
    dp_matrix = [[0 for j in range(item_count + 1)] for i in range(capacity + 1)]


    # first column is already 0 so now we need to fill in the rest of the table
    for column in range(1, item_count + 1):
        for row in range(0, capacity + 1):
            if items[column - 1].weight > row:
                # then there is no space for this item, even on its own so step across the table to the left
                # and take the value when we haven't chose this item
                dp_matrix[row][column] = dp_matrix[row][column - 1]
            else:
                # this item would fit on its own, so we need to check if we want it to
                if items[column - 1].value + dp_matrix[row - items[column - 1].weight][column - 1] > dp_matrix[row][column - 1]:
                    # we do want this item
                    dp_matrix[row][column] = items[column - 1].value + dp_matrix[row - items[column - 1].weight][column - 1]
                else:
                    # we don't want this item
                    dp_matrix[row][column] = dp_matrix[row][column-1]

    # we have now filled in the dynamic programming matrix so now we need to work out what answer we want
    taken = [0] * len(items)
    row = capacity
    value = 0
    for column in range(item_count, 1, -1):
        if dp_matrix[row][column] > dp_matrix[row][column - 1]:
            # we do want this item
            taken[column - 1] = 1
            row = row - items[column - 1].weight
            value += items[column -1].value

    # make the output
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))

    return output_data
    # print(dp_matrix[2][2])