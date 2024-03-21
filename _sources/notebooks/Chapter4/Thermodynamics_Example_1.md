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
# Rigid container: Polytropic process

## Problem Statement:
A rigid container with a volume of 0.5 m³ is filled with air at an initial temperature of 27°C and a pressure of 1 atm. 
The air inside the container is then heated until its temperature rises to 127°C. 
Assume that air behaves as an ideal gas with a constant specific heat at constant volume (Cv) 
and that the process is polytropic with an exponent n = 1.4. 

Calculate the following:
1. The change in specific internal energy of the air in the container.
2. The specific heat transfer to the air, assuming the mass of the air in the container is 0.6 kg.
3. The specific boundary work done by the air, considering its polytropic nature.

Use the ideal gas properties for air, and assume the heating process occurs in a closed system 
with no significant changes in kinetic and potential energy.
## Solution:
```{code-cell} ipython3
import CoolProp.CoolProp as CP
import math

# Given values
V = 0.5  # Volume in m^3
T1 = 27 + 273.15  # Initial temperature in Kelvin
T2 = 127 + 273.15  # Final temperature in Kelvin
m = 0.6  # Mass of air in kg
n = 1.4  # Polytropic exponent
R = CP.PropsSI('GAS_CONSTANT', 'Air') / CP.PropsSI('MOLAR_MASS', 'Air')  # Specific gas constant for Air

# Initial pressure (P1) using ideal gas law
P1 = m * R * T1 / V

# 1. Change in specific internal energy (Δu)
Cv = CP.PropsSI('Cvmass', 'T', T1, 'P', P1, 'Air')
delta_u = Cv * (T2 - T1)

# Convert Δu to kJ and round to 1 decimal place
delta_u_kJ = round(delta_u / 1000, 1)

# 3. Specific boundary work (w_boundary)
P2 = m * R * T2 / V  # Final pressure
if n != 1:
    w_boundary = ((P2 * V - P1 * V) / (1 - n)) / m
else:
    w_boundary = P1 * V * math.log(V / V)  # or equivalent with pressures

# Convert w_boundary to kJ and round to 1 decimal place
w_boundary_kJ = round(w_boundary / 1000, 1)
# Convert q to kJ/kg (since delta_u and w_boundary are already in kJ/kg)
q_kJ_kg = delta_u_kJ + w_boundary_kJ

# Output the specific heat transfer (q)
print(f"Specific heat transfer (q): {q_kJ_kg} kJ/kg")

# Output the results
print(f"Change in specific internal energy (Δu): {delta_u_kJ} kJ")
print(f"Specific heat transfer (q): {q_kJ_kg} kJ/kg")
print(f"Specific boundary work (w_boundary): {w_boundary_kJ} kJ")
```
