import numpy as np
from scipy.optimize import newton

#constants
kpc = 3e+19  #kiloparsec in meters
rc = 50 * kpc  #meters
alpha = 0.9
beta = 2/3
gamma = 0.5
mp = 1.6e-27  #kg
G = 6.8e-11  #m^3 kg^-1 s^-2
H0 = (70 * 1000) / (kpc * 1e3)
kT0 = 4 * 1.60e-16  #Joules
rhoc = 3 * H0**2 / (8 * np.pi * G)  #critical density kg/m^3

def mass_density(r, multiplier):
    mass_density = -kT0 * r**2 / (G * mp) * ((r/rc)**alpha * (1 + (r/rc)**2)**(-3*beta/2))**gamma
    mass_density *= ((alpha/r) * (gamma-1) - (3*beta*r/(r**2 + rc**2)) * (gamma+1))
    return mass_density / (4/3 * np.pi * r**3) - multiplier * rhoc

def find_radius(multiplier, initial_guess): #Newton-Raphson method to find the root where mass density equation equals zero
    radius_solution = newton(mass_density, initial_guess, args=(multiplier,))
    return radius_solution / kpc

#R_200 and R_500
initial_guess = 100 * kpc
R_200_kpc = find_radius(200, initial_guess)
R_500_kpc = find_radius(500, initial_guess)

display(R_200_kpc, R_500_kpc, rhoc)
