#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    def collatz_cycle_length (i):   # New function to calculate cycle length of single number

        cycle_length = 1

        while i > 1:

            if (i % 2 == 1):
                i = (3 * i) + 1
            else:
                i = i//2

            cycle_length += 1

        assert cycle_length > 0
        return cycle_length

    assert (i > 0 and j > 0)

    cycle_length = 0
    max_cycle_length = 0

    while (i < j or i > j):

        cycle_length = collatz_cycle_length(i)

        if (cycle_length > max_cycle_length):
            max_cycle_length = cycle_length

        if (i < j):
            i += 1

        if (i > j):
            i -= 1   

    return max_cycle_length

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
     
