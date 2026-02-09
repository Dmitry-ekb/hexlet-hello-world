from more_itertools import flatten, substrings

coll = [(0, 1), (2, 3)]
print(list(flatten(coll)))

print([''.join(s) for s in substrings('more')])
