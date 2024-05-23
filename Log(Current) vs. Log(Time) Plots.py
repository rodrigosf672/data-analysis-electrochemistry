"""
Author: Rodrigo Silva Ferreira
Project: MSc Thesis in Chemistry - University of Pittsburgh
Date: 04MAR2024
Purpose: Demonstrate how varying diffusion coefficients, concentrations, n values, 
and electrode area affect Log(Current) vs. Log(Time) plots
"""
import numpy as np
import matplotlib.pyplot as plt

n = 1 # Fixed n (e-)
F = 96485.3329  # Faraday constant in C/mol
A = 1E-4  # Area of electrode in m^2 (= 1 cm²)
pi = np.pi # pi value
D_values = np.linspace(1E-10, 1E-9, 5)  # Varying diffusion coefficients in m^2/s
C_values = np.linspace(1E-3, 5E-3, 5)  # Varying concentrations in mol/m^3
D_fixed = 1e-9  # Fixed diffusion coefficient in m^2/s
C_fixed = 1e-3  # Fixed concentration in mol/m^3
n_values = [1, 2, 3, 4, 5] #Varying n values
A_values_cm2 = [1, 2, 5, 10, 50] #Varying Areas
A_values = [A * 1e-4 for A in A_values_cm2]  # Convert from cm² to m²
t = np.linspace(1, 1000, 1000)  # Time range in seconds

plt.figure(figsize=(14, 12)) # Create plot

# Plot 1: (a) Log(Ion Flux) vs. Log(Time) for Different Diffusion Coefficients
plt.subplot(2, 2, 1)
for D in D_values:
    I = (n * F * A * C_values[2] * np.sqrt(D)) / (np.sqrt(pi * t))
    plt.loglog(t, I, label=f'{D:.1e} m²/s')
plt.title('(a) Log(Current) vs. Log(Time) for Different Diffusion Coefficients')
plt.xlabel('Log(Time) (s)')
plt.ylabel('Log(Current) (A)')
plt.legend()

# Plot 2: (b) Log(Ion Flux) vs. Log(Time) for Different Concentrations
plt.subplot(2, 2, 2)
for C in C_values:
    I = (n * F * A * (C / 1000) * np.sqrt(D_values[2])) / (np.sqrt(pi * t))  
# Convert C to mol/L
    plt.loglog(t, I, label=f'{C / 1000:.1e} M')  # Label in M
plt.title('(b) Log(Current) vs. Log(Time) for Different Concentrations')
plt.xlabel('Log(Time) (s)')
plt.ylabel('Log(Current) (A)')
plt.legend()

# Plot 3: (c) Log(Ion Flux) vs. Log(Time) for Different n Values
plt.subplot(2, 2, 3)
for n in n_values:
    I = (n * F * A_values[0] * C_fixed * np.sqrt(D_fixed)) / (np.sqrt(pi * t))
    plt.loglog(t, I, label=f'{n} e-')
plt.title('(c) Log(Current) vs. Log(Time) for Different n Values')
plt.xlabel('Log(Time) (s)')
plt.ylabel('Log(Current) (A)')
plt.legend()

# Plot 4: (d) Log(Ion Flux) vs. Log(Time) for Different Electrode Areas
plt.subplot(2, 2, 4)
for A, A_cm2 in zip(A_values, A_values_cm2):
    I = (n_values[0] * F * A * C_fixed * np.sqrt(D_fixed)) / (np.sqrt(pi * t))
    plt.loglog(t, I, label=f'{A_cm2} cm²')
plt.title('(d) Log(Current) vs. Log(Time) for Different Electrode Areas')
plt.xlabel('Log(Time) (s)')
plt.ylabel('Log(Current) (A)')
plt.legend()
plt.tight_layout()
plt.savefig('CurrentVSTime.jpeg', dpi=300) # Save as .JPEG