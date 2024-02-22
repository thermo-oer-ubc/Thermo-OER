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

# 1.8 Specific Entropy Calculation

## Problem Statement:
Calculate the specific entropy of a system with a total entropy of 2500 J/K and a mass of 10 kg.

```{code-cell} ipython3
## Solution:

# Given values
S_total = 2500  # Total entropy in J/K
m = 10  # Mass in kg

# Specific entropy calculation
s = S_total / m

# Output the result
print(f"Specific entropy: {round(s/1e3,1)} kJ/(kg*K)")
```
