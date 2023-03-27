# Coding exercise A: Inflation

This repository contains the coding exercise that explorews inflation in EU countries by inflation component. To download monthly inflation data from Eurostat and save it to Excel in the indicated formats, I will use the eurostat and pandas libraries in Python.

I first installed the eurostat library by running pip install eurostat. This code defines two main functions: <b>get_inflation_data()</b> to retrieve data for a single inflation component, and <b>download_inflation_data()</b> to download and save data for all components and countries. The latter function loops through each component and retrieves data for each country, storing it in a dictionary of dataframes. It then pivots the dataframes to create a separate dataframe for each component, and adds the EU27_2020 total inflation to each country dataframe. It saves the dataframes to two separate Excel files in the indicated formats.
