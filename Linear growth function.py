import numpy as np
import matplotlib.pyplot as plt
from astropy.cosmology import FlatLambdaCDM, LambdaCDM
from scipy.integrate import solve_ivp

#Define cosmologiey
cosmo_LCDM = FlatLambdaCDM(H0=70, Om0=0.3, Ob0=0.0)  #Flat LambdaCDM
cosmo_OCDM = LambdaCDM(H0=70, Om0=0.3, Ode0=0.0)     #Open CDM (no Lambda)
cosmo_SCDM = FlatLambdaCDM(H0=70, Om0=1.0, Ob0=0.0)  #SCDM (flat with Omega_m = 1)

#Define Hubble parameter
def H_t_astropy(cosmology, t_gyr):
    return cosmology.H(t_gyr)

#Growth rate equation using H(t)
def growth_eq_astropy(t, y, cosmology):
    delta_plus, ddelta_plus_dt = y
    H = H_t_astropy(cosmology, t).value / 3.086e19 * 3.1536e16 * 1e9  #Convert H to Gyr^-1
    d2delta_plus_dt2 = -(1/t) * ddelta_plus_dt + 3 * cosmology.Om0 / (2 * H**2 * t**2) * delta_plus
    return [ddelta_plus_dt, d2delta_plus_dt2]

#Solve growth factor δ_+(t) using astropy cosmology
def solve_growth_astropy(cosmology, t_start=0.1, t_end=14):
    #Initial conditions at t_start (early universe)
    delta_0 = 1e-6  #Small initial value for delta_+
    delta_prime_0 = delta_0  #Initial derivative

    #Time points
    t_eval = np.linspace(t_start, t_end, 1000)  # Increase number of time points for smoothness

    #Solve the system of ODEs
    sol = solve_ivp(
        growth_eq_astropy,
        [t_start, t_end],
        [delta_0, delta_prime_0],
        args=(cosmology,),
        t_eval=t_eval,  #Evaluate solution at these points
        rtol=1e-6, atol=1e-9
    )

    #Normalize the solution at t_end (today)
    delta_today = sol.y[0, -1]
    delta_normalized = sol.y[0] / delta_today  # Normalize δ_+(t_end) = 1

    return sol.t, delta_normalized

#Plot
plt.figure(figsize=(10, 6))

for label, cosmology in zip(["ΛCDM", "OCDM", "SCDM"], [cosmo_LCDM, cosmo_OCDM, cosmo_SCDM]):
    time_vals, delta_vals = solve_growth_astropy(cosmology)
    plt.plot(time_vals, delta_vals, label=label)

plt.xlabel("Universe Age (Gyr)")
plt.ylabel("Normalized Growth Factor δ₊(t)")
plt.title("Growth Factor Evolution")
plt.legend()
plt.grid(True, linewidth=0.2)
plt.show()
