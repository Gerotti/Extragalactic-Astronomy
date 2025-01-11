import numpy as np
from scipy.optimize import fsolve

#v(theta)
def v_theta(theta):
    return 56.03 * ((theta - np.sin(theta)) / (1 - np.cos(theta))**2) * np.sin(theta) + 120

#Solving
theta_solution = fsolve(v_theta, x0=1)  #Initial guess

theta_solution
