import sympy as sp

#Variables
r, rc, n0, T0, k_B, mu, m_p, G, alpha, beta, gamma = sp.symbols('r rc n0 T0 k_B mu m_p G alpha beta gamma')

#n(r), T(r) and ρ(r)
n_r = n0 * (r/rc)**(-alpha) * (1 + (r/rc)**2)**(-3*beta/2)
T_r = T0 * ((r/rc)**alpha * (1 + (r/rc)**2)**(-3*beta/2))**gamma
rho_r = m_p * n_r

#Derivatives
dln_rho_dr = sp.diff(sp.log(rho_r), r)
dln_T_dr = sp.diff(sp.log(T_r), r)

#M(r)
M_r = -(k_B * T_r * r**2 / (G * mu * m_p)) * (dln_rho_dr + dln_T_dr)

#Result
sp.init_printing(use_unicode=True)

p = sp.simplify(dln_rho_dr)
T = sp.simplify(dln_T_dr)
M_r_ = sp.simplify(M_r)
