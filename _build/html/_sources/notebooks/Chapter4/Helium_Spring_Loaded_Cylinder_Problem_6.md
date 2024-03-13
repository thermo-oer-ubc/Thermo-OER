---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 4.5 Helium in a Spring-Loaded Cylinder

## Problem Statement:
A spring-loaded piston-cylinder device contains 0.3 kg of helium. 
Initially, the helium is at 25°C and 150 kPa, and the spring is uncompressed. 
The system is heated until the pressure doubles and the volume increases by 20%. 
Calculate the work done by the helium on the spring and the total heat added to the system.
## Solution:
```{code-cell} ipython3
import CoolProp.CoolProp as CP
import math

# Given values
m = 0.3  # Mass of helium in kg
T1 = 25 + 273.15  # Initial temperature in Kelvin
P1 = 150000  # Initial pressure in Pa

# Calculate the initial volume using the density
V1 = m / CP.PropsSI('D', 'T', T1, 'P', P1, 'Helium')  
V2 = V1 * 1.2  # Final volume (20% increase)
P2 = 2 * P1  # Final pressure (doubled)

# Polytropic exponent for helium
n = CP.PropsSI('Cpmass', 'T', T1, 'P', P1, 'Helium') / CP.PropsSI('Cvmass', 'T', T1, 'P', P1, 'Helium')

# Calculate final temperature T2 using the polytropic process relation
T2 = T1 * (P2 / P1) * (V1 / V2)**n

# Calculate work done by the helium (W)
if n != 1:
    W = (P2 * V2 - P1 * V1) / (1 - n)
else:
    W = P1 * V1 * math.log(V2 / V1)

# Convert W to kJ and round to 1 decimal place
W_kJ = round(W / 1000, 1)

# Calculate the total heat added (Q)
Cv = CP.PropsSI('Cvmass', 'T', T1, 'P', P1, 'Helium')
delta_U = Cv * (T2 - T1) * m

# Convert delta_U to kJ and round to 1 decimal place
delta_U_kJ = round(delta_U / 1000, 1)

# Q is the sum of delta_U and W, converted to kJ and rounded
Q_kJ = round((delta_U + W) / 1000, 1)

# Output the results
print(f"Final Temperature (T2): {round(T2, 1)} K")
print(f"Work done by the helium (W): {W_kJ} kJ")
print(f"Total heat added (Q): {Q_kJ} kJ")
print(f"Change in Internal Energy (ΔU): {delta_U_kJ} kJ")
```
