import requests
import json

def study_api(api_url):
    # Make an API request
    response = requests.get(api_url)

    # Check the response status code
    if response.status_code == 200:
        # API request was successful, so process the response data

        # Get the response data as a JSON object
        data = response.json()

        # Extract relevant information from the data
        # (e.g. number of items in the response, data types of each item, etc.)
        num_items = len(data)
        item_data_types = []
        for item in data:
            item_data_types.append(type(item))

        # Save the extracted information to a file
        with open('api_study.txt', 'w') as f:
            f.write(f'Number of items in response: {num_items}\n')
            f.write(f'Data types of each item:\n')
            for data_type in item_data_types:
                f.write(f'{data_type}\n')
    else:
        # API request was unsuccessful, so print an error message
        print(f'Error: API request returned status code {response.status_code}')

if __name__ == '__main__':
    study_api('https://api.example.com/endpoint')
