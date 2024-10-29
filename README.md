# Data Analysis for Electrochemistry

This repository contains scripts for analyzing electrochemical data, specifically for **cyclic voltammetry (CV)** applications. These scripts were developed as part of my Master’s Thesis in Analytical Chemistry at the University of Pittsburgh. You can access the full thesis [here](http://d-scholarship.pitt.edu/46030/).

## Project Overview

The primary goal of these scripts is to demonstrate data analysis techniques for optimizing CV signals and understanding the effects of different parameters on electrochemical reactions.

## Getting Started

### 1. Log(Current) vs. Log(Time) Analysis  
   This script helps you understand how various parameters impact the relationship between Log(Current) and Log(Time). Start by running:

   ```python
   Log(Current) vs. Log(Time) Plots.py
   ```

This script generates plots to analyze the effects of different diffusion coefficients, concentrations, n values, and electrode areas.

### 2. Applying the Savitzky-Golay Filter for CV Data
The **Savitzky-Golay filter** is used to smooth CV data, enhancing signal interpretation. Follow these steps to apply the filter:

- **Step 1**: Download the data file `fc_fc+.xlsx` to your local machine. This data was sourced from:

  > Copley, G.; Gibson, E. *Cyclic Voltammetry of a Cobaloxime Catalyst* raw data. Newcastle University, 2019. (Licensed under CC BY 4.0)

- **Step 2**: Modify the file path on line 20 of the `Savitzky-Golay Filter for CV data.py` script to the location of `fc_fc+.xlsx` on your machine.

- **Step 3**: Run the script to generate filtered plots showing the effects of various window sizes and polynomial orders.

### 3. Calculating MSLE Values for Noise Resistance
This script calculates the **Mean Squared Logarithmic Error (MSLE)** values to assess noise resistance across different models. Run the following script:

```python
Bar Charts with MSLE.py
```
This script creates bar charts with error bars to illustrate the noise resistance of each model based on their MSLE values. You may adjust the values in the code to calculate MSLE for your specific data.
