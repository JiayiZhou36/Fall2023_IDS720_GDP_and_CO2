# import library
import pandas as pd
import matplotlib

# read csv
gdp = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# extract columns
print(gdp["Mortality rate, infant (per 1,000 live births)"])
print(gdp["GDP per capita (constant 2010 US$)"])
print(gdp["Country Name"])

# Plot a scatter plot
gdp.plot.scatter(
    x="Mortality rate, infant (per 1,000 live births)",
    y="GDP per capita (constant 2010 US$)",
)
