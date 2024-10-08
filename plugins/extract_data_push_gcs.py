import requests
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account


def extraction(response, csv_file_name, credentials):
	if response.status_code == 200:
		result = response.json()
		data_to_be_extracted = ['rank', 'name', 'country']
		rows = []
		for data in result['rank']:
			row = {column: data.get(column, None) for column in data_to_be_extracted}
			rows.append(row)
		final_dataframe = pd.DataFrame(rows, columns=data_to_be_extracted)
		final_dataframe.to_csv(csv_file_name,  mode='a', header=False, index=False)
		print(f"File converted and saved as {csv_file_name}")

		# Set up the client and bucket
		client = storage.Client(credentials=credentials, project='airflow-cricket-statistics')
		bucket_name = 'cricket_online_stats'
		bucket = client.get_bucket(bucket_name)

		# Define the local file path and destination blob
		blob_name = 'icc-rankings.csv'
		# Upload the file
		blob = bucket.blob(blob_name)
		blob.upload_from_filename(csv_file_name)
		print(f"File {csv_file_name} uploaded to {bucket_name}.")

	else:
		print(f"Failed to retrieve data. Status code: {response.status_code}")


