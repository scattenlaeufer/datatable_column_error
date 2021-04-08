#!/usr/bin/env python3

"""
A code example for datatable, that throws a ValueError when reading data
"""

import datatable as dt

column_names = ["A", "B", "C"]
example_data = dt.fread("bad_data.tsv", fill=True, columns=column_names)

print(example_data)
