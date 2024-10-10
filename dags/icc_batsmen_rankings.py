from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.operators.python import PythonOperator
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from airflow.operators.bash import BashOperator
from extract_data_push_gcs import extraction
from upload_files_to_bucket import upload_files_to_gcs_bucket
from trigger_data_flow_function import trigger_dataflow
import requests
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('RAPIDAPI_KEY')
api_host = os.getenv('RAPIDAPI_HOST')
service_account_path = os.getenv('SERVICE_ACCOUNT_PATH')
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"
querystring = {"formatType": "test"}
headers = {"x-rapidapi-key": api_key, "x-rapidapi-host": api_host}
response = requests.get(url, headers=headers, params=querystring)
credentials = service_account.Credentials.from_service_account_file(service_account_path)
files_to_upload = {
        "json_file_path": "/usr/local/airflow/dataset/data/bq_schema.json",
        "udf.js": "/opt/airflow/plugins/transform.js"
    }

@dag(
    start_date=datetime(2024, 10, 5),
    schedule=None,
    catchup=False,
    tags=['cric_ranks'],
)

def cric_ranks():
    # PythonOperator calling the extraction function
    ingest_csv_to_gcs = PythonOperator(
        task_id='ingest_csv_to_gcs',
        python_callable=extraction,
        op_kwargs={
            'response': response,  # Pass the API response
            'csv_file_name': '/usr/local/airflow/dataset/data/extracted_data.csv',  # Local file path
            'credentials': credentials
        },
    )
    build_ranking_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="build_ranking_dataset",
        dataset_id="icc_batsmen_rankings",
        gcp_conn_id="gcp",
    )
    upload_files_data_flow = PythonOperator(
        task_id='upload_files_data_flow',
        python_callable=upload_files_to_gcs_bucket,
        op_kwargs={
            'files_to_upload': files_to_upload,
            'credentials': credentials
        },
    )
    trigger_cloud_function = PythonOperator(
        task_id='trigger_cloud_function',
        python_callable=trigger_dataflow,
        op_kwargs={
            'credentials': credentials
        }
    )
    # Setting task dependencies
    ingest_csv_to_gcs >> build_ranking_dataset >> trigger_cloud_function

cric_ranks()