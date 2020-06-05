cache = {}

def has_negatives(a):
    result = []
    for (index, item) in enumerate(a):
        cache[index] = item

    for item in a:
        if (item * -1) in cache:
            if item == 0:
                continue
            result.append(-item)
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
