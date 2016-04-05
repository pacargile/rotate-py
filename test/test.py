import rotate
from astropy.table import Table
import numpy as np

# import matplotlib.pyplot as plt

t = Table.read('testspec.fits',format='fits')
wl = np.array(t['WAVE'])
flx = np.array(t['QMU1']/t['QMU2'])
rotatedict = {"NRAD":10,"VROT":100.0}

rot = rotate.rotate()
out = rot.rotate(wl,flx,rotatedict)

# plt.plot(t['WAVE'],t['FLUX'],'-r',alpha=0.5)
# plt.plot(out['WAVE'],out['FLUX'],'-b')

# plt.show()