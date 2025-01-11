from scipy.integrate import quad

#Constants
total_mass = 1e9
m_low = 0.08      #Lower mass limit
m_up = 120        #Upper mass limit
sn_low = 8        #Lower mass limit for SN progenitors
sn_up = 100       #Upper mass limit for SN progenitors

#Kroupa IMF parameters
def kroupa_imf(m, alpha1=1.3, alpha2=2.3, break1=0.5, break2=1.0):
    if m < break1:
        return m**-alpha1
    elif m < break2:
        return (break1**-alpha1) * (m/break1)**-alpha2
    else:
        return (break1**-alpha1) * (break2/break1)**-alpha2 * (m/break2)**-alpha2

#Normalization
def normalized_imf(m):
    return m * kroupa_imf(m)

#Total mass integral
total_mass_integral, _ = quad(normalized_imf, m_low, m_up)

#Normalization constant k
k = total_mass / total_mass_integral
print(k)

#Number of supernovae progenitors
def sn_imf(m):
    return kroupa_imf(m) * k

num_sn_progenitors, _ = quad(sn_imf, sn_low, sn_up)

#Total number of stars formed
def total_stars_imf(m):
    return sn_imf(m)

num_total_stars, _ = quad(total_stars_imf, m_low, m_up)

#Fraction of stars that become supernovae
fraction_sn = num_sn_progenitors / num_total_stars

num_total_stars, num_sn_progenitors, fraction_sn
