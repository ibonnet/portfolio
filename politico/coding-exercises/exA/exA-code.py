import eurostat
import pandas as pd

def get_inflation_data(component_code):
    # Set Eurostat API parameters
    api_params = {
        'precision': 1,
        'unit': 'PC',
        'geo': 'EU27_2020',
        'time_format': 'month',
        'time_order': 'ascending'
    }
    # Get data from Eurostat API
    data = eurostat.get_data_df(component_code, params=api_params)
    # Rename columns for readability
    data = data.rename(columns={'value': component_code})
    # Convert time column to YYYY-MM format
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m')
    data['time'] = data['time'].dt.strftime('%Y-%m')
    return data

# Define main function to download and save inflation data
def download_inflation_data():
    # Define list of inflation components to retrieve
    components = ['CPH_HICP', 'CPH_FOOD', 'CPH_ALCO', 'CPH_ENER', 'CPH_TOTF']
    # Create empty dataframes for each country and inflation component
    country_dfs = {country: pd.DataFrame() for country in eurostat.get_geo_info()['geo']}
    component_dfs = {component: pd.DataFrame() for component in components}
    # Loop through inflation components and retrieve data for each country
    for component in components:
        data = get_inflation_data(component)
        for country in country_dfs.keys():
            country_df = data[data['geo'] == country][['time', component]]
            country_df = country_df.set_index('time')
            country_dfs[country][component] = country_df[component]
        component_df = data.pivot(index='time', columns='geo', values=component)
        component_dfs[component] = component_df
    # Add EU27_2020 total inflation to country dataframes
    eu_total = component_dfs['CPH_TOTF']['EU27_2020']
    for country in country_dfs.keys():
        country_dfs[country]['EU27_2020'] = eu_total
    # Save dataframes to Excel files in indicated formats
    with pd.ExcelWriter('inflation_by_country.xlsx') as writer:
        for country, df in country_dfs.items():
            df.to_excel(writer, sheet_name=country)
    with pd.ExcelWriter('inflation_by_component.xlsx') as writer:
        for component, df in component_dfs.items():
            df.to_excel(writer, sheet_name=component)

# Call main function to download and save data
download_inflation_data()
