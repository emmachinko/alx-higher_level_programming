#!/usr/bin/python3
"""defines an object attribute lookup functions."""


def lookup(obj):
    """returns list of an object's available attribute"""
    return (dir(obj))
