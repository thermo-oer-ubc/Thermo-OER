---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: oer
  language: python
  name: python3
---

# 4.1: Piston-cylinder: isothermal expansion

## Problem Statement:
A cylinder fitted with a frictionless piston contains 1 kg of oxygen gas at an initial temperature of 20°C 
and a volume of 0.8 m³. The gas undergoes an isothermal expansion until its volume doubles. 
During the process, the cylinder is in thermal contact with a heat reservoir at 20°C. 

Calculate the following:
1. The specific boundary work done by the oxygen gas during the expansion.
2. The amount of heat transferred to the gas during this process.
3. Assuming the specific internal energy of oxygen changes due to the process, calculate the change in specific internal energy.

For the calculations, assume that oxygen behaves as an ideal gas and use its specific properties. 
Also, consider that the process is isothermal, meaning the temperature remains constant throughout the process.
## Solution:

```{code-cell} ipython3
## Solution:

import CoolProp.CoolProp as CP
import math

# Gas choice
gas = "Oxygen"

# Given values
m = 1.0  # Mass of the gas in kg
T1 = 20 + 273.15  # Initial temperature in Kelvin (converted from 20°C)
V1 = 0.8  # Initial volume in m^3
V2 = 2 * V1  # Final volume (double the initial volume)
R = CP.PropsSI('GAS_CONSTANT', gas) / CP.PropsSI('MOLAR_MASS', gas)  # Specific gas constant for Oxygen

# 1. Specific Boundary Work (w_boundary)
# For an isothermal process, P1 * V1 = P2 * V2 (Ideal Gas Law), and P1 can be found from P1 = m * R * T1 / V1
P1 = m * R * T1 / V1
# Calculating the boundary work
w_boundary = P1 * V1 * math.log(V2 / V1)

# 2. Heat Transfer (Q)
# For an isothermal process, the heat transfer is equal to the boundary work done
Q = w_boundary

# 3. Change in Specific Internal Energy (Δu)
# For an isothermal process of an ideal gas, Δu = 0
delta_u = 0

# Output the results
print(f"Specific Boundary Work (w_boundary): {round(w_boundary/1e3,1)} kJ")
print(f"Heat Transfer (Q): {round(Q/1e3,1)} kJ")
print(f"Change in Specific Internal Energy (Δu): {round(delta_u/1e3,1)} kJ")
```
