import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Constants
c = 299792.458
H0 = 67.0

#Cosmological parameters for a flat LambdaCDM universe
Omega_m = 0.27
Omega_Lambda = 0.73

def E(z):
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_Lambda)

def integrand(z):
    return 1.0 / E(z)

def comoving_distance(z):
    integral, error = quad(integrand, 0, z)
    return (c / H0) * integral

def angular_diameter_distance(z):
    return comoving_distance(z) / (1 + z)

#Generate redshifts
z_values = np.linspace(0, 15, 10000)
D_A_values = np.array([angular_diameter_distance(z) for z in z_values])

#Find the maximum value of D_A
max_D_A = np.max(D_A_values)
max_index = np.argmax(D_A_values)
max_z = z_values[max_index]

print(f"Maximum Angular Diameter Distance: {max_D_A} Mpc at Redshift z = {max_z}")

#Plot the results
plt.figure(figsize=(10, 6))
plt.plot(z_values, D_A_values, color = 'gray')
plt.axvline(x=max_z, color='orange', linestyle='--', label=f'Peak at z = {max_z:.2f}')
plt.axhline(y=max_D_A, color='blue', linestyle='--', label=f'Maximum D_A = {max_D_A:.0f} Mpc')
#plt.xscale('log')
#plt.yscale('log')
plt.grid(True, linewidth=0.2)
plt.xlabel('Redshift')
plt.ylabel('Angular Diameter Distance (Mpc)')
plt.title('Maximum Angular Diameter Distance')
plt.legend()
plt.show()
