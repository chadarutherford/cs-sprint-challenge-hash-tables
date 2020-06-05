cache = {}

def has_negatives(a):
    result = []
    # iterate through all items in the array
    for (index, item) in enumerate(a):
        # cache the items as they are accessed
        cache[index] = item

    # check a again
    for item in a:
        # if the item multiplied by -1 is in the cache
        if (item * -1) in cache:
            # if the item is 0,
            # ignore the value because
            # zero doesn't have a negative
            if item == 0:
                continue
            # else append the opposite of the item in the result array
            result.append(-item)
    # if we get here we are done adding items to array,
    # return the array 
    return result

if __name__ == "__main__":
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    # expected [1, 2, 4]

    a = list(range(5000000))
    a += [-1,-2,-3]

    result = has_negatives(a)
    result.sort()
    print(result)
    # expected [1, 2, 3]
