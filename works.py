#!/usr/bin/env python3

"""
A code example for datatable, that reads data correctly
"""

import datatable as dt


example_data = dt.fread("good_data.tsv", fill=True)

print(example_data)

column_names = ["A", "B", "C"]
example_data_with_names = dt.fread("good_data.tsv", fill=True, columns=column_names)
print(example_data_with_names)
