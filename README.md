# data-analysis-electrochemistry
Scripts for data analysis for electrochemical applications.

First, I encourage you to understand how different factors impact Log(Current) vs. Log(Time) by running 'Log(Current) vs. Log(Time) Plots.py'. 

Then, run the Savitzky-Golay Filter. To do so, first save the fc_fc+.xlsx file in your local machine. This file was obtained from the following reference:
Copley, G.; Gibson, E. Cyclic Voltammetry of a Cobaloxime Catalyst raw data. Newcastle University: 2019 (licensed under CC BY 4.0). 

After saving the file, change the file path in line 20 of 'Savitzky-Golay Filter for CV data.py' to your file path. 

Finally, run the 'Bar Charts with MSLE.py' file to obtain the MSLE values for my results. You may change the values in the code to obtain for your specific results (which should be similar).