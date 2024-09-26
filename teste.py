import numpy as np
n0, nE, F, lmbd = 2.848272, 2.539913, 0.5, 1550e-9
neff = F*n0 + (1-F)*nE
theta = 20 #20 deg
periodo = lmbd / (neff - np.sin(theta*np.pi/180))

print(f'{10*np.log10(0.5) - 10*np.log10(0.437297)}')
Pin = 0.00878
pout1 = 0.003710
pout2 = 0.003777376
avg = (pout1+pout2)/2
a = Pin-(2*pout1)
il = 10*np.log10(Pin) - 10*np.log10(avg)
print(il)
print(a)
#print(f'Largura de banda {1.58261-1.5264}')