ICC Top ODI Batsmen Rankings Data Pipeline
========
This project is a data pipeline that automates the process of extracting ICC top ODI batsmen rankings data from [RapidAPI] (https://rapidapi.com/hub), transforming it, and visualizing the results using Google Cloud Platform (GCP) and Looker Studio. The entire workflow is orchestrated using Apache Airflow.

Project Overview
================
The objective of this project is to automate the data extraction, transformation, and reporting for ICC Top ODI Batsmen Rankings. The workflow follows these steps:

1. Data Extraction: Retrieve ICC Top ODI Batsmen Rankings data from RapidAPI.
2. Data Transformation & Storage: Convert the extracted data into a CSV file and store it in a Google Cloud Storage (GCS) bucket.
3. BigQuery Dataset: Define a BigQuery dataset, apply a schema via a .json file, and create a transformation function using JavaScript.
4. Dataflow Transformation: Use Google Cloud Dataflow to automate the process of reading data from GCS, applying the transformation function using the defined schema, and loading the data into BigQuery.
5. Visualization: Connect the transformed data in BigQuery to Looker Studio for analytics and visualization.
6. Automation: Apache Airflow is used to orchestrate the entire workflow.

Tools and Technologies
================
1. [Apache Airflow] (https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html): Workflow automation and orchestration.
2. [Google Cloud Platform (GCP)] To get started with GCP, follow the [GCP Getting Started guide] (https://cloud.google.com/gcp/?hl=de&utm_source=google&utm_medium=cpc&utm_campaign=emea-de-all-de-bkws-all-all-trial-e-gcp-1707574&utm_content=text-ad-none-any-DEV_c-CRE_529379242747-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+-+GCP+-+General+-+v3-KWID_43700060393213364-kwd-6458750523-userloc_9043130&utm_term=KW_google%20cloud-NET_g-PLAC_&&gad_source=1&gclid=CjwKCAjwufq2BhAmEiwAnZqw8iAtk2q3eyQdrytn-Z14REzRsSd1fHfMZUBM71_Jh_GF2vzkOL74LxoCqV4QAvD_BwE&gclsrc=aw.ds): Cloud infrastructure.
    - Google Cloud Storage (GCS): Storage for raw CSV data.
    - BigQuery: Data warehousing for storing transformed data. 
    - Dataflow: Managed service for stream and batch processing of data.
3. Looker Studio: For building visual analytics dashboards.
4. RapidAPI: Source of ICC Top ODI Batsmen Rankings data.
5. Python: For scripting and development.
6. JavaScript: For defining BigQuery transformation functions.

Workflow Steps
================

1. Data Extraction
- Retrieve data from the ICC Top ODI Batsmen Rankings API using RapidAPI.
- Use Python to extract the data and convert it into a CSV file.
- Store the CSV file in a local folder.

2. Upload Data to GCS
- Upload the CSV file to a specified Google Cloud Storage (GCS) bucket.

3. BigQuery Dataset Setup
- Create a BigQuery dataset.
- Define a schema in a JSON file that will be used to map the fields of the data.
- Write a JavaScript transformation function that cleanses and formats the data for loading into BigQuery.

4. Dataflow Pipeline
- Set up a Dataflow pipeline that:
  - Reads the data from the GCS bucket.
  -  Applies the transformation function using the schema.
  - Loads the transformed data into the BigQuery table.
  
5. Data Visualization in Looker Studio
- Connect the transformed BigQuery data to Looker Studio.
- Build dashboards and reports to visualize the ICC Top ODI Batsmen Rankings.

6. Workflow Automation with Apache Airflow
- Apache Airflow is used to schedule and automate the end-to-end workflow, from data extraction to visualization.
- The pipeline tasks are organized into a Directed Acyclic Graph (DAG) in Airflow, which orchestrates the data extraction, GCS upload, Dataflow processing, and reporting in Looker Studio.

Installation and Setup
================
Prerequisites
-------------
Ensure the following are installed and set up:

- Python 3.x: For scripting and Airflow setup.
- Apache Airflow: Installed and configured.
- Google Cloud SDK: To interact with GCP services.
- BigQuery & Dataflow APIs: Enabled in GCP.
- RapidAPI Key: For accessing the ICC data.

1. Start the Airflow web server and scheduler.
`docker-compose up`

3. Trigger the DAG
   - Access the Airflow web interface at http://localhost:8080, and manually trigger the DAG to start the ETL process.
3. Monitor and Check
   - Monitor the progress of the ETL pipeline in the Airflow web interface. Check the BigQuery dataset and table to ensure data has been loaded correctly, and review the quality check results.
