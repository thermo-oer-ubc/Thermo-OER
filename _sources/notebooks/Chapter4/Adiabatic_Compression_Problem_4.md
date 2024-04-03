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

# 4.3 Adiabatic Compression of an Ideal Gas

## Problem Statement:
A piston-cylinder device initially contains 2 kg of air at 25°C and 1 atm. 
The air is compressed adiabatically to one-eighth of its original volume. 
Calculate:
1. The final temperature and pressure of the air.
2. The work done during this adiabatic compression process.
3. Assuming air behaves as an ideal gas with a specific heat ratio (γ), determine the change in internal energy.
## Solution:

```{code-cell} ipython3
import CoolProp.CoolProp as CP
import math

# Given values
m = 2.0  # Mass of air in kg
T1 = 25 + 273.15  # Initial temperature in Kelvin
P1 = 101325  # Initial pressure in Pa (1 atm)
V1 = 1.0  # Initial volume (arbitrary value)
V2 = V1 / 8  # Final volume (one-eighth of initial)
gamma = CP.PropsSI('Cpmass', 'T', T1, 'P', P1, 'Air') / CP.PropsSI('Cvmass', 'T', T1, 'P', P1, 'Air')  # γ for air

# 1. Final Temperature and Pressure (T2, P2)
# For adiabatic process, T1 * V1^(gamma - 1) = T2 * V2^(gamma - 1)
T2 = T1 * (V1 / V2) ** (gamma - 1)
# P2 using the adiabatic relation P2 * V2^gamma = P1 * V1^gamma
P2 = P1 * (V1 / V2) ** gamma

# 2. Work done (W)
# For adiabatic process, W = (P1 * V1 - P2 * V2) / (gamma - 1)
W = (P1 * V1 - P2 * V2) / (gamma - 1)

# 3. Change in internal energy (Δu)
# Δu = Q - W, but for adiabatic process, Q = 0
delta_u = -W

# Output the results
print(f"Final Temperature (T2): {round(T2,1)} K")
print(f"Final Pressure (P2): {round(P2/1e3,1)} kPa")
print(f"Work done (W): {round(W/1e3,1)} kJ")
print(f"Change in internal energy (Δu): {round(delta_u/1e3,1)} kJ")
```
