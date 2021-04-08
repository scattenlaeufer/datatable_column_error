#!/usr/bin/env python3

"""
A code example for datatable, that throws an IOError when reading data
"""

import datatable as dt


example_data = dt.fread("bad_data.tsv", fill=True)

print(example_data)
