cache = {}


def intersection(arrays):
    result = []
    for array in arrays:
        for item in array:
            if item in cache:
                cache[item] += 1
            else:
                cache[item] = 1

    for key, value in cache.items():
        if value == len(arrays):
            result.append(key)

    return result

if __name__ == "__main__":
    result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
    ])
    print(result == [1])