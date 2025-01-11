import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from astropy.cosmology import FlatLambdaCDM

# Load the data from the file
data = pd.read_csv("/content/Pantheon_SNdata.dat", delim_whitespace=True)

# Extract columns
z = data['z']
mag = data['mag']
err_mag = data['err_mag']

# Constants
M_abs = -19.4  # Absolute magnitude of Ia Supernova
H0 = 68.5  # Hubble constant in km/s/Mpc

# Define cosmological models
cosmo_model_1 = FlatLambdaCDM(H0=H0, Om0=0.3)  # ΩΛ = 0.7, ΩM = 0.3
cosmo_model_2 = FlatLambdaCDM(H0=H0, Om0=1.0)  # ΩΛ = 0, ΩM = 1

# Generate an array of redshifts from 0 to 1.5 (extend slightly beyond 1 for better curve visibility)
z_vals = np.linspace(0.01, 2.5, 1000)

# Compute distance modulus for each model
mu_model_1 = cosmo_model_1.distmod(z_vals).value  # Model 1 distance modulus
mu_model_2 = cosmo_model_2.distmod(z_vals).value  # Model 2 distance modulus

# Compute apparent magnitude for each model (m = M + mu)
mag_model_1 = M_abs + mu_model_1
mag_model_2 = M_abs + mu_model_2

# Plot the data and the models
plt.figure(figsize=(10, 6))

# Plot the observational data with error bars
plt.errorbar(
    z, mag, yerr=err_mag, fmt='o', ecolor='gray', capsize=2, markersize=1,
    markerfacecolor='blue', markeredgecolor='blue', label='Observed Data'
)

# Plot the two cosmological models
plt.plot(z_vals, mag_model_1, label=r'$\Omega_\Lambda=0.7, \Omega_M=0.3$', color='green')
plt.plot(z_vals, mag_model_2, label=r'$\Omega_\Lambda=0, \Omega_M=1$', color='red')

# Set labels and title
plt.xlim(0, 2.5)
plt.xlabel('Redshift (z)')
plt.ylabel('Magnitude')
plt.title('Magnitude vs Redshift for Ia Supernovas with Cosmological Models')
plt.legend()
plt.grid()

# Show the plot
plt.show()
