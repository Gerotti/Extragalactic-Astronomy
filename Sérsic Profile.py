import numpy as np
import matplotlib.pyplot as plt

# Define the Sérsic profile function
def sersic_profile(r, n, re, mu_e):
    b_n = 2.17 * n - 0.355  # Approximation for b_n
    return mu_e + b_n * ((r / re)**(1 / n) - 1)

# Parameters
r = np.linspace(0.01, 10, 1000)  # Radius (avoiding zero to prevent log issues)
n_values = [0.2, 0.5, 1, 2, 4]  # Sérsic indices
re = 5  # Effective radius
mu_e = 20  # Surface brightness at effective radius

# Plotting the Sérsic profiles
plt.figure(figsize=(10, 6))
for n in n_values:
    profile = sersic_profile(r, n, re, mu_e)
    plt.plot(r, profile, label=f'n = {n}', linewidth = 0.8)

plt.xlabel('Radius (r)')
plt.ylabel('Surface Brightness (μ)')
plt.title('Sérsic Profile')
plt.legend()
plt.gca().invert_yaxis()
#plt.yscale('log')
#plt.xscale('log')
plt.show()
