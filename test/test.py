import rotate
from astropy.table import Table
import numpy as np

import matplotlib.pyplot as plt

t = Table.read('testspec.fits',format='fits')
t = t[(t['WAVE'] < 1550.0) & (t['WAVE'] > 1549.0)]
print len(t)
wl = np.array(t['WAVE'])
flx = np.array(t['QMU1']/t['QMU2'])
rotatedict = {"NRAD":100,"VROT":100.0}

rot = rotate.rotate()
out = rot.rotate(wl,flx,rotatedict)

print out

# plt.plot(wl,flx,'-r',alpha=0.5)
# plt.plot(out['WAVE'],out['FLUX'],'-b')

# plt.show(block=True)