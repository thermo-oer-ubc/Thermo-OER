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

# 4.6 Isothermal Expansion of Nitrogen

## Problem Statement:
A cylinder with a movable piston contains 1 kg of nitrogen at 100 kPa and 300 K. 
It undergoes an isothermal expansion until the volume triples. 
Calculate the boundary work done during this process and the heat transfer involved.

## Solution:

```{code-cell} ipython3

import CoolProp.CoolProp as CP
import math

# Given values
m = 1.0  # Mass of nitrogen in kg
T = 300  # Temperature in Kelvin (constant)
P1 = 100000  # Initial pressure in Pa
V1 = m * CP.PropsSI('Dmolar', 'T', T, 'P', P1, 'Nitrogen')  # Initial volume using density
V2 = 3 * V1  # Final volume (tripled)

# 1. Boundary work (W)
# For isothermal process, W = nRT ln(V2/V1)
R = CP.PropsSI('GAS_CONSTANT', 'Nitrogen') / CP.PropsSI('MOLAR_MASS', 'Nitrogen')
W = m * R * T * math.log(V2 / V1)

# 2. Heat transfer (Q)
# For an isothermal process, Q = W
Q = W

# Output the results
print(f"Boundary work done (W): {round(W/1e3,1)} kJ")
print(f"Heat transfer (Q): {round(Q/1e3,1)} kJ")
```
