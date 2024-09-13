def count(data):
    n = 0

    def recurse(i):
        nonlocal n
        if isinstance(i, (int, float)):
            n += i
        elif isinstance(i, str):
            n += len(i)
        elif isinstance(i, (list, set, tuple)):
            for j in i:
                recurse(j)
        elif isinstance(i, dict):
            for key, value, in i.items():
                recurse(key)
                recurse(value)

    recurse(data)
    return n                               

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = count(data_structure)

print(result)