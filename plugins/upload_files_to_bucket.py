from google.cloud import storage

def upload_files_to_gcs_bucket(files_to_upload, credentials):

    storage_client = storage.Client(credentials=credentials)
    bucket_name = "schema_and_data_transform"
    bucket = storage_client.get_bucket(bucket_name)
    # Upload each file
    for file_name, file_path in files_to_upload.items():
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_name} to {bucket_name}")
