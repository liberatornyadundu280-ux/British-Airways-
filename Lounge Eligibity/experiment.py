# i want to check the rows in the dataset i have
import pandas as pd 
import numpy as np
from pathlib import Path


file_path = Path(__file__).with_name(
    "British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx"
)
data = pd.read_excel(file_path)

print(data.head())     # preview rows
print(list(data.columns)) 
print(data.shape[0])  # prints the number of rows
print(data.shape[1])  # prints the number of columns


# filtering the dataset using DEPARTURE_STATION_CD == 'LHR' and AIRLINE_CD == 'BA' so that we get our first flight from London Heathrow Airport to New York JFK Airport
filtered_data = data[(data['DEPARTURE_STATION_CD'] == 'LHR') & (data['AIRLINE_CD'] == 'BA')]   
# droping the FLIGHT_NO and AIRCRAFT_TYPE from the filtered dataset
# filtered_data = filtered_data.drop(columns=['FLIGHT_NO', 'AIRCRAFT_TYPE'])   
print(filtered_data.shape[0])  # prints the number of rows in the filtered dataset

# now calculating the total seat per flight using the summation of the $$\text{TOTAL\_SEATS} = \text{FIRST\_CLASS\_SEATS} + \text{BUSINESS\_CLASS\_SEATS} + \text{ECONOMY\_SEATS}$$
filtered_data['TOTAL_SEATS'] = filtered_data['FIRST_CLASS_SEATS'] + filtered_data['BUSINESS_CLASS_SEATS'] + filtered_data['ECONOMY_SEATS']

print(filtered_data.head())  # preview the filtered dataset with the new TOTAL_SEATS column

#  EXploratory analysis of the filtered dataset
# 1 grouping our dataset by .groupby(['HAUL', 'TIME_OF_DAY']) 
print(filtered_data.groupby(['HAUL', 'TIME_OF_DAY']).size())  # prints the number of flights for each combination of HAUL and TIME_OF_DAY

# 2 grouping by .groupby(['HAUL', 'ARRIVAL_REGION', 'TIME_OF_DAY'])
print(filtered_data.groupby(['HAUL', 'ARRIVAL_REGION', 'TIME_OF_DAY']).size())  # prints the number of flights for each combination of HAUL, ARRIVAL_REGION, and TIME_OF_DAY

# 3 grouping by ARRIVAL_REGION + TIME_OF_DAY
print(filtered_data.groupby(['ARRIVAL_REGION','TIME_OF_DAY']).size())



# Ensure TOTAL_SEATS is calculated
filtered_data['TOTAL_SEATS'] = filtered_data['FIRST_CLASS_SEATS'] + filtered_data['BUSINESS_CLASS_SEATS'] + filtered_data['ECONOMY_SEATS']

# Group by ARRIVAL_REGION and TIME_OF_DAY
summary = filtered_data.groupby(['ARRIVAL_REGION', 'TIME_OF_DAY']).agg(
    FLIGHTS=('FLIGHT_NO', 'count'),
    TOTAL_SEATS=('TOTAL_SEATS', 'sum'),
    T1_PAX=('TIER1_ELIGIBLE_PAX', 'sum'),
    T2_PAX=('TIER2_ELIGIBLE_PAX', 'sum'),
    T3_PAX=('TIER3_ELIGIBLE_PAX', 'sum')
)

summary['TIER1_%'] = (summary['T1_PAX'] / summary['TOTAL_SEATS'] * 100).round(2)
summary['TIER2_%'] = (summary['T2_PAX'] / summary['TOTAL_SEATS'] * 100).round(2)
summary['TIER3_%'] = (summary['T3_PAX'] / summary['TOTAL_SEATS'] * 100).round(2)

print(summary[['FLIGHTS', 'TIER1_%', 'TIER2_%', 'TIER3_%']])

#  planing the answer by checking the template of the answer we want to give to the questi
path2= Path(__file__).with_name("Lounge Eligibility Lookup Template - Task 1.xlsx")
temp=pd.read_excel(path2)   
print("the number of columns are",temp.shape[1])  # prints the number of columns in the template    
print(list(temp.columns))

# 1. Compute capacity-weighted percentages by HAUL and TIME_OF_DAY
haul_summary = filtered_data.groupby(['HAUL', 'TIME_OF_DAY']).agg(
    FLIGHTS=('FLIGHT_NO', 'count'),
    TOTAL_SEATS=('TOTAL_SEATS', 'sum'),
    T1_PAX=('TIER1_ELIGIBLE_PAX', 'sum'),
    T2_PAX=('TIER2_ELIGIBLE_PAX', 'sum'),
    T3_PAX=('TIER3_ELIGIBLE_PAX', 'sum')
)

haul_summary['Tier 1 %'] = (haul_summary['T1_PAX'] / haul_summary['TOTAL_SEATS'] * 100).round(2)
haul_summary['Tier 2 %'] = (haul_summary['T2_PAX'] / haul_summary['TOTAL_SEATS'] * 100).round(2)
haul_summary['Tier 3 %'] = (haul_summary['T3_PAX'] / haul_summary['TOTAL_SEATS'] * 100).round(2)

print(haul_summary[['FLIGHTS', 'Tier 1 %', 'Tier 2 %', 'Tier 3 %']])

# 2. Check top destinations per HAUL for the 'Example Destinations' column
print("\nTop Short-Haul Destinations:", filtered_data[filtered_data['HAUL']=='SHORT']['ARRIVAL_STATION_CD'].value_counts().head(5).to_dict())
print("Top Long-Haul Destinations:", filtered_data[filtered_data['HAUL']=='LONG']['ARRIVAL_STATION_CD'].value_counts().head(5).to_dict()) 

