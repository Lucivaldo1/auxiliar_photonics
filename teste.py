import numpy as np
n0 = 2.848272
nE = 2.539913
F = 0.5
lmbd = 1550e-9
neff = F*n0 + (1-F)*nE
theta = 20 #20 deg
periodo = lmbd / (neff - np.sin(theta*np.pi/180))

print(neff)
print(periodo)