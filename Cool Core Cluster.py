
import matplotlib.pyplot as plt

def temperature_profile(r, T0, rc, alpha, beta, gamma):
    return T0 * ((r/rc)**alpha * (1 + (r/rc)**2)**(-3*beta/2))**gamma

#Parameters
T0 = 4.6e7  #kelvin (calculated from the definition of keV)
rc = 50
alpha = 0.9
beta = 2/3
gamma = 0.5

#Radius array
r = np.linspace(0.1, 500, 400)

#Temperature profile
T_r = temperature_profile(r, T0, rc, alpha, beta, gamma)

#Plotting
plt.figure(figsize=(10, 6))
plt.plot(r, T_r, label='Temperature Profile $T(r)$', color='orange')
plt.xlabel('Radius (kpc)')
plt.ylabel('Temperature (K)')
plt.title('Galaxy Cluster Temperature Profile')
#plt.yscale('log')
plt.grid(False)
plt.legend()
plt.show()
