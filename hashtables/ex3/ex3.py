cache = {}


def intersection(arrays):
    result = []
    # get the inner array from the 2D array passed in
    for array in arrays:
        # get the value from the inner array
        for item in array:
            if item in cache:
                # if the item is in the cache increment the value
                cache[item] += 1
            else:
                # else set the value == 1
                cache[item] = 1

    for key, value in cache.items():
        # for each value in the cache
        # if the value is equal to the amount of inner arrays,
        # append the result to the array
        if value == len(arrays):
            result.append(key)

    # if we get here, the array is set,
    # return it
    return result

if __name__ == "__main__":
    result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
    ])
    print(result == [1])