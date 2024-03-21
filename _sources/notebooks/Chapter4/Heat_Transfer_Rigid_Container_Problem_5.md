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

# 4.4 Heat Transfer in a Rigid Container

## Problem Statement:
A rigid container is initially filled with 0.5 kg of carbon dioxide at 20°C and 100 kPa. 
The container is then heated until the temperature of the gas reaches 80°C. 
Calculate the amount of heat transferred to the carbon dioxide and the change in its internal energy.

## Solution:

```{code-cell} ipython3
import CoolProp.CoolProp as CP

# Given values
m = 0.5  # Mass of carbon dioxide in kg
T1 = 20 + 273.15  # Initial temperature in Kelvin
T2 = 80 + 273.15  # Final temperature in Kelvin
gas = 'CarbonDioxide'

# 1. Change in internal energy (Δu)
Cv = CP.PropsSI('Cvmass', 'T', T1, 'P', 100000, gas)  # Cv for carbon dioxide
delta_u = Cv * (T2 - T1) * m

# Convert delta_u to kJ and round to one decimal point
delta_u_kJ = round(delta_u / 1000, 1)

# 2. Total heat transfer (Q)
# For a rigid container, Q = Δu (First Law of Thermodynamics)
Q = delta_u

# Convert Q to kJ and round to one decimal point
Q_kJ = round(Q / 1000, 1)

# Output the results
print(f"Change in internal energy (Δu): {delta_u_kJ} kJ")
print(f"Total heat transfer (Q): {Q_kJ} kJ")
```
