import numpy as np
import matplotlib.pyplot as plt

# Given parameters
r_d = 0.5
v_c = 200

# Define the functions
def v(r):
    return v_c * (1 - np.exp(-r / r_d))

def w(r):
    return v(r) / r

def k(r):
    term1 = r * (2 * v_c**2 / r_d) * np.exp(-r / r_d) * (1 - np.exp(-r / r_d))
    term2 = 4 * (v(r) / r)**2
    return np.sqrt(term1 + term2)

# Generate r values
r_values = np.linspace(-0.01, 50, 500)  # Avoid division by zero by starting from 0.01

# Calculate w(r) and k(r)
w_values = w(r_values)
k_values = k(r_values)

# Calculate w(r) - k(r)/2 and w(r) + k(r)/2
w_minus_k_half = -w_values + k_values / 2 -3.81
w_plus_k_half = w_values + k_values / 2 - 3.81

# Plotting with the additional curves
plt.figure(figsize=(10, 6))
plt.plot(r_values, w_values, label='$\Omega(r)$', linewidth=2)
#plt.plot(r_values, k_values, label='k(r)', linewidth=2)
plt.plot(r_values, w_minus_k_half, label='$\Omega(r) - \kappa(r)/2$', linestyle='--', linewidth=2)
plt.plot(r_values, w_plus_k_half, label='$\Omega(r) + \kappa(r)/2$', linestyle='--', linewidth=2)
plt.xlabel('radius ($kpc$)')
plt.ylabel('Angular Velocity ($km \ s^{-1} \ kpc^{-1}$)')
plt.title('Angular velocity and Lindblad curves')
plt.legend(fontsize=10)


plt.ylim(-10, 75)
plt.xlim(-1, 25)
plt.grid(True)
plt.show()
