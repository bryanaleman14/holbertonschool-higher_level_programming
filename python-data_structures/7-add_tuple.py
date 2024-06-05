#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    index_min = min(len(tuple_a), len(tuple_b))
    tuple_c = tuple(tuple_a[i] + tuple_b[i] for i in range(index_min))
    return tuple_c
