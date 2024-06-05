#!/usr/bin/python


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (tuple_a[0] + tuple_b[0] if len(tuple_b) > 0 else tuple_a[0], tuple_a[1] + tuple_b[1] if len(tuple_b) > 1 else tuple_a[1])
    return tuple_c
