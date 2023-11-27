#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 00:07:44 2023

@author: joshua
"""
import pandas as pd

# Specify the path to your CSV file
csv_file_path = '/Users/joshua/Library/CloudStorage/OneDrive-Personal/Covid Data Analytics/owid-covid-data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Specify the conditions for selecting rows and columns
condition = df['iso_code'] == 'USA'
selected_columns = ['location', 'date', 'total_cases', 'total_deaths', 'people_fully_vaccinated', 'median_age', 'aged_65_older', 'cardiovasc_death_rate', 'diabetes_prevalence']
# Apply the conditions and select specific columns
selected_data = df.loc[condition, selected_columns]

# Specify the path for the Excel file
excel_file_path = '/Users/joshua/Library/CloudStorage/OneDrive-Personal/Covid Data Analytics/covidParse.xlsx'

# Write the selected data to an Excel file
selected_data.to_excel(excel_file_path, index=False)