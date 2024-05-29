import pandas as pd
import requests
from tabulate import tabulate

# Sample DataFrame
data = {
    'org': ['ibm inc', 'Microsoft Corp.', 'go0gle llc','IBM','Google','Microsot', 'Amazon', 'microsfttt']
}
df = pd.DataFrame(data)

# API details
url = 'https://api.interzoid.com/getcompanymatchadvanced'
headers = {
    'x-api-key': 'Your-Interzoid-API-Key'    # obtain at www.interzoid.com
}

# Function to call the API and get the simkey
def get_simkey(org):
    params = {
        'company': org,
        'algorithm': 'ai-plus'   # kicks in the AI-enhanced algorithms
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("SimKey", None)
    else:
        return None

# Apply the function to each row in the DataFrame
df['simkey'] = df['org'].apply(get_simkey)

# Sort the DataFrame by simkey
df_sorted = df.sort_values(by='simkey').reset_index(drop=True)

# Filter out records that don't have at least one other record with the same simkey
filtered_df = df_sorted[df_sorted.duplicated(subset=['simkey'], keep=False)]

# Proceed only if there are records with duplicate simkeys
if not filtered_df.empty:
    # Insert blank lines where simkey changes
    output_rows = []
    previous_simkey = None

    for index, row in filtered_df.iterrows():
        if previous_simkey is not None and row['simkey'] != previous_simkey:
            # Insert a blank row (as a dictionary of NaN values)
            blank_row = pd.Series([None] * len(filtered_df.columns), index=filtered_df.columns)
            output_rows.append(blank_row)
        output_rows.append(row)
        previous_simkey = row['simkey']

    # Create a new DataFrame from the rows with blank lines inserted
    output_df = pd.concat(output_rows, axis=1).T.reset_index(drop=True)

    # Replace None with empty string
    output_df.fillna('', inplace=True)

    # Convert the DataFrame to a table with left-justified columns
    table = tabulate(output_df, headers='keys', tablefmt='plain', stralign='left')

    # Print the table
    print(table)
else:
    print("No records with duplicate simkeys found.")
