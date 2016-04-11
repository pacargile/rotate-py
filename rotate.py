from ctypes import cdll, CDLL, POINTER, c_int, c_double, c_char_p, c_char, c_void_p
import numpy as np


class rotate(object):
        def __init__(self):
            """
            Class for python hooks for Bob Kurucz rotation broadening function.
            """

            # read in fortran library with ctype hooks
            self.fortran = cdll.LoadLibrary('/Users/pcargile/Astro/bin/FORTRAN/SYNTHE/lib/librotate.so')

            # define this useful thing for later
            self.c_double_p = POINTER(c_double)

        def rotate(self,wli,fluxi,rotatedict):
            """
            Function
            """

            # make sure arrays are numpy arrays with dtype=double
            wli = np.array(wli,dtype="double")
            fluxi = np.array(fluxi,dtype="double")

            # define other needed parameters
            NWL = len(wli) # number of rows in spectrum

            # determine how many MU angles input spectrum contains
            try:
                NMU = int(fluxi.shape[1]) # First see if it has multiple MU angles
            except IndexError:
                NMU = int(1) # threw an error because only a single spectrum
            
            # Number of radii Vrot calculated at (default = 100)
            if 'NRAD' in rotatedict.keys():
                NRADIUS = int(rotatedict['NRAD'])
            else:
                NRADIUS = int(100)

            # Rotation Velocity
            VROT = float(rotatedict['VROT'])

            # define output array
            fluxo = np.zeros(NWL,dtype="double")

            # run the fortran rotation broadening code
            self.fortran.rotate(
                wli.ctypes.data_as(self.c_double_p),                
                fluxi.ctypes.data_as(self.c_double_p),
                fluxo.ctypes.data_as(self.c_double_p),
                c_int(NWL),
                c_int(NMU),
                c_int(NRADIUS),
                c_double(VROT)
                )

            return {"WAVE":wli,"FLUX":fluxo}