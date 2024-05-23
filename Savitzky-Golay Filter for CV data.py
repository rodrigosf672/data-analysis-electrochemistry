"""
Author: Rodrigo Silva Ferreira
Project: MSc Thesis in Chemistry - University of Pittsburgh
Date: 21FEB2024
Purpose: Demonstrate how data analysis techniques can be helpful to optimize CV signals
Method: 
Plot CV data: original data from Fc/Fc+, noisy data, and filtered data using Savitzky-Golay filter
Expectation: Four plots containing original CV data, noisy data, and filtered data 
with four combinations of window sizes and polynomial orders.
"""

# Step 1: Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import math

# Step 2: Load data from Excel file and extract potentials and currents from columns
file_path = '/Users/ros114/Downloads/8269661/fc_fc+.xlsx'
data = pd.read_excel(file_path)
E = data['E /V']
I = data['I /uA']

# Step 3: Define four different combinations for window sizes and polynomial orders.
combinations = [
    (31, 1),
    (31, 5),
    (101, 1),
    (101, 5),
]

# Step 4: Add varying levels of random noise to the original data.
noise_levels = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
for noise in noise_levels:
    msle_results = []
    I_noisy = I + np.random.normal(0, max(I) * noise, size=I.shape)  # Calculate max_current within the loop

    # Step 5: Prepare plots 2x2 with the respective sizes.
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    axs = axs.flatten()

    # Step 6: Apply the Savitzky-Golay filter and plot them.
    for i, (window_length, poly_order) in enumerate(combinations):
        I_restored = savgol_filter(I_noisy, window_length, poly_order)

        # Step 7: Define data within specified potential range of the observed peak (-0.5 to 0.2V)
        valid_indices = (E >= -0.5) & (E <= 0.2)
        E_valid = E[valid_indices]
        I_original_valid = I[valid_indices]
        I_restored_valid = I_restored[valid_indices]

        # Step 8: Calculate mean squared logarithmic error (MSLE) of the results
        msle = np.mean((np.log(I_original_valid + 1) - np.log(I_restored_valid + 1)) ** 2)
        msle_results.append((window_length, poly_order, msle))

        # Step 9: Define parameters for plots
        axs[i].plot(E, I, label='Original CV Data', color='blue', linewidth=2)
        axs[i].plot(E, I_noisy, label='Noisy CV Data', color='red', linewidth=1, alpha=0.5)
        axs[i].plot(E, I_restored, label='Filtered CV Data', color='green', linewidth=2)
        axs[i].set_title(f"Window Size: {window_length}, Polynomial Order: {poly_order}, Noise: {noise}, MSLE: {msle:.2f}")
        axs[i].set_xlabel('Potential (V)')
        axs[i].set_ylabel('Current (µA)')
        axs[i].legend()
        axs[i].invert_xaxis()
        axs[i].set_xticks(np.arange(E.max(), E.min() - 0.1, -0.1))

    # Step 10: Print results in the terminal
    print(f"Results for Noise Level: {noise}")
    for window_length, poly_order, msle in msle_results:
        print(f"Window Size: {window_length}, Polynomial Order: {poly_order}, Noise: {noise}, MSLE: {msle:.2f}")

    # Step 11: Create plots and display them
    plt.tight_layout()
    plt.show()