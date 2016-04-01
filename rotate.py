from ctypes import cdll, CDLL, POINTER, c_int, c_double, c_char_p, c_char, c_void_p
import numpy as np


class rotate(object):
        def __init__(self):
                """
                Class for python hooks for Bob Kurucz rotation broadening function.
                """

                # read in fortran library with ctype hooks
                self.fortran = cdll.LoadLibrary('/Users/Phill/Astro/FAL/BROADEN/librotate.so')

                # define this useful thing for later
                self.c_double_p = POINTER(c_double)

        def rotate(self,):
          pass