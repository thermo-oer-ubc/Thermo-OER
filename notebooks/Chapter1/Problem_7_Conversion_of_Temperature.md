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
  name: oerminimal
---

# 1.7 Conversion of Temperature

## Problem Statement:
Convert a temperature of 20°C to Kelvin.

```{code-cell} ipython3
## Solution:

# Given value
T_Celsius = 20  # Temperature in Celsius

# Conversion to Kelvin
T_Kelvin = T_Celsius + 273.15

# Output the result
print(f"Temperature in Kelvin: {T_Kelvin} K")
```
