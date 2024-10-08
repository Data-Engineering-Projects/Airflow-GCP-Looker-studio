from googleapiclient.discovery import build
import base64
import google.auth
import os


def trigger_dataflow(credentials):
    service = build('dataflow', 'v1b3', credentials=credentials)
    project = "airflow-cricket-statistics"
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"
    template_body = {
        "jobName": "bq-load-final",  # Provide a unique name for the job
        "parameters": {
            "javascriptTextTransformGcsPath": "gs://schema_and_data_transform/udf.js",
            "JSONPath": "gs://schema_and_data_transform/json_file_path",
            "javascriptTextTransformFunctionName": "transform",
            "outputTable": "airflow-cricket-statistics:icc_batsmen_rankings.odi_batsmen_rankings",
            "inputFilePattern": "gs://cricket_online_stats/icc-rankings.csv",
            "bigQueryLoadingTemporaryDirectory": "gs://schema_and_data_transform",
        }
    }

    request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
