import pandas as pd


def load_and_normalize_data(raw_dir, normalized_dir):

    # Load data from files
    flights_df = pd.read_csv(f'{raw_dir}/flights.csv')
    weather_df = pd.read_csv(f'{raw_dir}/weather.csv')
    planes_df = pd.read_csv(f'{raw_dir}/planes.csv')
    airports_df = pd.read_csv(f'{raw_dir}/airports.csv')
    airlines_df = pd.read_csv(f'{raw_dir}/airlines.csv')

    # Normalize columns
    # Rename 'faa' to 'airport_code' in airports dataset
    airports_df.rename(columns={'faa': 'airport_code'}, inplace=True)

    # Make sure all key fields are strings and properly formatted
    flights_df['origin'] = flights_df['origin'].astype(str).str.upper()
    flights_df['dest'] = flights_df['dest'].astype(str).str.upper()
    airports_df['airport_code'] = airports_df['airport_code'].astype(str).str.upper()

    # Save the dataframes with standardized columns
    flights_df.to_csv(f'{normalized_dir}/flights.csv', index=False)
    weather_df.to_csv(f'{normalized_dir}/weather.csv', index=False)
    planes_df.to_csv(f'{normalized_dir}/planes.csv', index=False)
    airports_df.to_csv(f'{normalized_dir}/airports.csv', index=False)
    airlines_df.to_csv(f'{normalized_dir}/airlines.csv', index=False)

    print("Normalization complete. Files have been saved in the normalized directory.")


# Usage
raw_directory = 'raw'  # Directory containing raw CSV files
normalized_directory = 'normalized'  # Directory to store normalized CSV files
load_and_normalize_data(raw_directory, normalized_directory)
