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

# 4.2 Isochoric Process for a Gas
## Problem Statement:
Consider a container with a fixed volume of 0.3 m³ that initially contains helium gas at a temperature of 15°C 
and a pressure of 100 kPa. The gas undergoes an isochoric (constant volume) heating process until its pressure triples. 
Calculate:
1. The final temperature of the helium gas.
2. The change in internal energy of the gas during this process, assuming the specific heat at constant volume (Cv) is known.
3. The total heat transfer to the helium gas.

Use the ideal gas law and assume helium behaves as an ideal gas.


## Solution:

```{code-cell} ipython3

import CoolProp.CoolProp as CP
import math

# Given values
V = 0.3  # Volume in m^3
T1 = 15 + 273.15  # Initial temperature in Kelvin
P1 = 100000  # Initial pressure in Pa (100 kPa)
P2 = 3 * P1  # Final pressure (tripled)
gas = 'Helium'

# 1. Final Temperature (T2)
# Since the process is isochoric, P1/T1 = P2/T2 (Ideal Gas Law)
T2 = P2 * T1 / P1

# 2. Change in internal energy (Δu)
Cv = CP.PropsSI('Cvmass', 'T', T1, 'P', P1, gas)  # Cv for helium
delta_u = Cv * (T2 - T1)

# 3. Total heat transfer (Q)
# For an isochoric process, Q = Δu (First Law of Thermodynamics)
Q = delta_u

# Output the results
print(f"Final Temperature (T2): {round(T2,1)} K")
print(f"Change in internal energy (Δu): {round(delta_u/1e3,1)} kJ")
print(f"Total heat transfer (Q): {round(Q/1e3,1)} kJ")
```

```{code-cell} ipython3

```
