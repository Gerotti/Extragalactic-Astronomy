import numpy as np
import matplotlib.pyplot as plt


# Constants for the universe and NFW profile
rho_crit = 132.9  #M_sun/Kpc^3
M_200 = 1e12  #M_sun
c = 8  #Concentration parameter
L_tot = 3e10  #solar luminosities

#R200
R_200 = (3 * M_200 / (800 * np.pi * rho_crit))**(1/3)  # in kpc

#Rs
R_s = R_200 / c

#rho_0
rho_0 = M_200 / (4 * np.pi * R_s**3 * (np.log(1 + c) - c / (1 + c)))

#Mass within radius R for NFW profile
def mass_nfw(R, rho_0, R_s):
    return 4 * np.pi * rho_0 * R_s**3 * (np.log(1 + R / R_s) - R / (R + R_s))

# Radii
R_values = np.linspace(0.1, 220, 400)

#Mass within each radius
M_R = np.array([mass_nfw(R, rho_0, R_s) for R in R_values])

#Mass-to-luminosity ratio within each radius
M_to_L_ratio = M_R / L_tot

#Plotting
plt.figure(figsize=(10, 6))
plt.plot(R_values, M_to_L_ratio, label='Mass/Luminosity Ratio', color = 'orange')
plt.xlabel('Radius (kpc)')
plt.ylabel('Mass-to-Luminosity Ratio ($M_{\odot}/L_{\odot}$)')
plt.title('Mass-to-Luminosity Ratio within Radius $R$')
plt.grid(False)
plt.yscale('log')

plt.axhline(y=1, color='blue', linestyle='--', label='M/L = 1')
intersect_radius = np.interp(1, M_to_L_ratio, R_values)
plt.annotate(f'$R = {intersect_radius:.2f} kpc$', xy=(intersect_radius, 1), xytext=(intersect_radius+10, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))

plt.legend()
plt.show()

display(R_200)
