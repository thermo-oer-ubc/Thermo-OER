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

# Compressed Liquid Approximation

## Problem Statement:
For water at 50°C under high pressure, approximate the specific volume, internal energy, enthalpy, and entropy 
assuming it behaves as a compressed liquid.

```{code-cell} ipython3
## Solution:

import CoolProp.CoolProp as CP

# Given values
T = 50 + 273.15  # Temperature in Kelvin

# Approximations for compressed liquid
v = CP.PropsSI('D', 'T', T, 'Q', 0, 'Water')  # Specific volume
u = CP.PropsSI('U', 'T', T, 'Q', 0, 'Water')/1e3  # Specific internal energy
h = CP.PropsSI('H', 'T', T, 'Q', 0, 'Water')/1e3  # Specific enthalpy
s = CP.PropsSI('S', 'T', T, 'Q', 0, 'Water')/1e3  # Specific entropy

# Output the results
print(f"Specific volume: {round(v,2)} m^3/kg")
print(f"Specific internal energy: {round(u,2)} kJ/kg")
print(f"Specific enthalpy: {round(h,2)} kJ/kg")
print(f"Specific entropy: {round(s,2)} kJ/kg*K")
```
