cache = {}

def finder(files, queries):
    result = []
    for query in queries:
        cache[query] = { file_string for file_string in files if query in files }
    result = list(cache.values())
    return result


if __name__ == "__main__":
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []
    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    print(finder(files, queries))
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))
    # expected ['/bin/foo', '/usr/bin/baz']