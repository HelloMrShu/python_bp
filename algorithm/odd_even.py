#!/usr/bin/env python
# -*- coding: utf-8 -*-

def oddEvenSort(data):
    size = len(data)
    if not data or size < 2:
        return data

    odd = even = 0
    for i in data:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd != even:
        return False

    i = 0
    j = 1

    while True:
        while i < size and data[i] % 2 == 0:
            i += 2

        while j < size and data[j] % 2 != 0:
            j += 2

        if i >= size or j >= size:
            break

        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp

        i += 2
        j += 2

    return data

# data = []
# data = [2,1,7,12,9]
# data = [2,1,7,12,6,9]
data = [2,1,7,12,9,6]
print(oddEvenSort(data))
