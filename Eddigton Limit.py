import numpy as np
import matplotlib.pyplot as plt

#Constants
M_BN_0 = 10
k = 1.372e-8  #Growth rate
years = np.linspace(10**6, 10**9, 1000)

#Mass growth equation
M_BN = M_BN_0 * np.exp(k * years)

#Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, M_BN, color = 'orange', label = f'M$_{{BN}}$ = {M_BN_0} $e^{{kt}}$')
plt.xlabel('Time (years)')
plt.ylabel('Mass of Black Hole ($M_{\odot}$)')
plt.title('Growth of Black Hole Mass')

t1 = 3e8
t2 = 1e9
plt.axvline(x=t1, color='grey', linestyle='--', label='$t = 3 \\times 10^8$ years')
plt.axvline(x=t2, color='blue', linestyle='--', label='$t = 10^9$ years')

#intersection
y1 = M_BN_0 * np.exp(k * t1)
y2 = M_BN_0 * np.exp(k * t2)
plt.scatter([t1, t2], [y1, y2], color='red')
plt.text(t1, y1, f'{y1:.1e}', fontsize=10, verticalalignment='top')
plt.text(t2, y2, f'{y2:.1e}', fontsize=10, verticalalignment='top')

plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(False)
plt.show()
