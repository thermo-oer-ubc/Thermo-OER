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

# Energy in a Moving Vehicle

## Problem Statement:
A car with a mass of 1200 kg is traveling at a speed of 60 km/h. 
If the height above the ground is 50 m, calculate the total stored energy of the car.

```{code-cell} ipython3
## Solution:

# Given values
m = 1200  # Mass of the car in kg
V = 60 * (1000 / 3600)  # Speed in m/s (60 km/h)
g = 9.81  # Acceleration due to gravity in m/s^2
z = 50  # Height in meters

# Total stored energy calculation
E = m * (V**2 / 2 + g * z)

# Output the result
print(f"Total stored energy of the car: {round(E/1e3)} kJ")
```
