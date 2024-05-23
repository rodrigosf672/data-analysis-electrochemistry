"""
Author: Rodrigo Silva Ferreira
Project: MSc Thesis in Chemistry - University of Pittsburgh
Date: 17MAR2024
Purpose: Plot bar charts with error to compare resistance to noise of the four different models,
         based on the average MSLE values of each model.
"""

import matplotlib.pyplot as plt
import numpy as np
models = ['31, 1', '31, 5', '101, 1', '101, 5']
avg_msle = [0.439, 0.711, 0.736, 0.505]
std_dev = [0.391, 0.456, 0.318, 0.353]
positions = np.arange(len(models))
width = 0.5
fig, ax = plt.subplots()
bars = ax.bar(positions, avg_msle, width, yerr=std_dev, capsize=5, color='skyblue', edgecolor='black')
ax.set_xlabel('Model (Window Size, Polynomial Order)')
ax.set_ylabel('Average MSLE')
ax.set_xticks(positions)
ax.set_xticklabels(models)
plt.tight_layout()
plt.savefig('Resistance to Noise - Bar Charts with Errors.jpeg', dpi=300) # Save as .JPEG