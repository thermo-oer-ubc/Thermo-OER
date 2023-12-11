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

# Pressure in a Tank

## Problem Statement:
A cylindrical tank contains air at a gauge pressure of 3 atm and an ambient atmospheric pressure of 1 atm. 
Calculate the absolute pressure inside the tank.

```{code-cell} ipython3
## Solution:

# Given values
P_gauge = 3 * 101325  # Gauge pressure in Pascals (1 atm = 101325 Pa)
P_atm = 1 * 101325  # Atmospheric pressure in Pascals

# Absolute pressure
P_abs = P_gauge + P_atm

# Output the result
print(f"Absolute pressure inside the tank: {round(P_abs/1e3,1)} kPa")
```
