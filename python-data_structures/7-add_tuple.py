#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    index_max = max(len(tuple_a), len(tuple_b))
    if index_max > 2:
        index_max == 2
    tuple_c = tuple((tuple_a[i] if i < len(tuple_a) else 0) + (tuple_b[i] if i < len(tuple_b) else 0) for i in range(index_max))
    return tuple_c
