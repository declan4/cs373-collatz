#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "8 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  8)
        self.assertEqual(j, 2)

    def test_read_3 (self) :
        s    = "4.1 11\n"
        self.assertRaises(ValueError, lambda: collatz_read(s))

    def test_read_4 (self) :
        s    = "4 d\n"
        self.assertRaises(ValueError, lambda: collatz_read(s))

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)  

    def test_eval_6 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174) 

    def test_eval_7 (self) :
        v = collatz_eval(60, 60)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 5000, 10000, 262)
        self.assertEqual(w.getvalue(), "5000 10000 262\n")  

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 100, 3, 119)
        self.assertEqual(w.getvalue(), "100 3 119\n")  

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("345 345\n1269 7814\n400 200\n100 59\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "345 345 126\n1269 7814 262\n400 200 144\n100 59 119\n")

    def test_solve_3 (self) :
        r = StringIO("500 1\n1298 1299\n1 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "500 1 144\n1298 1299 146\n1 3 8\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()



"""
# pragma: no cover

% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""

