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

# 1.4 Enthalpy of a Steam

## Problem Statement:
Calculate the specific enthalpy of steam at a pressure of 200 kPa and a specific volume of 0.15 m³/kg.

```{code-cell} ipython3
## Solution:

import CoolProp.CoolProp as CP

# Given values
P = 200000  # Pressure in Pascals
v = 0.15  # Specific volume in m^3/kg

# Specific enthalpy calculation
h = CP.PropsSI('H', 'P', P, 'D', 1/v, 'Water')

# Output the result
print(f"Specific enthalpy of steam: {round(h/1e3,1)} kJ/kg")
```
